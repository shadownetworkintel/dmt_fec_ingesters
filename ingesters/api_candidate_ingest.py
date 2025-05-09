import requests
import psycopg2
from psycopg2.extras import execute_batch
import time
import winsound
import json

FEC_API_KEY = "REDACTED_SECRET"
url = "https://api.open.fec.gov/v1/candidates/"

DB_CONFIG = {
    'dbname': 'political_finance_data',
    'user': 'postgres',
    'password': 'EMvAYOrD#BYU8y',
    'host': 'localhost',
    'port': 5432
}

# List of all fields as of FEC API documentation (2024-04, update if FEC adds new fields)
CANDIDATE_FIELDS = [
    "candidate_id", "name", "candidate_status", "candidate_status_full", "cycle", "district", "district_number",
    "election_years", "federal_funds_flag", "first_file_date", "incumbent_challenge", "incumbent_challenge_full",
    "last_file_date", "load_date", "office", "office_full", "office_sought", "party", "party_full", "state", "state_full",
    "active_through", "candidate_inactive", "candidate_election_years", "committee_ids", "has_raised_funds",
    "principal_campaign_committee_id", "principal_campaign_committee_name"
]

def fetch_and_insert_candidates():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        params = {
            "api_key": FEC_API_KEY,
            "per_page": 100,
            "sort": "candidate_id",
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
                for field in CANDIDATE_FIELDS:
                    val = result.get(field)
                    # Store lists as JSON strings for JSONB columns
                    if field in ['election_years', 'candidate_election_years', 'committee_ids']:
                        row.append(json.dumps(val) if val is not None else None)
                    else:
                        row.append(val)
                rows.append(tuple(row))

            try:
                execute_batch(cur, f"""
                    INSERT INTO candidates (
                        {', '.join(CANDIDATE_FIELDS)}
                    ) VALUES (
                        {', '.join(['%s'] * len(CANDIDATE_FIELDS))}
                    )
                    ON CONFLICT (candidate_id) DO NOTHING;
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
    fetch_and_insert_candidates()
    winsound.Beep(2000, 500)