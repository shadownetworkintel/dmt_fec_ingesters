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
FEC_API_URL = "https://api.open.fec.gov/v1/schedules/schedule_a"
PAGE_SIZE = 100
SLEEP_SECONDS = 3.7
DAYS_BACK = 2
TWO_YEAR_TRANSACTION_PERIOD = 2026
SORT_COLUMN = "-contribution_receipt_date"

SCHEDULE_A_FIELDS = [
    "amendment_indicator", "amendment_indicator_desc", "back_reference_schedule_name",
    "back_reference_transaction_id", "candidate_first_name", "candidate_id", "candidate_last_name",
    "candidate_middle_name", "candidate_name", "candidate_office", "candidate_office_district",
    "candidate_office_full", "candidate_office_state", "candidate_office_state_full", "candidate_prefix",
    "candidate_suffix", "committee_id", "committee_name", "conduit_committee_city", "conduit_committee_id",
    "conduit_committee_name", "conduit_committee_state", "conduit_committee_street1", "conduit_committee_street2",
    "conduit_committee_zip", "contribution_receipt_amount", "contribution_receipt_date",
    "contributor_aggregate_ytd", "contributor_city", "contributor_employer", "contributor_first_name",
    "contributor_id", "contributor_last_name", "contributor_middle_name", "contributor_name",
    "contributor_occupation", "contributor_prefix", "contributor_state", "contributor_street_1",
    "contributor_street_2", "contributor_suffix", "contributor_zip", "donor_committee_name", "election_type",
    "election_type_full", "entity_type", "entity_type_desc", "fec_election_type_desc", "fec_election_year",
    "file_number", "filing_form", "image_number", "increased_limit", "is_individual", "line_number",
    "line_number_label", "link_id", "load_date", "memo_code", "memo_code_full", "memo_text", "memoed_subtotal",
    "national_committee_nonfederal_account", "original_sub_id", "pdf_url", "receipt_type", "receipt_type_desc",
    "receipt_type_full", "recipient_committee_designation", "recipient_committee_org_type",
    "recipient_committee_type", "report_type", "report_year", "schedule_type", "schedule_type_full", "sub_id",
    "transaction_id", "two_year_transaction_period", "unused_contbr_id"
]

def run(committee_id=None, resume_index=None, resume_date=None):
    logger.info(f"Starting schedule A ingester {'for ALL committees' if not committee_id else f'for {committee_id}'}")
    run_started_at = datetime.now(timezone.utc)

    total_inserted = 0
    page = 1
    params = {}

    try:
        params = {
            "two_year_transaction_period": TWO_YEAR_TRANSACTION_PERIOD,
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": SORT_COLUMN,
        }

        if committee_id:
            params["committee_id"] = committee_id
            # Use the new target-based state tracking
            last_run = get_last_run("schedule_a", target=committee_id)
        else:
            # "All committees" mode
            last_run = get_last_run("schedule_a", target="all")

        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date()
            min_load_date = (last_run_date - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
            params["min_load_date"] = min_load_date

        last_indexes = {}
        checkpoint_started_at = None
        
        #Resume functionality ONLY for "all" committees run
        #CLI resume overrides checkpoint
        if not committee_id and resume_index and resume_date:
            logger.info(f"Resuming from last_index={resume_index} and last_contribution_receipt_date={resume_date}")
            last_indexes = {
                "last_index": resume_index,
                "last_contribution_receipt_date": resume_date,
            }
        elif not committee_id:
            checkpoint = get_checkpoint("schedule_a", target="all")
            if checkpoint:
                logger.info(f"Auto-resuming from checkpoint: {checkpoint}")
                last_indexes = {k: v for k, v in checkpoint.items() if k != "started_at"}
                # Get the original started_at from the checkpoint
                checkpoint_started_at = get_checkpoint_started_at("schedule_a", target="all")
                if checkpoint_started_at:
                    logger.info(f"Using checkpoint started_at: {checkpoint_started_at}")

        # Use checkpoint started_at if resuming, otherwise use current time
        effective_started_at = checkpoint_started_at or run_started_at

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
                f"   - min_load_date: {params.get('min_load_date')}\n"
                f"   - last_index: {params.get('last_index')}\n"
                f"   - last_contribution_receipt_date: {params.get('last_contribution_receipt_date')}"
            )

            data = fetch_with_retries(FEC_API_URL, params)
            results = data.get('results', [])
            pagination = data.get('pagination', {})
            last_indexes = pagination.get('last_indexes', {})

            if not results:
                if committee_id:
                    # Update for specific committee
                    update_last_run("schedule_a", run_started_at, target=committee_id)
                else:
                    # Update for "all committees" mode using effective started time
                    update_last_run("schedule_a", effective_started_at, target="all")
                    clear_checkpoint("schedule_a", target="all")
                logger.info(f"Schedule A ingester complete. Total rows inserted: {total_inserted}")
                break

            rows = [tuple(result.get(field) for field in SCHEDULE_A_FIELDS) for result in results]

            insert_sql = f"""
                INSERT INTO schedule_a_contributions (
                    {', '.join(SCHEDULE_A_FIELDS)}
                ) VALUES (
                    {', '.join(['%s'] * len(SCHEDULE_A_FIELDS))}
                )
                ON CONFLICT (sub_id) DO UPDATE
                SET
                    {', '.join(
                        f"{col} = EXCLUDED.{col}"
                        for col in SCHEDULE_A_FIELDS
                        if col not in ("sub_id", "ingestion_date", "last_updated")
                    )},
                    last_updated = CASE
                        WHEN { ' OR '.join(
                            f"schedule_a_contributions.{col} IS DISTINCT FROM EXCLUDED.{col}"
                            for col in SCHEDULE_A_FIELDS
                            if col not in ("sub_id", "ingestion_date", "last_updated")
                        )}
                        THEN CURRENT_TIMESTAMP
                        ELSE schedule_a_contributions.last_updated
                    END
            """
            execute_batch_with_retry(db_cursor, insert_sql, rows, sleep_seconds=SLEEP_SECONDS)
                
            logger.info(f"Inserted {len(rows)} rows from page {page}.")
            total_inserted += len(rows)

            if not last_indexes:
                if committee_id:
                    # Update for specific committee
                    update_last_run("schedule_a", run_started_at, target=committee_id)
                else:
                    # Update for "all committees" mode using effective started time
                    update_last_run("schedule_a", effective_started_at, target="all")
                    clear_checkpoint("schedule_a", target="all")
                logger.info(f"Schedule A ingestion complete. Total rows inserted: {total_inserted}")
                break
            elif not committee_id:
                # Save checkpoint with started_at timestamp
                update_checkpoint("schedule_a", last_indexes, target="all", started_at=effective_started_at)

            page += 1
            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.error(
            f"Schedule A ingester encountered an error\n"
            f"   - Error: {str(e)}\n"
        )
        send_slack_alert(
            f"❌ *Schedule A Ingester FAILED*\n"
            f"> Error: `{str(e)}`\n"
        )
        raise
    finally:
        pass

def main(args=None):
    parser = argparse.ArgumentParser(description="Run Schedule A ingester with optional resume index.")
    parser.add_argument("--resume-index", type=str, help="The last_index to resume from")
    parser.add_argument("--resume-date", type=str, help="The last_contribution_receipt_date to resume from (YYYY-MM-DD)")
    args = parser.parse_args()
    
    committee_list = load_committee_list()
    if not committee_list:
        run(resume_index=args.resume_index, resume_date=args.resume_date)
    else:
        for committee_id in committee_list:
            run(committee_id=committee_id)

if __name__ == "__main__":
    main()