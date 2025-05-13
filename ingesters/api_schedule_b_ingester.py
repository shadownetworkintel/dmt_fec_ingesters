import os
import json
import time
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv
from psycopg2.extras import execute_batch
from core.logger import get_logger
from core.database import get_db_connection
from core.state_tracker import get_last_run, update_last_run

load_dotenv()
logger = get_logger("api_schedule_b_ingester")

FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_API_URL = "https://api.open.fec.gov/v1/schedules/schedule_b/"
PAGE_SIZE = 100
SLEEP_SECONDS = 3.7
DAYS_BACK = 2
SORT_COLUMN = '-disbursement_date'

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

def run():    
    logger.info("Starting schedule B ingester")

    conn = None
    total_inserted = 0
    page = 1

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        last_run = get_last_run("schedule_b")
        params = {
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": SORT_COLUMN
        }
        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date()
            min_load_date = (last_run_date - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
            params["min_load_date"] = min_load_date

        total_inserted = 0
        last_indexes = {}

        while True:
            # Remove any old pagination keys from params
            for key in list(params.keys()):
                if key in last_indexes:
                    params.pop(key)

            # Add all keys from last_indexes to params
            for key, value in last_indexes.items():
                params[key] = value

            logger.info(
                f"Fetching page {page}\n"
                f"   - min_load_date: {params.get('min_load_date')}\n"
                f"   - last_index: {params.get('last_index')}\n"
                f"   - last_disbursement_date: {params.get('last_disbursement_date')}"
            )
            response = requests.get(FEC_API_URL, params=params)
            response.raise_for_status()

            if response.status_code != 200:
                logger.error(
                    f"API request failed\n"
                    f"   - Status code: {response.status_code}\n"
                    f"   - URL: {response.url}\n"
                    f"   - min_load_date: {params.get('min_load_date')}\n"
                    f"   - last_index: {params.get('last_index')}\n"
                    f"   - last_disbursement_date: {params.get('last_disbursement_date')}\n"
                    f"   - Response snippet: {response.text.strip()[:300]}"
                )
                break
            data = response.json()

            results = data.get('results', [])
            pagination = data.get('pagination', {})
            last_indexes = pagination.get('last_indexes', {})
            print(f"LAST INDEXES: {last_indexes}")

            if not results:
                update_last_run("schedule_b")
                logger.info(f"Schedule B ingester complete. Total rows inserted: {total_inserted}")
                break

            rows = []
            for result in results:
                row = tuple(result.get(field) for field in ALL_FIELDS)
                rows.append(row)

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
            execute_batch(cur, insert_sql, rows)
            conn.commit()
            logger.info(f"Inserted {len(rows)} rows from page {page}.")
            total_inserted += len(rows)

            if not last_indexes:
                update_last_run("schedule_b")
                logger.info(f"Schedule B ingester complete. Total rows inserted: {total_inserted}")
                break

            page += 1
            time.sleep(SLEEP_SECONDS)  # Respect API rate limits

    except Exception as e:
        logger.error(
            f"Schedule B ingester encountered an error\n"
            f"   - Status code: {response.status_code}\n"
            f"   - URL: {response.url}\n"
            f"   - min_load_date: {params.get('min_load_date')}\n"
            f"   - last_index: {params.get('last_index')}\n"
            f"   - last_disbursement_date: {params.get('last_disbursement_date')}\n"
            f"   - Response snippet: {response.text.strip()[:300]}"
            f"   - Error: {str(e)}"
        )
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
if __name__ == "__main__":
    run()