# ScheduleFPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleF]**](ScheduleF.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_f_page import ScheduleFPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleFPage from a JSON string
schedule_f_page_instance = ScheduleFPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleFPage.to_json())

# convert the object into a dict
schedule_f_page_dict = schedule_f_page_instance.to_dict()
# create an instance of ScheduleFPage from a dict
schedule_f_page_from_dict = ScheduleFPage.from_dict(schedule_f_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


