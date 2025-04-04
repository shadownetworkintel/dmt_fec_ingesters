# OperationsLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_indicator** | **str** | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
**beginning_image_number** | **str** |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 
**candidate_committee_id** | **str** |  A unique identifier of the registered filer.  | [optional] 
**coverage_end_date** | **datetime** | Ending date of the reporting period | [optional] 
**coverage_start_date** | **datetime** | Beginning date of the reporting period | [optional] 
**ending_image_number** | **str** | Image number is an unique identifier for each page the electronic or paper report. The last image number corresponds to the image number for the last page of the document. | [optional] 
**form_type** | **str** | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
**receipt_date** | **datetime** | Date the FEC received the electronic or paper record | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_year** | **int** |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
**status_num** | **int** |  Status of the transactional report.     -0- Transaction is entered            into the system.           But not verified.     -1- Transaction is verified.  | [optional] 
**sub_id** | **int** |  A unique identifier of the transactional report.  | [optional] 
**summary_data_complete_date** | **datetime** |  Date when the report is entered into the database  | [optional] 
**summary_data_verification_date** | **datetime** |  Same day or a day after the report is loaded in the database  | [optional] 
**transaction_data_complete_date** | **date** |  Date when the report is processed completely  | [optional] 

## Example

```python
from openapi_client.models.operations_log import OperationsLog

# TODO update the JSON string below
json = "{}"
# create an instance of OperationsLog from a JSON string
operations_log_instance = OperationsLog.from_json(json)
# print the JSON string representation of the object
print(OperationsLog.to_json())

# convert the object into a dict
operations_log_dict = operations_log_instance.to_dict()
# create an instance of OperationsLog from a dict
operations_log_from_dict = OperationsLog.from_dict(operations_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


