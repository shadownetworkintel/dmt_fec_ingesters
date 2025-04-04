# V1LegalSearchGetDefaultResponseAdminFinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_outcome** | **str** |  | [optional] 
**challenge_receipt_date** | **date** |  | [optional] 
**check_amount** | **float** |  | [optional] 
**commission_votes** | [**List[V1LegalSearchGetDefaultResponseAdminFinesInnerCommissionVotesInner]**](V1LegalSearchGetDefaultResponseAdminFinesInnerCommissionVotesInner.md) |  | [optional] 
**committee_id** | **str** |  | [optional] 
**doc_id** | **str** |  | [optional] 
**document_highlights** | **object** |  | [optional] 
**documents** | [**List[V1LegalSearchGetDefaultResponseAdminFinesInnerDocumentsInner]**](V1LegalSearchGetDefaultResponseAdminFinesInnerDocumentsInner.md) |  | [optional] 
**final_determination_amount** | **float** |  | [optional] 
**final_determination_date** | **date** |  | [optional] 
**highlights** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**no** | **str** |  | [optional] 
**petition_court_decision_date** | **date** |  | [optional] 
**petition_court_filing_date** | **date** |  | [optional] 
**reason_to_believe_action_date** | **date** |  | [optional] 
**reason_to_believe_fine_amount** | **float** |  | [optional] 
**report_type** | **str** |  | [optional] 
**report_year** | **str** |  | [optional] 
**treasury_referral_amount** | **float** |  | [optional] 
**treasury_referral_date** | **date** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_legal_search_get_default_response_admin_fines_inner import V1LegalSearchGetDefaultResponseAdminFinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1LegalSearchGetDefaultResponseAdminFinesInner from a JSON string
v1_legal_search_get_default_response_admin_fines_inner_instance = V1LegalSearchGetDefaultResponseAdminFinesInner.from_json(json)
# print the JSON string representation of the object
print(V1LegalSearchGetDefaultResponseAdminFinesInner.to_json())

# convert the object into a dict
v1_legal_search_get_default_response_admin_fines_inner_dict = v1_legal_search_get_default_response_admin_fines_inner_instance.to_dict()
# create an instance of V1LegalSearchGetDefaultResponseAdminFinesInner from a dict
v1_legal_search_get_default_response_admin_fines_inner_from_dict = V1LegalSearchGetDefaultResponseAdminFinesInner.from_dict(v1_legal_search_get_default_response_admin_fines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


