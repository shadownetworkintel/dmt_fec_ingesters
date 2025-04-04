# ScheduleAByZipPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleAByZip]**](ScheduleAByZip.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_zip_page import ScheduleAByZipPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByZipPage from a JSON string
schedule_aby_zip_page_instance = ScheduleAByZipPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByZipPage.to_json())

# convert the object into a dict
schedule_aby_zip_page_dict = schedule_aby_zip_page_instance.to_dict()
# create an instance of ScheduleAByZipPage from a dict
schedule_aby_zip_page_from_dict = ScheduleAByZipPage.from_dict(schedule_aby_zip_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


