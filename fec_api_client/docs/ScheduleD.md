# ScheduleD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_code** | **str** |  | [optional] 
**action_code_full** | **str** |  | [optional] 
**amount_incurred_period** | **float** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**coverage_end_date** | **date** | Ending date of the reporting period | [optional] 
**coverage_start_date** | **date** | Beginning date of the reporting period | [optional] 
**creditor_debtor_city** | **str** |  | [optional] 
**creditor_debtor_first_name** | **str** |  | [optional] 
**creditor_debtor_last_name** | **str** |  | [optional] 
**creditor_debtor_middle_name** | **str** |  | [optional] 
**creditor_debtor_name** | **str** |  | [optional] 
**creditor_debtor_prefix** | **str** |  | [optional] 
**creditor_debtor_state** | **str** |  | [optional] 
**creditor_debtor_street1** | **str** |  | [optional] 
**creditor_debtor_street2** | **str** |  | [optional] 
**creditor_debtor_suffix** | **str** |  | [optional] 
**election_cycle** | **int** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**filing_form** | **str** | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
**form_line_number** | **str** |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**line_number** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**nature_of_debt** | **str** |  | [optional] 
**original_sub_id** | **int** |  | [optional] 
**outstanding_balance_beginning_of_period** | **float** |  | [optional] 
**outstanding_balance_close_of_period** | **float** |  | [optional] 
**payment_period** | **float** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_year** | **int** |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_full** | **str** |  | [optional] 
**sub_id** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_d import ScheduleD

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleD from a JSON string
schedule_d_instance = ScheduleD.from_json(json)
# print the JSON string representation of the object
print(ScheduleD.to_json())

# convert the object into a dict
schedule_d_dict = schedule_d_instance.to_dict()
# create an instance of ScheduleD from a dict
schedule_d_from_dict = ScheduleD.from_dict(schedule_d_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


