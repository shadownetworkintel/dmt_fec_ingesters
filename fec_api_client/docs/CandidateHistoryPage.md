# CandidateHistoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CandidateHistory]**](CandidateHistory.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_history_page import CandidateHistoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateHistoryPage from a JSON string
candidate_history_page_instance = CandidateHistoryPage.from_json(json)
# print the JSON string representation of the object
print(CandidateHistoryPage.to_json())

# convert the object into a dict
candidate_history_page_dict = candidate_history_page_instance.to_dict()
# create an instance of CandidateHistoryPage from a dict
candidate_history_page_from_dict = CandidateHistoryPage.from_dict(candidate_history_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


