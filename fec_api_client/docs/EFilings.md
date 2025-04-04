# EFilings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amended_by** | **int** |  | [optional] 
**amendment_chain** | **List[int]** |  | [optional] 
**amendment_number** | **int** |  Number of times the report has been amended.  | [optional] 
**amends_file** | **int** |  For amendments, this file_number is the file_number of the previous report that is being amended. Refer to the amended_by for the most recent version of the report.  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**coverage_end_date** | **date** | Ending date of the reporting period | [optional] 
**coverage_start_date** | **date** | Beginning date of the reporting period | [optional] 
**csv_url** | **str** |  | [optional] 
**document_description** | **str** |  | [optional] 
**ending_image_number** | **str** |  | [optional] 
**fec_file_id** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** | Filing ID number | [optional] 
**filed_date** | **date** | Timestamp of electronic or paper record that FEC received | [optional] 
**form_type** | **str** | The form where the underlying data comes from, for example Form 1 would appear as F1:      - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text NOTE: This filter also works if you specify new, amended, or termination,  for example F3XN, F3XA, or F3XT respectively   | [optional] 
**html_url** | **str** |  | [optional] 
**is_amended** | **bool** |  | [optional] 
**load_timestamp** | **datetime** | Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently. | [optional] 
**most_recent** | **bool** |  | [optional] 
**most_recent_filing** | **int** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**receipt_date** | **datetime** | Date the FEC received the electronic or paper record | [optional] 

## Example

```python
from openapi_client.models.e_filings import EFilings

# TODO update the JSON string below
json = "{}"
# create an instance of EFilings from a JSON string
e_filings_instance = EFilings.from_json(json)
# print the JSON string representation of the object
print(EFilings.to_json())

# convert the object into a dict
e_filings_dict = e_filings_instance.to_dict()
# create an instance of EFilings from a dict
e_filings_from_dict = EFilings.from_dict(e_filings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


