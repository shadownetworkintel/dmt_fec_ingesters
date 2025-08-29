import json
import time
from datetime import datetime
import os
from psycopg2.extras import execute_batch
from core.logger import get_logger
from core.database import db_cursor
from core.state_tracker import get_last_run, update_last_run
from core.fetcher import fetch_with_retries
from core.alerting import send_slack_alert

logger = get_logger()

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
    logger.info("Starting committees ingester")

    total_inserted = 0
    page = 1
    params = {}

    try:        
        last_run = get_last_run("committees")

        params = {
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": "committee_id"
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

            results = data.get("results", [])
            if not results:
                update_last_run("committees")
                logger.info(f"Committee ingester complete. Total rows inserted: {total_inserted}")
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
                ON CONFLICT (committee_id) DO UPDATE SET
                    {', '.join([
                        f"{field} = EXCLUDED.{field}" 
                        for field in COMMITTEE_FIELDS 
                        if field != "committee_id"
                    ])},
                    last_updated = CURRENT_TIMESTAMP
                WHERE { ' OR '.join([
                    f"committees.{field} IS DISTINCT FROM EXCLUDED.{field}"
                    for field in COMMITTEE_FIELDS if field != "committee_id"
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
            f"Committees ingester encountered an error\n"
            f"   - Error: {str(e)}\n"
            f"   - Params: {json.dumps(params, indent=2)}"
        )
        send_slack_alert(
            f"❌ *Committees Ingester FAILED*\n"
            f"> Error: `{str(e)}`\n"
            f"> Params: ```{json.dumps(params, indent=2)}```"
        )
        raise

    finally:
        pass
