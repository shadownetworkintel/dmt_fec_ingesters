# ingestion/fec_wrapper.py

from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient
from openapi_client.api.candidate_api import CandidateApi
from openapi_client.api.committee_api import CommitteeApi
from openapi_client.exceptions import OpenApiException

FEC_API_KEY = "23AAniIpvgK6UadWi7jJxF7hAeKVxLqSdxY9RLS1" 
HOST = "https://api.open.fec.gov/"

class FECDataFetcher:
    def __init__(self, api_key: str = FEC_API_KEY, host: str = HOST):
        configuration = Configuration(api_key=api_key, host=host)
        self.client = ApiClient(configuration)

        # Initialize FEC API endpoints
        self.candidates_api = CandidateApi(self.client)
        self.committees_api = CommitteeApi(self.client)

    def get_candidates(self):
        # Define the arguments in a dictionary
        
        try:
            return self.candidates_api.v1_candidates_get()
        except Exception as e:
            print(f"[ERROR] Failed to fetch candidates: {e}")
            return None

    def get_committee(self, committee_id: str):
        try:
            return self.committees_api.v1_committee_committee_id_get(committee_id=committee_id)
        except OpenApiException as e:
            print(f"[ERROR] Failed to fetch committee {committee_id}: {e}")
            return None


