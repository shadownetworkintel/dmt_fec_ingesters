import requests
FEC_API_KEY = "" 
HOST = "https://api.open.fec.gov/"
url = "https://api.open.fec.gov/v1/candidates"
params = {
    "office": "P",
    "election_year": 2020,
    "api_key": "23AAniIpvgK6UadWi7jJxF7hAeKVxLqSdxY9RLS1"
}

r = requests.get(url, params=params)
print(r.status_code)
print(r.json())


# TODO:
# 1 how to add pagination to the request?
# 2 how to save the data to the database?
