# ScheduleC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_code** | **str** |  | [optional] 
**action_code_full** | **str** |  | [optional] 
**candidate_first_name** | **str** |  | [optional] 
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**candidate_last_name** | **str** |  | [optional] 
**candidate_middle_name** | **str** |  | [optional] 
**candidate_name** | **str** | Name of candidate running for office | [optional] 
**candidate_office** | **str** |  | [optional] 
**candidate_office_district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**candidate_office_full** | **str** |  | [optional] 
**candidate_office_state** | **str** |  | [optional] 
**candidate_office_state_full** | **str** |  | [optional] 
**candidate_prefix** | **str** |  | [optional] 
**candidate_suffix** | **str** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**cycle** | **int** |  | [optional] 
**due_date_terms** | **str** |  | [optional] 
**election_type** | **str** |  | [optional] 
**election_type_full** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_type_full** | **str** |  | [optional] 
**fec_committee_id** | **str** |  | [optional] 
**fec_election_type_full** | **str** |  | [optional] 
**fec_election_type_year** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**filing_form** | **str** |  | [optional] 
**form_line_number** | **str** |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**incurred_date** | **date** |  | [optional] 
**interest_rate_terms** | **str** |  | [optional] 
**line_number** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**load_date** | **datetime** |  | [optional] 
**loan_balance** | **float** |  | [optional] 
**loan_source_city** | **str** |  | [optional] 
**loan_source_first_name** | **str** |  | [optional] 
**loan_source_last_name** | **str** |  | [optional] 
**loan_source_middle_name** | **str** |  | [optional] 
**loan_source_name** | **str** | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate | [optional] 
**loan_source_prefix** | **str** |  | [optional] 
**loan_source_state** | **str** |  | [optional] 
**loan_source_street_1** | **str** |  | [optional] 
**loan_source_street_2** | **str** |  | [optional] 
**loan_source_suffix** | **str** |  | [optional] 
**loan_source_zip** | **str** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**original_loan_amount** | **float** |  | [optional] 
**original_sub_id** | **int** |  | [optional] 
**payment_to_date** | **float** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**personally_funded** | **str** |  | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_year** | **float** |  | [optional] 
**schedule_a_line_number** | **str** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_full** | **str** |  | [optional] 
**secured_ind** | **str** |  | [optional] 
**sub_id** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_c import ScheduleC

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleC from a JSON string
schedule_c_instance = ScheduleC.from_json(json)
# print the JSON string representation of the object
print(ScheduleC.to_json())

# convert the object into a dict
schedule_c_dict = schedule_c_instance.to_dict()
# create an instance of ScheduleC from a dict
schedule_c_from_dict = ScheduleC.from_dict(schedule_c_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


