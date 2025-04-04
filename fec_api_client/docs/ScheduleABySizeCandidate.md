# ScheduleABySizeCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**cycle** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_size_candidate import ScheduleABySizeCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleABySizeCandidate from a JSON string
schedule_aby_size_candidate_instance = ScheduleABySizeCandidate.from_json(json)
# print the JSON string representation of the object
print(ScheduleABySizeCandidate.to_json())

# convert the object into a dict
schedule_aby_size_candidate_dict = schedule_aby_size_candidate_instance.to_dict()
# create an instance of ScheduleABySizeCandidate from a dict
schedule_aby_size_candidate_from_dict = ScheduleABySizeCandidate.from_dict(schedule_aby_size_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


