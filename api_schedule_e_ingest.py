import requests
import psycopg2
from psycopg2.extras import execute_batch
import time
import winsound

FEC_API_KEY = "REDACTED_SECRET"
url = "https://api.open.fec.gov/v1/schedules/schedule_e/"

DB_CONFIG = {
    'dbname': 'political_finance_data',
    'user': 'postgres',
    'password': 'EMvAYOrD#BYU8y',
    'host': 'localhost',
    'port': 5432
}

def fetch_and_insert_schedule_e():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Get the latest load_date from your table
        cur.execute("""
            SELECT MAX(load_date)
            FROM schedule_e_expenditures
            WHERE load_date <= CURRENT_DATE
        """)
        latest_load_date = cur.fetchone()[0]
        params = {
            "api_key": FEC_API_KEY,
            "per_page": 100
        }
        if latest_load_date:
            params["min_load_date"] = latest_load_date.strftime("%Y-%m-%dT%H:%M:%S")

        total_inserted = 0
        last_indexes = {}

        while True:
            # Add keyset pagination params if present
            if "last_index" in last_indexes:
                params["last_index"] = last_indexes["last_index"]
            if "last_disbursement_date" in last_indexes:
                params["last_disbursement_date"] = last_indexes["last_disbursement_date"]
            if "sort_null_only" in last_indexes:
                params["sort_null_only"] = last_indexes["sort_null_only"]

            print(f"Requesting with params: {params}")
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

            # Prepare data for batch insertion (all columns)
            rows = []
            for result in results:
                rows.append((
                    result.get('action_code'),
                    result.get('action_code_full'),
                    result.get('amendment_indicator'),
                    result.get('amendment_indicator_desc'),
                    result.get('back_reference_schedule_name'),
                    result.get('back_reference_transaction_id'),
                    result.get('candidate_first_name'),
                    result.get('candidate_id'),
                    result.get('candidate_last_name'),
                    result.get('candidate_middle_name'),
                    result.get('candidate_name'),
                    result.get('candidate_office'),
                    result.get('candidate_office_district'),
                    result.get('candidate_office_full'),
                    result.get('candidate_office_state'),
                    result.get('candidate_office_state_full'),
                    result.get('candidate_party'),
                    result.get('candidate_prefix'),
                    result.get('candidate_suffix'),
                    result.get('committee'),
                    result.get('committee_id'),
                    result.get('committee_name'),
                    result.get('conduit_committee_city'),
                    result.get('conduit_committee_id'),
                    result.get('conduit_committee_name'),
                    result.get('conduit_committee_state'),
                    result.get('conduit_committee_street1'),
                    result.get('conduit_committee_street2'),
                    result.get('conduit_committee_zip'),
                    result.get('disbursement_description'),
                    result.get('disbursement_date'),
                    result.get('election_type'),
                    result.get('election_type_full'),
                    result.get('expenditure_amount'),
                    result.get('fec_election_type_desc'),
                    result.get('fec_election_year'),
                    result.get('file_number'),
                    result.get('filing_form'),
                    result.get('image_number'),
                    result.get('independent_sign_date'),
                    result.get('independent_sign_name'),
                    result.get('is_notice'),
                    result.get('line_number'),
                    result.get('line_number_label'),
                    result.get('link_id'),
                    result.get('load_date'),
                    result.get('memo_code'),
                    result.get('memo_code_full'),
                    result.get('memo_text'),
                    result.get('notary_commission_expiration_date'),
                    result.get('notary_sign_date'),
                    result.get('notary_sign_name'),
                    result.get('original_sub_id'),
                    result.get('payee_city'),
                    result.get('payee_name'),
                    result.get('payee_state'),
                    result.get('payee_street_1'),
                    result.get('payee_street_2'),
                    result.get('payee_zip'),
                    result.get('pdf_url'),
                    result.get('primary_general_indicator'),
                    result.get('primary_general_indicator_desc'),
                    result.get('recipient_committee_designation'),
                    result.get('recipient_committee_org_type'),
                    result.get('recipient_committee_type'),
                    result.get('report_type'),
                    result.get('report_year'),
                    result.get('schedule_type'),
                    result.get('schedule_type_full'),
                    result.get('semi_annual_bundled_refund'),
                    result.get('sub_id'),
                    result.get('support_oppose_indicator'),
                    result.get('transaction_id'),
                ))

            # Batch insert into the database
            execute_batch(cur, """
                INSERT INTO schedule_e_expenditures (
                    action_code, action_code_full, amendment_indicator, amendment_indicator_desc,
                    back_reference_schedule_name, back_reference_transaction_id, candidate_first_name, candidate_id,
                    candidate_last_name, candidate_middle_name, candidate_name, candidate_office, candidate_office_district,
                    candidate_office_full, candidate_office_state, candidate_office_state_full, candidate_party, candidate_prefix,
                    candidate_suffix, committee, committee_id, committee_name, conduit_committee_city, conduit_committee_id,
                    conduit_committee_name, conduit_committee_state, conduit_committee_street1, conduit_committee_street2,
                    conduit_committee_zip, disbursement_description, disbursement_date, election_type, election_type_full,
                    expenditure_amount, fec_election_type_desc, fec_election_year, file_number, filing_form, image_number,
                    independent_sign_date, independent_sign_name, is_notice, line_number, line_number_label, link_id, load_date,
                    memo_code, memo_code_full, memo_text, notary_commission_expiration_date, notary_sign_date, notary_sign_name,
                    original_sub_id, payee_city, payee_name, payee_state, payee_street_1, payee_street_2, payee_zip, pdf_url,
                    primary_general_indicator, primary_general_indicator_desc, recipient_committee_designation,
                    recipient_committee_org_type, recipient_committee_type, report_type, report_year, schedule_type,
                    schedule_type_full, semi_annual_bundled_refund, sub_id, support_oppose_indicator, transaction_id
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                ON CONFLICT (sub_id) DO NOTHING;
            """, rows)

            conn.commit()
            total_inserted += len(rows)
            print(f"Inserted {len(rows)} rows. Last indexes: {last_indexes}")

            # Stop if no last_indexes (no more pages)
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
    fetch_and_insert_schedule_e()
    # Play a beep sound (frequency, duration in ms)
    winsound.Beep(1000, 700)