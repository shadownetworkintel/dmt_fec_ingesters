# ScheduleEByCandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleEByCandidate]**](ScheduleEByCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_eby_candidate_page import ScheduleEByCandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEByCandidatePage from a JSON string
schedule_eby_candidate_page_instance = ScheduleEByCandidatePage.from_json(json)
# print the JSON string representation of the object
print(ScheduleEByCandidatePage.to_json())

# convert the object into a dict
schedule_eby_candidate_page_dict = schedule_eby_candidate_page_instance.to_dict()
# create an instance of ScheduleEByCandidatePage from a dict
schedule_eby_candidate_page_from_dict = ScheduleEByCandidatePage.from_dict(schedule_eby_candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


