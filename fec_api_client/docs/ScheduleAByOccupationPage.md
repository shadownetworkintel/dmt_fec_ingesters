# ScheduleAByOccupationPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleAByOccupation]**](ScheduleAByOccupation.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_occupation_page import ScheduleAByOccupationPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByOccupationPage from a JSON string
schedule_aby_occupation_page_instance = ScheduleAByOccupationPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByOccupationPage.to_json())

# convert the object into a dict
schedule_aby_occupation_page_dict = schedule_aby_occupation_page_instance.to_dict()
# create an instance of ScheduleAByOccupationPage from a dict
schedule_aby_occupation_page_from_dict = ScheduleAByOccupationPage.from_dict(schedule_aby_occupation_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


