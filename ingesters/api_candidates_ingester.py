import os
import json
import time
import requests
from dotenv import load_dotenv

from psycopg2.extras import execute_batch
from core.logger import get_logger
from core.database import get_db_connection
from core.state_tracker import get_last_run, update_last_run

load_dotenv()
logger = get_logger("candidates_ingester")

last_run = get_last_run("candidates")
if last_run:
    params["min_first_file_date"] = last_run  # or another suitable field


FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_API_URL = "https://api.open.fec.gov/v1/candidates/"
PAGE_SIZE = 100
SLEEP_SECONDS = 3.7

# List of all expected FEC candidate fields
CANDIDATE_FIELDS = [
    "candidate_id", "name", "candidate_status", "candidate_status_full", "cycle", "district", "district_number",
    "election_years", "federal_funds_flag", "first_file_date", "incumbent_challenge", "incumbent_challenge_full",
    "last_file_date", "load_date", "office", "office_full", "office_sought", "party", "party_full", "state", "state_full",
    "active_through", "candidate_inactive", "candidate_election_years", "committee_ids", "has_raised_funds",
    "principal_campaign_committee_id", "principal_campaign_committee_name"
]

def run():
    logger.info("Starting candidate ingestion.")

    conn = None
    total_inserted = 0
    page = 1

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        while True:
            params = {
                "api_key": FEC_API_KEY,
                "per_page": PAGE_SIZE,
                "sort": "candidate_id",
                "page": page
            }
            logger.debug(f"Requesting page {page} from FEC API.")

            response = requests.get(FEC_API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            results = data.get('results', [])
            if not results:
                logger.info("No more data to fetch.")
                break

            rows = []
            for result in results:
                row = []
                for field in CANDIDATE_FIELDS:
                    val = result.get(field)
                    if isinstance(val, list):
                        row.append(json.dumps(val))
                    else:
                        row.append(val)
                rows.append(tuple(row))

            insert_sql = f"""
                INSERT INTO candidates (
                    {', '.join(CANDIDATE_FIELDS)}
                ) VALUES (
                    {', '.join(['%s'] * len(CANDIDATE_FIELDS))}
                )
                ON CONFLICT (candidate_id) DO NOTHING;
            """

            execute_batch(cur, insert_sql, rows)
            conn.commit()
            update_last_run("candidates")
            logger.info(f"Inserted {len(rows)} rows from page {page}.")
            total_inserted += len(rows)
            page += 1

            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.exception(f"Candidate ingestion failed: {e}")
    finally:
        if conn:
            conn.close()

    logger.info(f"Candidate ingestion complete. Total rows inserted: {total_inserted}")

if __name__ == "__main__":
    run()