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
from core.utils import load_candidate_list  # NEW

logger = get_logger()

FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_API_LIST_URL = "https://api.open.fec.gov/v1/candidates/"
FEC_API_DETAIL_URL = "https://api.open.fec.gov/v1/candidate/{candidate_id}/"
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

INSERT_SQL = f"""
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
        f"candidates.{field} IS DISTINCT FROM EXCLUDED.{field}"
        for field in CANDIDATE_FIELDS if field != "candidate_id"
    ])}
"""


def _build_rows_from_results(results):
    rows = []
    for result in results:
        row = []
        for field in CANDIDATE_FIELDS:
            val = result.get(field)
            # JSONB-ish list fields come back as lists
            row.append(json.dumps(val) if isinstance(val, list) else val)
        rows.append(tuple(row))
    return rows


def _upsert_candidates(rows):
    if not rows:
        return 0
    with db_cursor() as cur:
        execute_batch(cur, INSERT_SQL, rows)
    return len(rows)


def _run_all_candidates():
    logger.info("Starting candidates ingester (ALL candidates)")

    total_inserted = 0
    page = 1
    params = {}

    try:
        last_run = get_last_run("candidates")

        params = {
            "api_key": FEC_API_KEY,
            "per_page": PAGE_SIZE,
            "sort": "candidate_id",
        }
        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date().isoformat()
            params["min_first_file_date"] = last_run_date

        while True:
            params["page"] = page

            logger.info(
                f"Fetching page {page} - min_first_file_date: {params.get('min_first_file_date')}"
            )

            data = fetch_with_retries(FEC_API_LIST_URL, params)
            results = data.get("results", [])
            if not results:
                update_last_run("candidates")
                logger.info(
                    f"Candidates ingester complete. Total rows inserted: {total_inserted}"
                )
                break

            rows = _build_rows_from_results(results)
            inserted = _upsert_candidates(rows)

            logger.info(f"Inserted {inserted} rows (page {page})")
            total_inserted += inserted
            page += 1
            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.error(
            f"Candidates ingester (ALL) encountered an error\n"
            f"   - Error: {str(e)}\n"
        )
        send_slack_alert(
            f"❌ *Candidates Ingester (ALL) FAILED*\n"
            f"> Error: `{str(e)}`\n"
        )
        raise


def _run_for_candidate(candidate_id: str):
    """
    Fetch and upsert a single candidate by ID using the detail endpoint:
        /v1/candidate/{candidate_id}/
    """
    logger.info(f"Fetching candidate details for {candidate_id}")
    params = {"api_key": FEC_API_KEY}
    url = FEC_API_DETAIL_URL.format(candidate_id=candidate_id)

    try:
        data = fetch_with_retries(url, params)
        results = data.get("results", [])

        if not results:
            logger.warning(f"No candidate data returned for {candidate_id}; skipping.")
            return 0

        rows = _build_rows_from_results(results)
        inserted = _upsert_candidates(rows)
        logger.info(f"Upserted {inserted} row(s) for candidate {candidate_id}")
        return inserted

    except Exception as e:
        logger.error(
            f"Candidates ingester encountered an error for candidate {candidate_id}\n"
            f"   - Error: {str(e)}\n"
            f"   - URL: {url}\n"
        )
        send_slack_alert(
            f"❌ *Candidates Ingester FAILED for candidate {candidate_id}*\n"
            f"> Error: `{str(e)}`\n"
            f"> URL: `{url}`\n"
        )
        raise


def main():
    """
    Entry point.

    - If candidate_list is empty/missing: run full paginated ingestion.
    - If candidate_list has IDs: only ingest those candidates via /candidate/{id}/.
    """
    candidate_list = load_candidate_list()

    if not candidate_list:
        _run_all_candidates()
        return

    logger.info(
        f"Starting candidates ingester for {len(candidate_list)} candidate(s) "
        f"from candidate_list"
    )

    total_inserted = 0
    for candidate_id in candidate_list:
        inserted = _run_for_candidate(candidate_id)
        total_inserted += inserted
        time.sleep(SLEEP_SECONDS)

    logger.info(
        f"Candidates ingester (filtered) complete. Total rows upserted: {total_inserted}"
    )