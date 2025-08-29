import os
import json
import time
from datetime import datetime
from psycopg2.extras import execute_batch
from core.logger import get_logger
from core.database import db_cursor
from core.state_tracker import get_last_run, update_last_run
from core.fetcher import fetch_with_retries
from core.alerting import send_slack_alert

logger = get_logger()

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
    logger.info("Starting candidates ingester")

    total_inserted = 0
    page = 1
    params = {}

    try:
        last_run = get_last_run("candidates")

        params = {
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": "candidate_id"
        }
        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date().isoformat()
            params["min_first_file_date"] = last_run_date

        while True:
            params["page"] = page

            logger.info(
                f"Fetching page {page} - min_first_file_date: {params.get('min_first_file_date')}"
            )

            data = fetch_with_retries(FEC_API_URL, params)

            results = data.get('results', [])
            if not results:
                update_last_run("candidates")
                logger.info(f"Candidates ingester complete. Total rows inserted: {total_inserted}")
                break

            rows = []
            for result in results:
                row = []
                for field in CANDIDATE_FIELDS:
                    val = result.get(field)
                    row.append(json.dumps(val) if isinstance(val, list) else val)
                rows.append(tuple(row))

            insert_sql = f"""
                INSERT INTO candidates (
                    {', '.join(CANDIDATE_FIELDS)}
                ) VALUES (
                    {', '.join(['%s'] * len(CANDIDATE_FIELDS))}
                )
                ON CONFLICT (candidate_id) DO UPDATE SET
                    {', '.join([
                        f"{field} = EXCLUDED.{field}" for field in CANDIDATE_FIELDS if field != "candidate_id"
                    ])},
                    last_updated = NOW()
                WHERE { ' OR '.join([
                    f"candidates.{field} IS DISTINCT FROM EXCLUDED.{field}" for field in CANDIDATE_FIELDS if field != "candidate_id"
                ])}
            """
            with db_cursor() as cur:
                execute_batch(cur, insert_sql, rows)

            logger.info(f"Inserted {len(rows)} rows (page {page})")
            total_inserted += len(rows)
            page += 1
            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.error(
            f"Candidates ingester encountered an error\n"
            f"   - Error: {str(e)}\n"
            f"   - Params: {json.dumps(params, indent=2)}"
        )
        send_slack_alert(
            f"❌ *Candidates Ingester FAILED*\n"
            f"> Error: `{str(e)}`\n"
            f"> Params: ```{json.dumps(params, indent=2)}```"
        )
        raise

    finally:
        pass
