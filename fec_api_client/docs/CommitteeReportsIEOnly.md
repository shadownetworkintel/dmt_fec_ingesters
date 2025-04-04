# CommitteeReportsIEOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beginning_image_number** | **str** |  | [optional] 
**committee_id** | **str** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**committee_type** | **str** |  | [optional] 
**coverage_end_date** | **datetime** |  | [optional] 
**coverage_start_date** | **datetime** |  | [optional] 
**csv_url** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**document_description** | **str** |  | [optional] 
**end_image_number** | **str** |  | [optional] 
**fec_file_id** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**independent_contributions_period** | **float** |  | [optional] 
**independent_expenditures_period** | **float** |  | [optional] 
**is_amended** | **bool** |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
**means_filed** | **str** | The method used to file with the FEC, either electronic or on paper. | [optional] 
**pdf_url** | **str** |  | [optional] 
**receipt_date** | **date** | Date the FEC received the electronic or paper record | [optional] 
**report_form** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**report_type_full** | **str** |  | [optional] 
**report_year** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.committee_reports_ie_only import CommitteeReportsIEOnly

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeReportsIEOnly from a JSON string
committee_reports_ie_only_instance = CommitteeReportsIEOnly.from_json(json)
# print the JSON string representation of the object
print(CommitteeReportsIEOnly.to_json())

# convert the object into a dict
committee_reports_ie_only_dict = committee_reports_ie_only_instance.to_dict()
# create an instance of CommitteeReportsIEOnly from a dict
committee_reports_ie_only_from_dict = CommitteeReportsIEOnly.from_dict(committee_reports_ie_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


