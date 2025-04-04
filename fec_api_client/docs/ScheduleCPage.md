# ScheduleCPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleC]**](ScheduleC.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_c_page import ScheduleCPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCPage from a JSON string
schedule_c_page_instance = ScheduleCPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleCPage.to_json())

# convert the object into a dict
schedule_c_page_dict = schedule_c_page_instance.to_dict()
# create an instance of ScheduleCPage from a dict
schedule_c_page_from_dict = ScheduleCPage.from_dict(schedule_c_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


