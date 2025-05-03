import requests
import psycopg2
from psycopg2.extras import execute_batch
import time
import winsound
import json

FEC_API_KEY = "REDACTED_SECRET"
url = "https://api.open.fec.gov/v1/committees/"

DB_CONFIG = {
    'dbname': 'political_finance_data',
    'user': 'postgres',
    'password': 'REDACTED_PASSWORD',
    'host': 'localhost',
    'port': 5432
}

# All fields as of FEC API documentation (2024-04, may need to update if FEC adds new fields)
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

def fetch_and_insert_committees():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        params = {
            "api_key": FEC_API_KEY,
            "per_page": 100,
            "sort": "committee_id",
            "page": 1
        }
        total_inserted = 0

        while True:
            print("Requesting with params:", params)
            r = requests.get(url, params=params)
            if r.status_code != 200:
                print(f"Failed to fetch data: {r.status_code}")
                break

            data = r.json()
            results = data.get('results', [])

            if not results:
                print("No more data to fetch.")
                break

            rows = []
            for result in results:
                row = []
                for field in COMMITTEE_FIELDS:
                    val = result.get(field)
                    # Store lists/dicts as JSON strings for JSONB columns
                    if field in [
                        'candidate_ids', 'cycles', 'cycles_has_activity', 'cycles_has_financial', 'jfc_committee',
                        'sponsor_candidate_ids', 'sponsor_candidate_list'
                    ]:
                        row.append(json.dumps(val) if val is not None else None)
                    else:
                        row.append(val)
                rows.append(tuple(row))

            try:
                execute_batch(cur, f"""
                    INSERT INTO committees (
                        {', '.join(COMMITTEE_FIELDS)}
                    ) VALUES (
                        {', '.join(['%s'] * len(COMMITTEE_FIELDS))}
                    )
                    ON CONFLICT (committee_id) DO NOTHING;
                """, rows)
                conn.commit()
                total_inserted += len(rows)
                print(f"Inserted {len(rows)} rows. Page: {params['page']}")
            except Exception as e:
                print("Database error:", e)
                break

            params["page"] += 1  # Move to next page

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
    fetch_and_insert_committees()
    winsound.Beep(2000, 500)