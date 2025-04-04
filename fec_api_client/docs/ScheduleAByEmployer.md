# ScheduleAByEmployer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**count** | **int** |  Number of records making up the total.  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
**employer** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_employer import ScheduleAByEmployer

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByEmployer from a JSON string
schedule_aby_employer_instance = ScheduleAByEmployer.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByEmployer.to_json())

# convert the object into a dict
schedule_aby_employer_dict = schedule_aby_employer_instance.to_dict()
# create an instance of ScheduleAByEmployer from a dict
schedule_aby_employer_from_dict = ScheduleAByEmployer.from_dict(schedule_aby_employer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


