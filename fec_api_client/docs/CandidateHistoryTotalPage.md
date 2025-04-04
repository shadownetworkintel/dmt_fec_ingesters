# CandidateHistoryTotalPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CandidateHistoryTotal]**](CandidateHistoryTotal.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_history_total_page import CandidateHistoryTotalPage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateHistoryTotalPage from a JSON string
candidate_history_total_page_instance = CandidateHistoryTotalPage.from_json(json)
# print the JSON string representation of the object
print(CandidateHistoryTotalPage.to_json())

# convert the object into a dict
candidate_history_total_page_dict = candidate_history_total_page_instance.to_dict()
# create an instance of CandidateHistoryTotalPage from a dict
candidate_history_total_page_from_dict = CandidateHistoryTotalPage.from_dict(candidate_history_total_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


