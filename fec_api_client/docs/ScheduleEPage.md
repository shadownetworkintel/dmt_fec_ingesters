# ScheduleEPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**SeekInfo**](SeekInfo.md) |  | [optional] 
**results** | [**List[ScheduleE]**](ScheduleE.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_e_page import ScheduleEPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEPage from a JSON string
schedule_e_page_instance = ScheduleEPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleEPage.to_json())

# convert the object into a dict
schedule_e_page_dict = schedule_e_page_instance.to_dict()
# create an instance of ScheduleEPage from a dict
schedule_e_page_from_dict = ScheduleEPage.from_dict(schedule_e_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


