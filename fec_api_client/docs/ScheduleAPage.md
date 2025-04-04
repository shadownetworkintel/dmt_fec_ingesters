# ScheduleAPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**SeekInfo**](SeekInfo.md) |  | [optional] 
**results** | [**List[ScheduleA]**](ScheduleA.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_a_page import ScheduleAPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAPage from a JSON string
schedule_a_page_instance = ScheduleAPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleAPage.to_json())

# convert the object into a dict
schedule_a_page_dict = schedule_a_page_instance.to_dict()
# create an instance of ScheduleAPage from a dict
schedule_a_page_from_dict = ScheduleAPage.from_dict(schedule_a_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


