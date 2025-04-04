# ReportingDatesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ReportingDates]**](ReportingDates.md) |  | [optional] 

## Example

```python
from openapi_client.models.reporting_dates_page import ReportingDatesPage

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingDatesPage from a JSON string
reporting_dates_page_instance = ReportingDatesPage.from_json(json)
# print the JSON string representation of the object
print(ReportingDatesPage.to_json())

# convert the object into a dict
reporting_dates_page_dict = reporting_dates_page_instance.to_dict()
# create an instance of ReportingDatesPage from a dict
reporting_dates_page_from_dict = ReportingDatesPage.from_dict(reporting_dates_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


