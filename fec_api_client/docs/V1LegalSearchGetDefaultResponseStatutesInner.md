# V1LegalSearchGetDefaultResponseStatutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chapter** | **str** |  | [optional] 
**doc_id** | **str** |  | [optional] 
**document_highlights** | **object** |  | [optional] 
**highlights** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**no** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_legal_search_get_default_response_statutes_inner import V1LegalSearchGetDefaultResponseStatutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1LegalSearchGetDefaultResponseStatutesInner from a JSON string
v1_legal_search_get_default_response_statutes_inner_instance = V1LegalSearchGetDefaultResponseStatutesInner.from_json(json)
# print the JSON string representation of the object
print(V1LegalSearchGetDefaultResponseStatutesInner.to_json())

# convert the object into a dict
v1_legal_search_get_default_response_statutes_inner_dict = v1_legal_search_get_default_response_statutes_inner_instance.to_dict()
# create an instance of V1LegalSearchGetDefaultResponseStatutesInner from a dict
v1_legal_search_get_default_response_statutes_inner_from_dict = V1LegalSearchGetDefaultResponseStatutesInner.from_dict(v1_legal_search_get_default_response_statutes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


