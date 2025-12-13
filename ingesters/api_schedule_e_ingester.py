import argparse
import os
import json
import time
from datetime import datetime, timedelta, timezone
from core.logger import get_logger
from core.database import db_cursor
from core.state_tracker import (
    get_last_run,
    update_last_run,
    get_checkpoint,
    update_checkpoint,
    clear_checkpoint,
    get_checkpoint_started_at,
)
from core.fetcher import fetch_with_retries
from core.alerting import send_slack_alert
from core.utils import load_committee_list
from core.db_batch import execute_batch_with_retry

logger = get_logger()

FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_API_URL = "https://api.open.fec.gov/v1/schedules/schedule_e/"
PAGE_SIZE = 100
SLEEP_SECONDS = 3.7
DAYS_BACK = 30
SORT_COLUMN = "-expenditure_date"

ALL_FIELDS = [
    "action_code", "action_code_full", "amendment_indicator", "amendment_number", "amendment_indicator_desc",
    "back_reference_schedule_name", "back_reference_transaction_id", "candidate", "candidate_first_name", "candidate_id",
    "candidate_last_name", "candidate_middle_name", "candidate_name", "candidate_office", "candidate_office_district",
    "candidate_office_full", "candidate_office_state", "candidate_office_state_full", "candidate_party", "candidate_prefix",
    "candidate_suffix",
    "affiliated_committee_name", "candidate_ids", "committee_city", "committee_committee_id", "committee_type",
    "committee_type_full", "committee_cycle", "committee_cycles", "committee_cycles_has_activity", "committee_cycles_has_financial",
    "committee_designation", "committee_designation_full", "committee_filing_frequency", "committee_first_f1_date",
    "committee_first_file_date", "committee_is_active", "committee_jfc_committee", "committee_last_cycle_has_activity", "committee_last_cycle_has_financial",
    "committee_last_f1_date", "committee_last_file_date", "committee_name", "committee_organization_type", "committee_organization_type_full",
    "committee_party", "committee_party_full", "committee_state", "committee_state_full", "committee_street_1", "committee_street_2",
    "committee_treasurer_name", "committee_zip",
    "committee_id", "committee_name2", "conduit_committee_city", "conduit_committee_id", "conduit_committee_name", "conduit_committee_state",
    "conduit_committee_street1", "conduit_committee_street2", "conduit_committee_zip", "disbursement_dt", "dissemination_date",
    "election_type", "election_type_full", "expenditure_amount", "expenditure_date", "expenditure_description", "file_number",
    "filer_first_name", "filer_last_name", "filer_middle_name", "filer_prefix", "filer_suffix", "filing_date", "filing_form",
    "form_line_number", "image_number", "independent_sign_date", "independent_sign_name", "is_notice", "line_number", "line_number_label", "link_id",
    "memo_code", "memo_code_full", "memo_text", "memoed_subtotal", "most_recent", "notary_commission_expiration_date",
    "notary_sign_date", "notary_sign_name", "office_total_ytd", "original_sub_id", "payee_city", "payee_first_name",
    "payee_last_name", "payee_middle_name", "payee_name", "payee_prefix", "payee_state", "payee_street_1", "payee_street_2",
    "payee_suffix", "payee_zip", "pdf_url", "previous_file_number", "report_type", "report_year", "schedule_type",
    "schedule_type_full", "semi_annual_bundled_refund", "sub_id", "support_oppose_indicator", "transaction_id"
]

def adapt_value(val):
    if isinstance(val, (dict, list)):
        return json.dumps(val)
    return val

def run(committee_id=None, resume_index=None, resume_date=None):
    logger.info(f"Starting schedule E ingester {'for ALL committees' if not committee_id else f'for {committee_id}'}")
    run_started_at = datetime.now(timezone.utc)

    total_inserted = 0
    page = 1
    params = {}

    try:
        params = {
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": SORT_COLUMN,
        }
        if committee_id:
            params["committee_id"] = committee_id
            # Use the new target-based state tracking
            last_run = get_last_run("schedule_e", target=committee_id)
        else:
            # "All committees" mode
            last_run = get_last_run("schedule_e", target="all")

        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date()
            min_date = (last_run_date - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
            params["min_date"] = min_date

        total_inserted = 0
        last_indexes = {}

        #Resume functionality ONLY for "all" committees run
        #CLI resume overrides checkpoint
        
        if not committee_id and resume_index and resume_date:
            logger.info(f"Resuming from last_index={resume_index} and last_expenditure_date={resume_date}")
            last_indexes["last_index"] = resume_index
            last_indexes["last_expenditure_date"] = resume_date
        elif not committee_id:
            checkpoint = get_checkpoint("schedule_e", target="all")
            if checkpoint:
                logger.info(f"Auto-resuming from checkpoint: {checkpoint}")
                last_indexes = checkpoint

        while True:
            # Clean old keys from params
            for key in list(params.keys()):
                if key in last_indexes:
                    params.pop(key)

            # Add pagination keys
            for key, value in last_indexes.items():
                params[key] = value

            logger.info(
                f"Fetching page {page}\n"
                f"   - min_date: {params.get('min_date')}\n"
                f"   - last_index: {params.get('last_index')}\n"
                f"   - last_expenditure_date: {params.get('last_expenditure_date')}"
            )

            data = fetch_with_retries(FEC_API_URL, params)
            results = data.get('results', [])
            pagination = data.get('pagination', {})
            last_indexes = pagination.get('last_indexes', {})

            if not results:
                if committee_id:
                    # Update for specific committee
                    update_last_run("schedule_e", run_started_at, target=committee_id)
                else:
                    # Update for "all committees" mode
                    update_last_run("schedule_e", run_started_at, target="all")
                    clear_checkpoint("schedule_e", target="all")
                logger.info(f"Schedule E ingester complete. Total rows inserted: {total_inserted}")
                break

            rows = [
                tuple(adapt_value(result.get(field)) for field in ALL_FIELDS)
                for result in results
            ]

            columns = ', '.join(f'"{field}"' for field in ALL_FIELDS)
            placeholders = ', '.join(['%s'] * len(ALL_FIELDS))
            update_set = ', '.join([
                f'"{field}" = EXCLUDED."{field}"'
                for field in ALL_FIELDS if field != "sub_id"
            ])
            update_where = ' OR '.join([
                f'schedule_e_expenditures."{field}" IS DISTINCT FROM EXCLUDED."{field}"'
                for field in ALL_FIELDS if field != "sub_id"
            ])

            insert_sql = f"""
                INSERT INTO schedule_e_expenditures (
                    {columns}
                ) VALUES (
                    {placeholders}
                )
                ON CONFLICT (sub_id)
                DO UPDATE SET
                    {update_set},
                    last_updated = CASE WHEN {update_where} THEN NOW() ELSE schedule_e_expenditures.last_updated END
                WHERE {update_where}
            """
            execute_batch_with_retry(db_cursor, insert_sql, rows, sleep_seconds=SLEEP_SECONDS)

            logger.info(f"Inserted {len(rows)} rows from page {page}.")
            total_inserted += len(rows)

            if not last_indexes:
                if committee_id:
                    # Update for specific committee
                    update_last_run("schedule_e", run_started_at, target=committee_id)
                else:
                    # Update for "all committees" mode
                    update_last_run("schedule_e", run_started_at, target="all")
                    clear_checkpoint("schedule_e", target="all")
                logger.info(f"Schedule E ingester complete. Total rows inserted: {total_inserted}")
                break
            elif not committee_id:
                update_checkpoint("schedule_e", last_indexes, target="all")

            page += 1
            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.error(
            f"Schedule E ingester encountered an error\n"
            f"   - Error: {str(e)}\n"
        )
        send_slack_alert(
            f"❌ *Schedule E Ingester FAILED*\n"
            f"> Error: `{str(e)}`\n"
        )
        raise

    finally:
        pass

def main(args=None):
    parser = argparse.ArgumentParser(description="Run Schedule E ingester with optional resume index.")
    parser.add_argument("--resume-index", type=str, help="The last_index to resume from")
    parser.add_argument("--resume-date", type=str, help="The last_disbursement_date to resume from (YYYY-MM-DD)")
    args = parser.parse_args()
    
    committee_list = load_committee_list()
    if not committee_list:
        run(resume_index=args.resume_index, resume_date=args.resume_date)
    else:
        for committee_id in committee_list:
            run(committee_id=committee_id)

if __name__ == "__main__":
    main()