# CommitteeHistoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeHistory]**](CommitteeHistory.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_history_page import CommitteeHistoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeHistoryPage from a JSON string
committee_history_page_instance = CommitteeHistoryPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeHistoryPage.to_json())

# convert the object into a dict
committee_history_page_dict = committee_history_page_instance.to_dict()
# create an instance of CommitteeHistoryPage from a dict
committee_history_page_from_dict = CommitteeHistoryPage.from_dict(committee_history_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


