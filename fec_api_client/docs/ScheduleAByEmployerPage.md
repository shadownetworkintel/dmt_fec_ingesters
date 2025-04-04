# ScheduleAByEmployerPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleAByEmployer]**](ScheduleAByEmployer.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_employer_page import ScheduleAByEmployerPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByEmployerPage from a JSON string
schedule_aby_employer_page_instance = ScheduleAByEmployerPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByEmployerPage.to_json())

# convert the object into a dict
schedule_aby_employer_page_dict = schedule_aby_employer_page_instance.to_dict()
# create an instance of ScheduleAByEmployerPage from a dict
schedule_aby_employer_page_from_dict = ScheduleAByEmployerPage.from_dict(schedule_aby_employer_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


