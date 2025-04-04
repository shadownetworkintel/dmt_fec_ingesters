# V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**citations** | [**List[V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInnerCitationsInner]**](V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInnerCitationsInner.md) |  | [optional] 
**disposition** | **str** |  | [optional] 
**penalty** | **float** |  | [optional] 
**respondent** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_legal_search_get_default_response_adrs_inner_dispositions_inner import V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner from a JSON string
v1_legal_search_get_default_response_adrs_inner_dispositions_inner_instance = V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.from_json(json)
# print the JSON string representation of the object
print(V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.to_json())

# convert the object into a dict
v1_legal_search_get_default_response_adrs_inner_dispositions_inner_dict = v1_legal_search_get_default_response_adrs_inner_dispositions_inner_instance.to_dict()
# create an instance of V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner from a dict
v1_legal_search_get_default_response_adrs_inner_dispositions_inner_from_dict = V1LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.from_dict(v1_legal_search_get_default_response_adrs_inner_dispositions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


