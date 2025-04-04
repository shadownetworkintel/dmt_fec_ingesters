# BaseF3PFiling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amended_by** | **int** |  | [optional] 
**amendment** | **object** |  | [optional] 
**amendment_chain** | **List[int]** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**cash_on_hand_beginning_period** | **float** |  | [optional] 
**cash_on_hand_end_period** | **float** |  | [optional] 
**city** | **str** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**coverage_end_date** | **date** |  | [optional] 
**coverage_start_date** | **date** |  | [optional] 
**csv_url** | **str** |  | [optional] 
**debts_owed_by_committee** | **float** |  | [optional] 
**debts_owed_to_committee** | **float** |  | [optional] 
**document_description** | **str** |  | [optional] 
**election_date** | **date** |  | [optional] 
**election_state** | **str** |  | [optional] 
**expenditure_subject_to_limits** | **float** |  | [optional] 
**fec_file_id** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**general_election** | **str** |  | [optional] 
**is_amended** | **bool** |  | [optional] 
**most_recent** | **bool** |  | [optional] 
**most_recent_filing** | **int** |  | [optional] 
**net_contributions_cycle_to_date** | **float** |  | [optional] 
**net_operating_expenditures_cycle_to_date** | **float** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**primary_election** | **str** |  | [optional] 
**receipt_date** | **date** |  | [optional] 
**report** | **object** |  | [optional] 
**report_type** | **str** |  | [optional] 
**report_year** | **int** |  | [optional] 
**rpt_pgi** | **str** | Election type  Convention, Primary, General, Special, Runoff etc.  | [optional] 
**sign_date** | **date** |  | [optional] 
**state** | **str** |  | [optional] 
**street_1** | **str** |  | [optional] 
**street_2** | **str** |  | [optional] 
**subtotal_summary_period** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**summary_lines** | **object** |  | [optional] [readonly] 
**treasurer_first_name** | **str** |  | [optional] 
**treasurer_last_name** | **str** |  | [optional] 
**treasurer_middle_name** | **str** |  | [optional] 
**treasurer_name** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.base_f3_p_filing import BaseF3PFiling

# TODO update the JSON string below
json = "{}"
# create an instance of BaseF3PFiling from a JSON string
base_f3_p_filing_instance = BaseF3PFiling.from_json(json)
# print the JSON string representation of the object
print(BaseF3PFiling.to_json())

# convert the object into a dict
base_f3_p_filing_dict = base_f3_p_filing_instance.to_dict()
# create an instance of BaseF3PFiling from a dict
base_f3_p_filing_from_dict = BaseF3PFiling.from_dict(base_f3_p_filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


