# ScheduleAByState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**count** | **int** |  Number of records making up the total.  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
**state** | **str** | US state or territory | 
**state_full** | **str** | US state or territory | 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_state import ScheduleAByState

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByState from a JSON string
schedule_aby_state_instance = ScheduleAByState.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByState.to_json())

# convert the object into a dict
schedule_aby_state_dict = schedule_aby_state_instance.to_dict()
# create an instance of ScheduleAByState from a dict
schedule_aby_state_from_dict = ScheduleAByState.from_dict(schedule_aby_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


