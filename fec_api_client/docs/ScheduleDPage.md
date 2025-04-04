# ScheduleDPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleD]**](ScheduleD.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_d_page import ScheduleDPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDPage from a JSON string
schedule_d_page_instance = ScheduleDPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleDPage.to_json())

# convert the object into a dict
schedule_d_page_dict = schedule_d_page_instance.to_dict()
# create an instance of ScheduleDPage from a dict
schedule_d_page_from_dict = ScheduleDPage.from_dict(schedule_d_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


