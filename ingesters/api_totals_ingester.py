import os
import json
import time
from datetime import datetime
import requests
from core.logger import get_logger
from core.database import db_cursor
from core.state_tracker import get_last_run, update_last_run
from core.fetcher import fetch_with_retries
from core.alerting import send_slack_alert
from core.utils import load_committee_list
from core.db_batch import execute_batch_with_retry

logger = get_logger()

FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_API_URL_TEMPLATE = "https://api.open.fec.gov/v1/committee/{committee_id}/totals/"
SLEEP_SECONDS = 3.7
CYCLE_YEAR = 2026

# List of all expected FEC totals fields
TOTALS_FIELDS = [
    "all_other_loans", "candidate_contribution", "cash_on_hand_beginning_period", "committee_designation", "committee_designation_full",
    "committee_id", "committee_name", "committee_state", "committee_type", "committee_type_full", "contribution_refunds", "contributions",
    "coverage_end_date", "coverage_start_date", "cycle", "disbursements", "filing_frequency", "filing_frequency_full", "first_f1_date",
    "first_file_date", "individual_contributions", "individual_itemized_contributions", "individual_unitemized_contributions",
    "last_beginning_image_number", "last_cash_on_hand_end_period", "last_debts_owed_by_committee", "last_debts_owed_to_committee",
    "last_report_type_full", "last_report_year", "loan_repayments", "loan_repayments_candidate_loans", "loan_repayments_other_loans",
    "loans", "loans_made_by_candidate", "net_contributions", "net_operating_expenditures", "offsets_to_operating_expenditures",
    "operating_expenditures", "organization_type", "organization_type_full", "other_disbursements", "other_political_committee_contributions",
    "other_receipts", "party_full", "political_party_committee_contributions", "receipts", "refunded_individual_contributions",
    "refunded_other_political_committee_contributions", "refunded_political_party_committee_contributions", "transaction_coverage_date",
    "transfers_from_other_authorized_committee", "transfers_to_other_authorized_committee", "treasurer_name"
]

def run(committee_id=None):
    """
    Ingest totals data for a given committee_id from the FEC API.
    """
    logger.info(f"Starting totals ingester for committee_id={committee_id}")
    fec_api_url = FEC_API_URL_TEMPLATE.format(committee_id=committee_id)
    total_inserted = 0
    page = 1
    params = {}

    try:
        last_run = get_last_run("totals", target=committee_id)

        params = {
            "api_key": FEC_API_KEY,
            "cycle": CYCLE_YEAR,
        }
        if last_run:
            last_run_date = datetime.fromisoformat(last_run).date().isoformat()

        while True:
            params["page"] = page

            logger.info(
                f"Fetching page {page} for committee_id={committee_id}"
            )

            try:
                data = fetch_with_retries(fec_api_url, params)
            except requests.exceptions.HTTPError as e:
                if getattr(e.response, "status_code", None) == 404:
                    logger.warning(f"No totals found for committee_id={committee_id} (404). Skipping.")
                    return  # Skip this committee, continue with next
                else:
                    raise  # Re-raise for other HTTP errors

            results = data.get('results', [])
            if not results:
                update_last_run("totals", target=committee_id)
                logger.info(f"Totals ingester complete for committee_id={committee_id}. Total rows inserted: {total_inserted}")
                break

            rows = []
            for result in results:
                row = []
                for field in TOTALS_FIELDS:
                    val = result.get(field)
                    # Handle lists and dicts as JSON
                    if isinstance(val, (list, dict)):
                        row.append(json.dumps(val))
                    else:
                        row.append(val)
                rows.append(tuple(row))

            insert_sql = f"""
                INSERT INTO totals (
                    {', '.join(TOTALS_FIELDS)}
                ) VALUES (
                    {', '.join(['%s'] * len(TOTALS_FIELDS))}
                )
                ON CONFLICT (committee_id, cycle) DO UPDATE SET
                    {', '.join([
                        f"{field} = EXCLUDED.{field}" for field in TOTALS_FIELDS if field not in ("committee_id", "cycle")
                    ])},
                    last_updated = NOW()
                WHERE { ' OR '.join([
                    f"totals.{field} IS DISTINCT FROM EXCLUDED.{field}" for field in TOTALS_FIELDS if field not in ("committee_id", "cycle")
                ])}
            """
            execute_batch_with_retry(db_cursor, insert_sql, rows, sleep_seconds=SLEEP_SECONDS)

            logger.info(f"Inserted {len(rows)} rows (page {page}) for committee_id={committee_id}")
            total_inserted += len(rows)
            page += 1
            time.sleep(SLEEP_SECONDS)

    except Exception as e:
        logger.error(
            f"Totals ingester encountered an error\n"
            f"   - Error: {str(e)}\n"
        )
        send_slack_alert(
            f"❌ *Totals Ingester FAILED*\n"
            f"> Error: `{str(e)}`\n"
        )
        raise

def main(args=None):
    committee_list = load_committee_list()
    if not committee_list:
        logger.warning("No committees found to ingest totals for.")
        return
    for committee_id in committee_list:
        run(committee_id=committee_id)

if __name__ == "__main__":
    main()