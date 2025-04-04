# ScheduleAByOccupation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**count** | **int** |  Number of records making up the total.  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
**occupation** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_occupation import ScheduleAByOccupation

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByOccupation from a JSON string
schedule_aby_occupation_instance = ScheduleAByOccupation.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByOccupation.to_json())

# convert the object into a dict
schedule_aby_occupation_dict = schedule_aby_occupation_instance.to_dict()
# create an instance of ScheduleAByOccupation from a dict
schedule_aby_occupation_from_dict = ScheduleAByOccupation.from_dict(schedule_aby_occupation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


