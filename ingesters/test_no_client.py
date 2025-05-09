import requests
FEC_API_KEY = "" 
HOST = "https://api.open.fec.gov/"
url = "https://api.open.fec.gov/v1/schedules/schedule_a"
params = {
    "two_year_transaction_period": 2026,
    "api_key": "REDACTED_SECRET"
}

r = requests.get(url, params=params)
#print(r.status_code)
#print(r.json())

data = r.json()
results = data.get('results', [])

if results:
    print("Columns in the response:")
    print(results[0].keys())  # Print all the keys in the first record
else:
    print("No data found in the response.")



# TODO:
# 1 how to add pagination to the request?
# 2 how to save the data to the database?
