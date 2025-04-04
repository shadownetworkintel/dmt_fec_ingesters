# ScheduleAEfilePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleAEfile]**](ScheduleAEfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_a_efile_page import ScheduleAEfilePage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAEfilePage from a JSON string
schedule_a_efile_page_instance = ScheduleAEfilePage.from_json(json)
# print the JSON string representation of the object
print(ScheduleAEfilePage.to_json())

# convert the object into a dict
schedule_a_efile_page_dict = schedule_a_efile_page_instance.to_dict()
# create an instance of ScheduleAEfilePage from a dict
schedule_a_efile_page_from_dict = ScheduleAEfilePage.from_dict(schedule_a_efile_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


