import openapi_client
import os
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.open.fec.gov/"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration.api_key['ApiKeyHeaderAuth'] = "23AAniIpvgK6UadWi7jJxF7hAeKVxLqSdxY9RLS1" #os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeaderAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration.api_key['ApiKeyQueryAuth'] = "23AAniIpvgK6UadWi7jJxF7hAeKVxLqSdxY9RLS1" #os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQueryAuth'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = "23AAniIpvgK6UadWi7jJxF7hAeKVxLqSdxY9RLS1" #os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuditApi(api_client)

    # Define the arguments in a dictionary
    api_args = {
        # 'page': 1,
        # 'per_page': 20,
         'q': ['%Senate%'],
        # 'qq': ['qq_example'],
        # 'primary_category_id': 'all',
        # 'sub_category_id': 'all',
        # 'audit_case_id': ['audit_case_id_example'],
        # 'cycle': [56],
        # 'committee_id': ['committee_id_example'],
        # 'committee_type': ['committee_type_example'],
        # 'committee_designation': 'committee_designation_example',
        # 'audit_id': [56],
        # 'candidate_id': ['H0IA04145'], 
         'min_election_cycle': 20,
         'max_election_cycle': 2026,
        # 'sort': ['sort_example'],
        # 'sort_hide_null': False,
        # 'sort_null_only': False,
        # 'sort_nulls_last': False,
        'api_key': '23AAniIpvgK6UadWi7jJxF7hAeKVxLqSdxY9RLS1'}
    
    try:
        # Pass the dictionary as keyword arguments using **api_args
        api_response = api_instance.v1_audit_case_get(**api_args)
        print("The response of AuditApi->v1_audit_case_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuditApi->v1_audit_case_get: %s\n" % e)

