import argparse
import os
import json
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from psycopg2.extras import execute_batch
from core.logger import get_logger
from core.database import get_db_connection
from core.state_tracker import get_last_run, update_last_run, get_checkpoint, update_checkpoint, clear_checkpoint
from core.fetcher import fetch_with_retries

load_dotenv()
logger = get_logger("api_schedule_a_ingester")

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

def run(resume_index=None, resume_date=None):
    logger.info("Starting schedule A ingester")
    run_started_at = datetime.now()

    conn = None
    total_inserted = 0
    page = 1

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        last_run = get_last_run("schedule_a")
        params = {
            "two_year_transaction_period": TWO_YEAR_TRANSACTION_PERIOD,
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": SORT_COLUMN,
        }
        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date()
            min_load_date = (last_run_date - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
            params["min_load_date"] = min_load_date

        total_inserted = 0
        last_indexes = {}

        #CLI resume overrides checkpoint
        if resume_index and resume_date:
            logger.info(f"Resuming from last_index={resume_index} and last_contribution_receipt_date={resume_date}")
            last_indexes["last_index"] = resume_index
            last_indexes["last_contribution_receipt_date"] = resume_date
        else:
            checkpoint = get_checkpoint("schedule_a")
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
                f"   - min_load_date: {params.get('min_load_date')}\n"
                f"   - last_index: {params.get('last_index')}\n"
                f"   - last_contribution_receipt_date: {params.get('last_contribution_receipt_date')}"
            )

            data = fetch_with_retries(FEC_API_URL, params)

            results = data.get('results', [])
            pagination = data.get('pagination', {})
            last_indexes = pagination.get('last_indexes', {})

            if not results:
                update_last_run("schedule_a", run_started_at)
                clear_checkpoint("schedule_a")
                logger.info(f"Schedule A ingester complete. Total rows inserted: {total_inserted}")
                break

            rows = []
            for result in results:
                row = [result.get(field) for field in SCHEDULE_A_FIELDS]
                rows.append(tuple(row))

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
            execute_batch(cur, insert_sql, rows)
            conn.commit()
            logger.info(f"Inserted {len(rows)} rows from page {page}.")
            total_inserted += len(rows)

            if not last_indexes:
                update_last_run("schedule_a", run_started_at)
                clear_checkpoint("schedule_a")
                logger.info(f"Schedule A ingestion complete. Total rows inserted: {total_inserted}")
                break
            else:
                update_checkpoint("schedule_a", last_indexes)

            page += 1
            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.error(
            f"Schedule A ingester encountered an error\n"
            f"   - Error: {str(e)}\n"
            f"   - Params: {json.dumps(params, indent=2)}"
        )
        raise
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
