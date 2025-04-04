# BaseF3XFiling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amend_address** | **str** |  | [optional] 
**amended_by** | **int** |  | [optional] 
**amendment** | **object** |  | [optional] 
**amendment_chain** | **List[int]** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**coverage_end_date** | **date** |  | [optional] 
**coverage_start_date** | **date** |  | [optional] 
**csv_url** | **str** |  | [optional] 
**document_description** | **str** |  | [optional] 
**election_date** | **date** |  | [optional] 
**election_state** | **str** |  | [optional] 
**fec_file_id** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**is_amended** | **bool** |  | [optional] 
**most_recent** | **bool** |  | [optional] 
**most_recent_filing** | **int** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**qualified_multicandidate_committee** | **str** |  | [optional] 
**receipt_date** | **date** |  | [optional] 
**report** | **object** |  | [optional] 
**report_type** | **str** |  | [optional] 
**report_year** | **int** |  | [optional] 
**rpt_pgi** | **str** | Election type  Convention, Primary, General, Special, Runoff etc.  | [optional] 
**sign_date** | **date** |  | [optional] 
**state** | **str** |  | [optional] 
**street_1** | **str** |  | [optional] 
**street_2** | **str** |  | [optional] 
**summary_lines** | **object** |  | [optional] [readonly] 
**zip** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.base_f3_x_filing import BaseF3XFiling

# TODO update the JSON string below
json = "{}"
# create an instance of BaseF3XFiling from a JSON string
base_f3_x_filing_instance = BaseF3XFiling.from_json(json)
# print the JSON string representation of the object
print(BaseF3XFiling.to_json())

# convert the object into a dict
base_f3_x_filing_dict = base_f3_x_filing_instance.to_dict()
# create an instance of BaseF3XFiling from a dict
base_f3_x_filing_from_dict = BaseF3XFiling.from_dict(base_f3_x_filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


