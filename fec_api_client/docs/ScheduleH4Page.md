# ScheduleH4Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**SeekInfo**](SeekInfo.md) |  | [optional] 
**results** | [**List[ScheduleH4]**](ScheduleH4.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_h4_page import ScheduleH4Page

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleH4Page from a JSON string
schedule_h4_page_instance = ScheduleH4Page.from_json(json)
# print the JSON string representation of the object
print(ScheduleH4Page.to_json())

# convert the object into a dict
schedule_h4_page_dict = schedule_h4_page_instance.to_dict()
# create an instance of ScheduleH4Page from a dict
schedule_h4_page_from_dict = ScheduleH4Page.from_dict(schedule_h4_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


