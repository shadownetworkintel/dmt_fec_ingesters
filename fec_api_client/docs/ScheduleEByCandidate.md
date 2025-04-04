# ScheduleEByCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**committee_id** | **str** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**count** | **int** |  Number of records making up the total.  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
**support_oppose_indicator** | **str** | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_eby_candidate import ScheduleEByCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEByCandidate from a JSON string
schedule_eby_candidate_instance = ScheduleEByCandidate.from_json(json)
# print the JSON string representation of the object
print(ScheduleEByCandidate.to_json())

# convert the object into a dict
schedule_eby_candidate_dict = schedule_eby_candidate_instance.to_dict()
# create an instance of ScheduleEByCandidate from a dict
schedule_eby_candidate_from_dict = ScheduleEByCandidate.from_dict(schedule_eby_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


