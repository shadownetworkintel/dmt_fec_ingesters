import requests
import psycopg2
from psycopg2.extras import execute_batch
import time
import winsound
import json
from datetime import datetime, timedelta

FEC_API_KEY = "REDACTED_SECRET"
url = "https://api.open.fec.gov/v1/schedules/schedule_e/"

DB_CONFIG = {
    'dbname': 'political_finance_data',
    'user': 'postgres',
    'password': 'REDACTED_PASSWORD',
    'host': 'localhost',
    'port': 5432
}

def fetch_and_insert_schedule_e():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Always fetch the last N days (e.g., 180 for first run, 30 for daily)
        DAYS_BACK = 30
        min_filing_date = (datetime.today() - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
        params = {
            "api_key": FEC_API_KEY,
            "per_page": 100,
            "min_filing_date": min_filing_date,
            "sort": "expenditure_date"  # ascending order
        }
        total_inserted = 0
        last_indexes = {}

        # Committee keys in the order you want to insert
        committee_keys = [
            'affiliated_committee_name',
            'candidate_ids',
            'city',
            'committee_id',
            'committee_type',
            'committee_type_full',
            'cycle',
            'cycles',
            'cycles_has_activity',
            'cycles_has_financial',
            'designation',
            'designation_full',
            'filing_frequency',
            'first_f1_date',
            'first_file_date',
            'is_active',
            'jfc_committee',
            'last_cycle_has_activity',
            'last_cycle_has_financial',
            'last_f1_date',
            'last_file_date',
            'name',
            'organization_type',
            'organization_type_full',
            'party',
            'party_full',
            'state',
            'state_full',
            'street_1',
            'street_2',
            'treasurer_name',
            'zip'
        ]

        while True:
            # Remove old keyset params
            params.pop("last_index", None)
            params.pop("last_expenditure_date", None)

            # Add keyset params if present
            if "last_index" in last_indexes:
                params["last_index"] = last_indexes["last_index"]
            if "last_expenditure_date" in last_indexes:
                params["last_expenditure_date"] = last_indexes["last_expenditure_date"]

            #print(f"Requesting with params: {params}")
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

            # Prepare data for batch insertion (all columns, committee fields flattened)
            rows = []
            for result in results:
                committee = result.get('committee') or {}
                committee_values = []
                for key in committee_keys:
                    val = committee.get(key)
                    if key in ['candidate_ids', 'cycles', 'cycles_has_activity', 'cycles_has_financial', 'jfc_committee']:
                        committee_values.append(json.dumps(val) if val is not None else None)
                    else:
                        committee_values.append(val)

                # Extract candidate_id from candidate field if it's a dict, else use as is
                candidate_field = result.get('candidate')
                if isinstance(candidate_field, dict):
                    candidate_val = candidate_field.get('candidate_id')
                else:
                    candidate_val = candidate_field

                row_tuple = (
                    result.get('action_code'),
                    result.get('action_code_full'),
                    result.get('amendment_indicator'),
                    result.get('amendment_number'),
                    result.get('amendment_indicator_desc'),
                    result.get('back_reference_schedule_name'),
                    result.get('back_reference_transaction_id'),
                    candidate_val,  # Only candidate_id here
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
                    *committee_values,
                    result.get('committee_id'),
                    result.get('committee_name'),
                    result.get('conduit_committee_city'),
                    result.get('conduit_committee_id'),
                    result.get('conduit_committee_name'),
                    result.get('conduit_committee_state'),
                    result.get('conduit_committee_street1'),
                    result.get('conduit_committee_street2'),
                    result.get('conduit_committee_zip'),
                    result.get('disbursement_dt'),
                    result.get('dissemination_date'),
                    result.get('election_type'),
                    result.get('election_type_full'),
                    result.get('expenditure_amount'),
                    result.get('expenditure_date'),
                    result.get('expenditure_description'),
                    result.get('file_number'),
                    result.get('filer_first_name'),
                    result.get('filer_last_name'),
                    result.get('filer_middle_name'),
                    result.get('filer_prefix'),
                    result.get('filer_suffix'),
                    result.get('filing_date'),
                    result.get('filing_form'),
                    result.get('form_line_number'),
                    result.get('image_number'),
                    result.get('independent_sign_date'),
                    result.get('independent_sign_name'),
                    result.get('is_notice'),
                    result.get('line_number'),
                    result.get('line_number_label'),
                    result.get('link_id'),
                    result.get('memo_code'),
                    result.get('memo_code_full'),
                    result.get('memo_text'),
                    result.get('memoed_subtotal'),
                    result.get('most_recent'),
                    result.get('notary_commission_expiration_date'),
                    result.get('notary_sign_date'),
                    result.get('notary_sign_name'),
                    result.get('office_total_ytd'),
                    result.get('original_sub_id'),
                    result.get('payee_city'),
                    result.get('payee_first_name'),
                    result.get('payee_last_name'),
                    result.get('payee_middle_name'),
                    result.get('payee_name'),
                    result.get('payee_prefix'),
                    result.get('payee_state'),
                    result.get('payee_street_1'),
                    result.get('payee_street_2'),
                    result.get('payee_suffix'),
                    result.get('payee_zip'),
                    result.get('pdf_url'),
                    result.get('previous_file_number'),
                    result.get('report_type'),
                    result.get('report_year'),
                    result.get('schedule_type'),
                    result.get('schedule_type_full'),
                    result.get('semi_annual_bundled_refund'),
                    result.get('sub_id'),
                    result.get('support_oppose_indicator'),
                    result.get('transaction_id')
                )

                # for idx, value in enumerate(row_tuple):
                #     if isinstance(value, (dict, list)):
                #         print(f"Index {idx} value is {type(value)}: {value}")
                rows.append(row_tuple)

            # Batch insert into the database
            execute_batch(cur, """
                INSERT INTO schedule_e_expenditures (
                    action_code, action_code_full, amendment_indicator, amendment_number, amendment_indicator_desc,
                    back_reference_schedule_name, back_reference_transaction_id, candidate, candidate_first_name, candidate_id,
                    candidate_last_name, candidate_middle_name, candidate_name, candidate_office, candidate_office_district,
                    candidate_office_full, candidate_office_state, candidate_office_state_full, candidate_party, candidate_prefix,
                    candidate_suffix,
                    affiliated_committee_name, candidate_ids, committee_city, committee_committee_id, committee_type,
                    committee_type_full, committee_cycle, committee_cycles, committee_cycles_has_activity, committee_cycles_has_financial,
                    committee_designation, committee_designation_full, committee_filing_frequency, committee_first_f1_date,
                    committee_first_file_date, committee_is_active, committee_jfc_committee, committee_last_cycle_has_activity, committee_last_cycle_has_financial,
                    committee_last_f1_date, committee_last_file_date, committee_name, committee_organization_type, committee_organization_type_full,
                    committee_party, committee_party_full, committee_state, committee_state_full, committee_street_1, committee_street_2,
                    committee_treasurer_name, committee_zip,
                    committee_id, committee_name2, conduit_committee_city, conduit_committee_id, conduit_committee_name, conduit_committee_state,
                    conduit_committee_street1, conduit_committee_street2, conduit_committee_zip, disbursement_dt, dissemination_date,
                    election_type, election_type_full, expenditure_amount, expenditure_date, expenditure_description, file_number,
                    filer_first_name, filer_last_name, filer_middle_name, filer_prefix, filer_suffix, filing_date, filing_form,
                    form_line_number, image_number, independent_sign_date, independent_sign_name, is_notice, line_number, line_number_label, link_id,
                    memo_code, memo_code_full, memo_text, memoed_subtotal, most_recent, notary_commission_expiration_date,
                    notary_sign_date, notary_sign_name, office_total_ytd, original_sub_id, payee_city, payee_first_name,
                    payee_last_name, payee_middle_name, payee_name, payee_prefix, payee_state, payee_street_1, payee_street_2,
                    payee_suffix, payee_zip, pdf_url, previous_file_number, report_type, report_year, schedule_type,
                    schedule_type_full, semi_annual_bundled_refund, sub_id, support_oppose_indicator, transaction_id
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
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
    winsound.Beep(2000, 500)