# ScheduleABySizePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleABySize]**](ScheduleABySize.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_size_page import ScheduleABySizePage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleABySizePage from a JSON string
schedule_aby_size_page_instance = ScheduleABySizePage.from_json(json)
# print the JSON string representation of the object
print(ScheduleABySizePage.to_json())

# convert the object into a dict
schedule_aby_size_page_dict = schedule_aby_size_page_instance.to_dict()
# create an instance of ScheduleABySizePage from a dict
schedule_aby_size_page_from_dict = ScheduleABySizePage.from_dict(schedule_aby_size_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


