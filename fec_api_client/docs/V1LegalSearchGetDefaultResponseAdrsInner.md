# V1LegalSearchGetDefaultResponseAdrsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_date** | **date** |  | [optional] 
**commission_votes** | [**List[V1LegalSearchGetDefaultResponseAdminFinesInnerCommissionVotesInner]**](V1LegalSearchGetDefaultResponseAdminFinesInnerCommissionVotesInner.md) |  | [optional] 
**dispositions** | [**List[V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner]**](V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.md) |  | [optional] 
**doc_id** | **str** |  | [optional] 
**document_highlights** | **object** |  | [optional] 
**documents** | [**List[V1LegalSearchGetDefaultResponseAdminFinesInnerDocumentsInner]**](V1LegalSearchGetDefaultResponseAdminFinesInnerDocumentsInner.md) |  | [optional] 
**election_cycles** | **int** |  | [optional] 
**highlights** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**no** | **str** |  | [optional] 
**open_date** | **date** |  | [optional] 
**participants** | [**List[V1LegalSearchGetDefaultResponseAdrsInnerParticipantsInner]**](V1LegalSearchGetDefaultResponseAdrsInnerParticipantsInner.md) |  | [optional] 
**respondents** | **List[str]** |  | [optional] 
**subjects** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_legal_search_get_default_response_adrs_inner import V1LegalSearchGetDefaultResponseAdrsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1LegalSearchGetDefaultResponseAdrsInner from a JSON string
v1_legal_search_get_default_response_adrs_inner_instance = V1LegalSearchGetDefaultResponseAdrsInner.from_json(json)
# print the JSON string representation of the object
print(V1LegalSearchGetDefaultResponseAdrsInner.to_json())

# convert the object into a dict
v1_legal_search_get_default_response_adrs_inner_dict = v1_legal_search_get_default_response_adrs_inner_instance.to_dict()
# create an instance of V1LegalSearchGetDefaultResponseAdrsInner from a dict
v1_legal_search_get_default_response_adrs_inner_from_dict = V1LegalSearchGetDefaultResponseAdrsInner.from_dict(v1_legal_search_get_default_response_adrs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


