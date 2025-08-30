import argparse
import os
import json
import time
from datetime import datetime, timedelta
from psycopg2.extras import execute_batch
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

logger = get_logger()

FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_API_URL = "https://api.open.fec.gov/v1/schedules/schedule_b/"
PAGE_SIZE = 100
SLEEP_SECONDS = 3.7
DAYS_BACK = 0
SORT_COLUMN = '-disbursement_date'
TWO_YEAR_TRANSACTION_PERIOD = 2026

ALL_FIELDS = [
    "amendment_indicator", "amendment_indicator_desc", "back_reference_schedule_name", "back_reference_transaction_id",
    "beneficiary_committee_name", "candidate_first_name", "candidate_id", "candidate_last_name", "candidate_middle_name",
    "candidate_name", "candidate_office", "candidate_office_district", "candidate_office_full", "candidate_office_state",
    "candidate_office_state_full", "candidate_party", "candidate_prefix", "candidate_suffix", "committee_id", "committee_name",
    "conduit_committee_city", "conduit_committee_id", "conduit_committee_name", "conduit_committee_state", "conduit_committee_street1",
    "conduit_committee_street2", "conduit_committee_zip", "disbursement_amount", "disbursement_date", "disbursement_description",
    "disbursement_type", "disbursement_type_full", "entity_type", "entity_type_desc", "fec_election_type_desc", "fec_election_year",
    "file_number", "filing_form", "image_number", "is_electioneering_communication", "is_independent_expenditure", "is_party_expenditure",
    "line_number", "line_number_label", "link_id", "load_date", "memo_code", "memo_code_full", "memo_text", "memoed_subtotal",
    "national_committee_nonfederal_account", "original_sub_id", "pdf_url", "recipient_city", "recipient_committee_designation",
    "recipient_committee_designation_full", "recipient_committee_id", "recipient_committee_name", "recipient_committee_org_type",
    "recipient_committee_org_type_full", "recipient_committee_type", "recipient_committee_type_full", "recipient_name", "recipient_state",
    "recipient_street_1", "recipient_street_2", "recipient_zip", "ref_disp_excess_amt", "ref_disp_excess_amt_desc", "ref_disp_excess_flg",
    "ref_disp_excess_flg_desc", "report_type", "report_year", "schedule_type", "schedule_type_full", "semi_annual_bundled_refund",
    "sub_id", "transaction_id", "two_year_transaction_period", "unused_recipient_id"
]

# Known bad indexes causing FEC server timeouts
BROKEN_LAST_INDEXES = {
    "1022620190037443452",  
    "1021420250265768489",
}

def run(committee_id=None, resume_index=None, resume_date=None):  
    logger.info(f"Starting schedule B ingester {'for ALL committees' if not committee_id else f'for {committee_id}'}")
    run_started_at = datetime.now()

    total_inserted = 0
    page = 1
    params = {}
    
    try:
        params = {
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": SORT_COLUMN,
            "two_year_transaction_period": TWO_YEAR_TRANSACTION_PERIOD,
        }

        if committee_id:
            params["committee_id"] = committee_id
            # Use the new target-based state tracking
            last_run = get_last_run("schedule_b", target=committee_id)
        else:
            # "All committees" mode
            last_run = get_last_run("schedule_b", target="all")

        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date()
            min_load_date = (last_run_date - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
            params["min_load_date"] = min_load_date

        total_inserted = 0
        last_indexes = {}

        #Resume functionality ONLY for "all" committees run
        #CLI resume overrides checkpoint
        if not committee_id and resume_index and resume_date:
            logger.info(f"Resuming from last_index={resume_index} and last_disbursement_date={resume_date}")
            last_indexes["last_index"] = resume_index
            last_indexes["last_disbursement_date"] = resume_date
            params["sort_null_only"] = True  # Required to enable keyset pagination resume
        elif not committee_id:
            checkpoint = get_checkpoint("schedule_b", target="all")
            if checkpoint:
                logger.info(f"Auto-resuming from checkpoint: {checkpoint}")
                last_indexes = checkpoint
                params["sort_null_only"] = True

        while True:
            # Clean old keys from params
            for key in list(params.keys()):
                if key in last_indexes:
                    params.pop(key)

            # Add pagination keys
            for key, value in last_indexes.items():
                params[key] = value

            last_index = last_indexes.get("last_index")

            if last_index in BROKEN_LAST_INDEXES:
                logger.warning(f"Reducing page size to skip through bad last_index {last_index}")
                params["per_page"] = 10  # Drop from 100 to 10 just for this call

            logger.info(
                f"Fetching page {page}\n"
                f"   - min_load_date: {params.get('min_load_date')}\n"
                f"   - last_index: {params.get('last_index')}\n"
                f"   - last_disbursement_date: {params.get('last_disbursement_date')}"
            )

            data = fetch_with_retries(FEC_API_URL, params)
            results = data.get('results', [])
            pagination = data.get('pagination', {})
            last_indexes = pagination.get('last_indexes', {})

            if not results:
                if committee_id:
                    # Update for specific committee
                    update_last_run("schedule_b", run_started_at, target=committee_id)
                else:
                    # Update for "all committees" mode
                    update_last_run("schedule_b", run_started_at, target="all")
                    clear_checkpoint("schedule_b", target="all")
                logger.info(f"Schedule B ingester complete. Total rows inserted: {total_inserted}")
                break

            rows = [
                tuple(result.get(field) for field in ALL_FIELDS)
                for result in results
            ]

            insert_sql = f"""
                INSERT INTO schedule_b_disbursements (
                    {', '.join(ALL_FIELDS)}
                ) VALUES (
                    {', '.join(['%s'] * len(ALL_FIELDS))}
                )
                ON CONFLICT (sub_id) DO UPDATE SET
                    {', '.join([
                        f"{field} = EXCLUDED.{field}" 
                        for field in ALL_FIELDS 
                        if field != "sub_id"
                    ])},
                    last_updated = CURRENT_TIMESTAMP
                WHERE { ' OR '.join([
                    f"schedule_b_disbursements.{field} IS DISTINCT FROM EXCLUDED.{field}" 
                    for field in ALL_FIELDS 
                    if field != "sub_id"
                ])}
            """
            with db_cursor() as cur:
                execute_batch(cur, insert_sql, rows)

            logger.info(f"Inserted {len(rows)} rows from page {page}.")
            total_inserted += len(rows)

            if not last_indexes:
                if committee_id:
                    # Update for specific committee
                    update_last_run("schedule_b", run_started_at, target=committee_id)
                else:
                    # Update for "all committees" mode
                    update_last_run("schedule_b", run_started_at, target="all")
                    clear_checkpoint("schedule_b", target="all")
                logger.info(f"Schedule B ingester complete. Total rows inserted: {total_inserted}")
                break
            elif not committee_id:
                update_checkpoint("schedule_b", last_indexes, target="all")

            page += 1
            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.error(
            f"Schedule B ingester encountered an error\n"
            f"   - Error: {str(e)}\n"
            f"   - Params: {json.dumps(params, indent=2)}"
        )
        send_slack_alert(
            f"❌ *Schedule B Ingester FAILED*\n"
            f"> Error: `{str(e)}`\n"
            f"> Params: ```{json.dumps(params, indent=2)}```"
        )
        raise

    finally:
        pass

def main(args=None):
    parser = argparse.ArgumentParser(description="Run Schedule B ingester with optional resume index.")
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