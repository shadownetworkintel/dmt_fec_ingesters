import requests
import psycopg2
from psycopg2.extras import execute_batch
import time
import winsound
from datetime import datetime, timedelta

FEC_API_KEY = "YOUR_FEC_API_KEY"
url = "https://api.open.fec.gov/v1/schedules/schedule_b/"

DB_CONFIG = {
    'dbname': 'political_finance_data',
    'user': 'postgres',
    'password': 'YOUR_DB_PASSWORD',
    'host': 'localhost',
    'port': 5432
}

# List of all fields as per FEC API documentation (2024-04)
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

def fetch_and_insert_schedule_b():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        DAYS_BACK = 30
        min_load_date = (datetime.today() - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
        params = {
            "api_key": FEC_API_KEY,
            "per_page": 100,
            "sort": "-disbursement_date",
            "min_load_date": min_load_date,
            "two_year_transaction_period": 2026
        }
        total_inserted = 0
        last_indexes = {}

        while True:
            # Add keyset pagination params if present
            if "last_index" in last_indexes:
                params["last_index"] = last_indexes["last_index"]
            if "last_disbursement_date" in last_indexes:
                params["last_disbursement_date"] = last_indexes["last_disbursement_date"]

            print("Requesting with params:", params)
            r = requests.get(url, params=params)
            if r.status_code != 200:
                print(f"Failed to fetch data: {r.status_code}")
                break

            data = r.json()
            results = data.get('results', [])
            pagination = data.get('pagination', {})
            last_indexes = pagination.get('last_indexes', {})

            if not results:
                print("No more data to fetch.")
                break

            rows = []
            for result in results:
                row = tuple(result.get(field) for field in ALL_FIELDS)
                rows.append(row)

            try:
                execute_batch(cur, f"""
                    INSERT INTO schedule_b_disbursements (
                        {', '.join(ALL_FIELDS)}
                    ) VALUES (
                        {', '.join(['%s'] * len(ALL_FIELDS))}
                    )
                    ON CONFLICT (sub_id) DO NOTHING;
                """, rows)
                conn.commit()
                total_inserted += len(rows)
                print(f"Inserted {len(rows)} rows. Last indexes: {last_indexes}")
            except Exception as e:
                print("Database error:", e)
                break

            if not last_indexes:
                break

            time.sleep(3.7)  # Respect API rate limits

        print(f"Total rows inserted: {total_inserted}")

    except psycopg2.Error as db_error:
        print(f"Database error: {db_error}")
    except requests.RequestException as api_error:
        print(f"API error: {api_error}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    fetch_and_insert_schedule_b()
    winsound.Beep(2000, 500)