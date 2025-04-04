# CCTotalsByCandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CCTotalsByCandidate]**](CCTotalsByCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.cc_totals_by_candidate_page import CCTotalsByCandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of CCTotalsByCandidatePage from a JSON string
cc_totals_by_candidate_page_instance = CCTotalsByCandidatePage.from_json(json)
# print the JSON string representation of the object
print(CCTotalsByCandidatePage.to_json())

# convert the object into a dict
cc_totals_by_candidate_page_dict = cc_totals_by_candidate_page_instance.to_dict()
# create an instance of CCTotalsByCandidatePage from a dict
cc_totals_by_candidate_page_from_dict = CCTotalsByCandidatePage.from_dict(cc_totals_by_candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


