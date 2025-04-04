# ScheduleAByStatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleAByState]**](ScheduleAByState.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_state_page import ScheduleAByStatePage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByStatePage from a JSON string
schedule_aby_state_page_instance = ScheduleAByStatePage.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByStatePage.to_json())

# convert the object into a dict
schedule_aby_state_page_dict = schedule_aby_state_page_instance.to_dict()
# create an instance of ScheduleAByStatePage from a dict
schedule_aby_state_page_from_dict = ScheduleAByStatePage.from_dict(schedule_aby_state_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


