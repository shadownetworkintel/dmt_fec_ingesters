# ScheduleBPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**SeekInfo**](SeekInfo.md) |  | [optional] 
**results** | [**List[ScheduleB]**](ScheduleB.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_b_page import ScheduleBPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBPage from a JSON string
schedule_b_page_instance = ScheduleBPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleBPage.to_json())

# convert the object into a dict
schedule_b_page_dict = schedule_b_page_instance.to_dict()
# create an instance of ScheduleBPage from a dict
schedule_b_page_from_dict = ScheduleBPage.from_dict(schedule_b_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


