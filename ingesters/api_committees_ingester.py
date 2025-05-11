import requests
import json
import time
from datetime import datetime
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_batch
from core.logger import get_logger
from core.database import get_db_connection
from core.state_tracker import get_last_run, update_last_run

load_dotenv()
logger = get_logger("api_committees_ingester")

FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_API_URL = "https://api.open.fec.gov/v1/committees/"
PAGE_SIZE = 100
SLEEP_SECONDS = 3.7

COMMITTEE_FIELDS = [
    "committee_id", "name", "designation", "designation_full", "committee_type", "committee_type_full",
    "organization_type", "organization_type_full", "party", "party_full", "state", "state_full",
    "treasurer_name", "street_1", "street_2", "city", "zip", "candidate_ids", "cycles",
    "cycles_has_activity", "cycles_has_financial", "first_f1_date", "first_file_date", "last_f1_date",
    "last_file_date", "filing_frequency", "is_active", "jfc_committee", "last_cycle_has_activity",
    "last_cycle_has_financial", "cycle", "party_type", "party_type_full", "sponsor_candidate_ids",
    "sponsor_candidate_list", "sponsor_candidate_name", "sponsor_candidate_office", "sponsor_candidate_office_district",
    "sponsor_candidate_office_state", "sponsor_candidate_party", "sponsor_candidate_party_full",
    "sponsor_candidate_state", "sponsor_candidate_state_full", "sponsor_candidate_type", "sponsor_candidate_type_full",
    "sponsor_candidate_zip", "sponsor_committee_id", "sponsor_committee_name", "sponsor_committee_type",
    "sponsor_committee_type_full", "sponsor_committee_zip", "sponsor_name", "sponsor_state", "sponsor_state_full",
    "sponsor_type", "sponsor_type_full", "sponsor_zip", "terminated"
]

def run():
    logger.info("Starting committees ingestion.")

    conn = None
    total_inserted = 0
    page = 1

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        last_run = get_last_run("committees")

        while True:
            params = {
                "api_key": FEC_API_KEY,
                "per_page": PAGE_SIZE,
                "sort": "committee_id",
                "page": page
            }
            if last_run:
                last_run_date = datetime.fromisoformat(last_run).date().isoformat()
                params["min_first_file_date"] = last_run

            logger.debug(f"Requesting page {page} from FEC API.")
            
            response = requests.get(FEC_API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            results = data.get("results", [])
            if not results:
                logger.info("No more data to fetch.")
                break

            rows = []
            for result in results:
                row = []
                for field in COMMITTEE_FIELDS:
                    val = result.get(field)
                    if field in [
                        'candidate_ids', 'cycles', 'cycles_has_activity', 'cycles_has_financial', 'jfc_committee',
                        'sponsor_candidate_ids', 'sponsor_candidate_list'
                    ]:
                        row.append(json.dumps(val) if val is not None else None)
                    else:
                        row.append(val)
                rows.append(tuple(row))

            insert_sql = f"""
                INSERT INTO committees (
                    {', '.join(COMMITTEE_FIELDS)}
                ) VALUES (
                    {', '.join(['%s'] * len(COMMITTEE_FIELDS))}
                )
                ON CONFLICT (committee_id) DO NOTHING;
            """
            execute_batch(cur, insert_sql, rows)
            conn.commit()
            logger.info(f"Inserted {len(rows)} rows (page {params['page']})")
            total_inserted += len(rows)
            page += 1

            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.exception(f"Committee ingestion failed: {e}")
    finally:
        if conn:
            conn.close()

    update_last_run("committees")
    logger.info(f"Committee ingestion complete. Total rows inserted: {total_inserted}")

if __name__ == "__main__":
    run()