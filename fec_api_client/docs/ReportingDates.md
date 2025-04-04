# ReportingDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **date** | Date the record was created | [optional] 
**due_date** | **date** | Date the report is due | [optional] 
**report_type** | **str** |  | [optional] 
**report_type_full** | **str** |  | [optional] 
**report_year** | **int** |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
**update_date** | **date** | Date the record was updated | [optional] 

## Example

```python
from openapi_client.models.reporting_dates import ReportingDates

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingDates from a JSON string
reporting_dates_instance = ReportingDates.from_json(json)
# print the JSON string representation of the object
print(ReportingDates.to_json())

# convert the object into a dict
reporting_dates_dict = reporting_dates_instance.to_dict()
# create an instance of ReportingDates from a dict
reporting_dates_from_dict = ReportingDates.from_dict(reporting_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


