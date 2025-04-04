# ScheduleAByStateCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**cycle** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**state_full** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_state_candidate import ScheduleAByStateCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByStateCandidate from a JSON string
schedule_aby_state_candidate_instance = ScheduleAByStateCandidate.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByStateCandidate.to_json())

# convert the object into a dict
schedule_aby_state_candidate_dict = schedule_aby_state_candidate_instance.to_dict()
# create an instance of ScheduleAByStateCandidate from a dict
schedule_aby_state_candidate_from_dict = ScheduleAByStateCandidate.from_dict(schedule_aby_state_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


