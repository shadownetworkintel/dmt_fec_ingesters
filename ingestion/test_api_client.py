from openapi_client import ApiClient, Configuration, CandidateApi

config = Configuration()
config.host = "https://api.open.fec.gov/"  # Set API base URL
config.api_key['api_key'] = '23AAniIpvgK6UadWi7jJxF7hAeKVxLqSdxY9RLS1'  # If using API keys
config.api_key_prefix['api_key'] = 'Bearer'  # Set the prefix for the API key if required

api_client = ApiClient(config)
api_instance = CandidateApi(api_client)

# Example API call
candidate_id = "H0AL01055"
response = api_instance.v1_candidate_candidate_id_get(candidate_id=candidate_id, api_key=config.api_key)
print(response)