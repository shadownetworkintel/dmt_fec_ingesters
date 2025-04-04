# IETotalsByCandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[IETotalsByCandidate]**](IETotalsByCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.ie_totals_by_candidate_page import IETotalsByCandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of IETotalsByCandidatePage from a JSON string
ie_totals_by_candidate_page_instance = IETotalsByCandidatePage.from_json(json)
# print the JSON string representation of the object
print(IETotalsByCandidatePage.to_json())

# convert the object into a dict
ie_totals_by_candidate_page_dict = ie_totals_by_candidate_page_instance.to_dict()
# create an instance of IETotalsByCandidatePage from a dict
ie_totals_by_candidate_page_from_dict = IETotalsByCandidatePage.from_dict(ie_totals_by_candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


