# CalendarDatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CalendarDate]**](CalendarDate.md) |  | [optional] 

## Example

```python
from openapi_client.models.calendar_date_page import CalendarDatePage

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarDatePage from a JSON string
calendar_date_page_instance = CalendarDatePage.from_json(json)
# print the JSON string representation of the object
print(CalendarDatePage.to_json())

# convert the object into a dict
calendar_date_page_dict = calendar_date_page_instance.to_dict()
# create an instance of CalendarDatePage from a dict
calendar_date_page_from_dict = CalendarDatePage.from_dict(calendar_date_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


