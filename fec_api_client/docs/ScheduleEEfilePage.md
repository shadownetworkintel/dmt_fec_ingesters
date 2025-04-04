# ScheduleEEfilePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleEEfile]**](ScheduleEEfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_e_efile_page import ScheduleEEfilePage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEEfilePage from a JSON string
schedule_e_efile_page_instance = ScheduleEEfilePage.from_json(json)
# print the JSON string representation of the object
print(ScheduleEEfilePage.to_json())

# convert the object into a dict
schedule_e_efile_page_dict = schedule_e_efile_page_instance.to_dict()
# create an instance of ScheduleEEfilePage from a dict
schedule_e_efile_page_from_dict = ScheduleEEfilePage.from_dict(schedule_e_efile_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


