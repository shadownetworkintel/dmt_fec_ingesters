# Filings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_bank_names** | **List[str]** |  Additional banks or depositories in which the committee deposits funds, holds accounts, rents safety deposit boxes or maintains funds.  | [optional] 
**amendment_chain** | **List[int]** |  | [optional] 
**amendment_indicator** | **str** |  The first value in the chain is the original filing.  The ordering in the chain reflects the order the amendments were filed up to the amendment being inspected.  | [optional] 
**amendment_version** | **int** |  Amendment version  | [optional] 
**bank_depository_city** | **str** |  City of bank or depository as reported on the Form 1  | [optional] 
**bank_depository_name** | **str** |  Primary bank or depository in which the committee deposits funds,holds accounts, rents safety deposit boxes or maintains funds.  | [optional] 
**bank_depository_state** | **str** |  State of bank or depository as reported on the Form 1  | [optional] 
**bank_depository_street_1** | **str** |  Street of bank or depository as reported on their Form 1.  | [optional] 
**bank_depository_street_2** | **str** |  Second line of the street of bank or depository as reported on the Form 1  | [optional] 
**bank_depository_zip** | **str** |  Zip code of bank or depository as reported on the Form 1  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**candidate_name** | **str** | Name of candidate running for office | [optional] 
**cash_on_hand_beginning_period** | **float** |  | [optional] 
**cash_on_hand_end_period** | **float** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**coverage_end_date** | **date** | Ending date of the reporting period | [optional] 
**coverage_start_date** | **date** | Beginning date of the reporting period | [optional] 
**csv_url** | **str** |  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**debts_owed_by_committee** | **float** |  | [optional] 
**debts_owed_to_committee** | **float** |  | [optional] 
**document_description** | **str** |  | [optional] 
**document_type** | **str** |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional] 
**document_type_full** | **str** |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional] 
**election_year** | **int** | Year of election | [optional] 
**ending_image_number** | **str** |  | [optional] 
**fec_file_id** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** | Filing ID number | [optional] 
**form_category** | **str** |  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13, F24     - NOTICE F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  | [optional] 
**form_type** | **str** | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
**house_personal_funds** | **float** |  | [optional] 
**html_url** | **str** |  HTML link to the filing.  | [optional] 
**is_amended** | **bool** |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
**means_filed** | **str** | The method used to file with the FEC, either electronic or on paper. | [optional] 
**most_recent** | **bool** |  Report is either new or is the most-recently filed amendment  | [optional] 
**most_recent_file_number** | **int** |  | [optional] 
**net_donations** | **float** |  | [optional] 
**office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**opposition_personal_funds** | **float** |  | [optional] 
**pages** | **int** |  Number of pages in the document  | [optional] 
**party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**pdf_url** | **str** |  pdf link to the filing  | [optional] 
**previous_file_number** | **int** |  Previous filing ID number  | [optional] 
**primary_general_indicator** | **str** |  Primary general indicator  | [optional] 
**receipt_date** | **datetime** | Date the FEC received the electronic or paper record | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_type_full** | **str** |  | [optional] 
**report_year** | **int** |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
**request_type** | **str** |  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  | [optional] 
**senate_personal_funds** | **float** |  | [optional] 
**state** | **str** | US state or territory where a candidate runs for office | [optional] 
**sub_id** | **str** |  | [optional] 
**total_communication_cost** | **float** |  | [optional] 
**total_disbursements** | **float** |  | [optional] 
**total_independent_expenditures** | **float** |  | [optional] 
**total_individual_contributions** | **float** |  | [optional] 
**total_receipts** | **float** |  | [optional] 
**treasurer_name** | **str** | Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
**update_date** | **date** | Date the record was updated | [optional] 

## Example

```python
from openapi_client.models.filings import Filings

# TODO update the JSON string below
json = "{}"
# create an instance of Filings from a JSON string
filings_instance = Filings.from_json(json)
# print the JSON string representation of the object
print(Filings.to_json())

# convert the object into a dict
filings_dict = filings_instance.to_dict()
# create an instance of Filings from a dict
filings_from_dict = Filings.from_dict(filings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


