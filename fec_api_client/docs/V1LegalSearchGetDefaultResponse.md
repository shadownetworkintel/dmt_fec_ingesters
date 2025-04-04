# V1LegalSearchGetDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_fines** | [**List[V1LegalSearchGetDefaultResponseAdminFinesInner]**](V1LegalSearchGetDefaultResponseAdminFinesInner.md) |  | [optional] 
**adrs** | [**List[V1LegalSearchGetDefaultResponseAdrsInner]**](V1LegalSearchGetDefaultResponseAdrsInner.md) |  | [optional] 
**advisory_opinions** | [**List[V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner]**](V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner.md) |  | [optional] 
**murs** | [**List[V1LegalSearchGetDefaultResponseMursInner]**](V1LegalSearchGetDefaultResponseMursInner.md) |  | [optional] 
**statutes** | [**List[V1LegalSearchGetDefaultResponseStatutesInner]**](V1LegalSearchGetDefaultResponseStatutesInner.md) |  | [optional] 
**total_admin_fines** | **int** | Total number of Admin Fines matching the search criteria | [optional] 
**total_adrs** | **int** | Total number of ADRs matching the search criteria | [optional] 
**total_advisory_opinions** | **int** | Total number of Advisory Opinions matching the search criteria | [optional] 
**total_all** | **int** | Total number of legal documents matching the search criteria | [optional] 
**total_murs** | **int** | Total number of MURs matching the search criteria | [optional] 
**total_statutes** | **int** | Total number of Statutes matching the search criteria | [optional] 

## Example

```python
from openapi_client.models.v1_legal_search_get_default_response import V1LegalSearchGetDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1LegalSearchGetDefaultResponse from a JSON string
v1_legal_search_get_default_response_instance = V1LegalSearchGetDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(V1LegalSearchGetDefaultResponse.to_json())

# convert the object into a dict
v1_legal_search_get_default_response_dict = v1_legal_search_get_default_response_instance.to_dict()
# create an instance of V1LegalSearchGetDefaultResponse from a dict
v1_legal_search_get_default_response_from_dict = V1LegalSearchGetDefaultResponse.from_dict(v1_legal_search_get_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


