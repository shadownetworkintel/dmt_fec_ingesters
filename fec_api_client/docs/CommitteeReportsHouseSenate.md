# CommitteeReportsHouseSenate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_amount_personal_contributions_general** | **float** |  | [optional] 
**aggregate_contributions_personal_funds_primary** | **float** |  | [optional] 
**all_other_loans_period** | **float** |  | [optional] 
**all_other_loans_ytd** | **float** |  | [optional] 
**amendment_chain** | **List[float]** |  The first value in the chain is the original filing.  The ordering in the chain reflects the order the amendments were filed up to the amendment being inspected.  | [optional] 
**amendment_indicator** | **str** |  | [optional] 
**amendment_indicator_full** | **str** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**candidate_contribution_period** | **float** |  | [optional] 
**candidate_contribution_ytd** | **float** |  | [optional] 
**cash_on_hand_beginning_period** | **float** |  | [optional] 
**cash_on_hand_end_period** | **float** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**committee_type** | **str** |  | [optional] 
**coverage_end_date** | **datetime** | Ending date of the reporting period | [optional] 
**coverage_start_date** | **datetime** | Beginning date of the reporting period | [optional] 
**csv_url** | **str** |  | [optional] 
**cycle** | **int** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**debts_owed_by_committee** | **float** |  | [optional] 
**debts_owed_to_committee** | **float** |  | [optional] 
**document_description** | **str** |  | [optional] 
**end_image_number** | **str** |  | [optional] 
**fec_file_id** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**gross_receipt_authorized_committee_general** | **float** |  | [optional] 
**gross_receipt_authorized_committee_primary** | **float** |  | [optional] 
**gross_receipt_minus_personal_contribution_general** | **float** |  | [optional] 
**gross_receipt_minus_personal_contributions_primary** | **float** |  | [optional] 
**html_url** | **str** |  HTML link to the filing.  | [optional] 
**individual_itemized_contributions_period** | **float** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. total for the reporting period | [optional] 
**individual_itemized_contributions_ytd** | **float** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. total for the year to date | [optional] 
**individual_unitemized_contributions_period** | **float** | Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. total for the reporting period | [optional] 
**individual_unitemized_contributions_ytd** | **float** | Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. total for the year to date | [optional] 
**is_amended** | **bool** |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
**loan_repayments_candidate_loans_period** | **float** |  | [optional] 
**loan_repayments_candidate_loans_ytd** | **float** |  | [optional] 
**loan_repayments_other_loans_period** | **float** |  | [optional] 
**loan_repayments_other_loans_ytd** | **float** |  | [optional] 
**loans_made_by_candidate_period** | **float** |  | [optional] 
**loans_made_by_candidate_ytd** | **float** |  | [optional] 
**means_filed** | **str** | The method used to file with the FEC, either electronic or on paper. | [optional] 
**most_recent** | **bool** |  Report is either new or is the most-recently filed amendment  | [optional] 
**most_recent_file_number** | **float** |  | [optional] 
**net_contributions_period** | **float** |  | [optional] 
**net_contributions_ytd** | **float** |  | [optional] 
**net_operating_expenditures_period** | **float** |  | [optional] 
**net_operating_expenditures_ytd** | **float** |  | [optional] 
**offsets_to_operating_expenditures_period** | **float** | Offsets to operating expenditures total for the reporting period | [optional] 
**offsets_to_operating_expenditures_ytd** | **float** | Offsets to operating expenditures total for the year to date | [optional] 
**operating_expenditures_period** | **float** |  | [optional] 
**operating_expenditures_ytd** | **float** |  | [optional] 
**other_disbursements_period** | **float** |  | [optional] 
**other_disbursements_ytd** | **float** |  | [optional] 
**other_political_committee_contributions_period** | **float** |  | [optional] 
**other_political_committee_contributions_ytd** | **float** |  | [optional] 
**other_receipts_period** | **float** |  | [optional] 
**other_receipts_ytd** | **float** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**political_party_committee_contributions_period** | **float** |  | [optional] 
**political_party_committee_contributions_ytd** | **float** |  | [optional] 
**previous_file_number** | **float** |  | [optional] 
**receipt_date** | **date** | Date the FEC received the electronic or paper record | [optional] 
**refunded_individual_contributions_period** | **float** |  | [optional] 
**refunded_individual_contributions_ytd** | **float** |  | [optional] 
**refunded_other_political_committee_contributions_period** | **float** |  | [optional] 
**refunded_other_political_committee_contributions_ytd** | **float** |  | [optional] 
**refunded_political_party_committee_contributions_period** | **float** |  | [optional] 
**refunded_political_party_committee_contributions_ytd** | **float** |  | [optional] 
**refunds_total_contributions_col_total_ytd** | **float** |  | [optional] 
**report_form** | **str** |  | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_type_full** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_year** | **int** |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
**subtotal_period** | **float** |  | [optional] 
**total_contribution_refunds_col_total_period** | **float** |  | [optional] 
**total_contribution_refunds_period** | **float** |  | [optional] 
**total_contribution_refunds_ytd** | **float** |  | [optional] 
**total_contributions_column_total_period** | **float** |  | [optional] 
**total_contributions_period** | **float** |  | [optional] 
**total_contributions_ytd** | **float** |  | [optional] 
**total_disbursements_period** | **float** |  | [optional] 
**total_disbursements_ytd** | **float** |  | [optional] 
**total_individual_contributions_period** | **float** | Individual contributions total for the reporting period | [optional] 
**total_individual_contributions_ytd** | **float** | Individual contributions total for the year to date | [optional] 
**total_loan_repayments_made_period** | **float** |  | [optional] 
**total_loan_repayments_made_ytd** | **float** |  | [optional] 
**total_loans_received_period** | **float** |  | [optional] 
**total_loans_received_ytd** | **float** |  | [optional] 
**total_offsets_to_operating_expenditures_period** | **float** |  | [optional] 
**total_offsets_to_operating_expenditures_ytd** | **float** |  | [optional] 
**total_operating_expenditures_period** | **float** |  | [optional] 
**total_operating_expenditures_ytd** | **float** |  | [optional] 
**total_receipts_period** | **float** |  | [optional] 
**total_receipts_ytd** | **float** | Anything of value (money, goods, services or property) received by a political committee total for the year to date | [optional] 
**transfers_from_other_authorized_committee_period** | **float** |  | [optional] 
**transfers_from_other_authorized_committee_ytd** | **float** |  | [optional] 
**transfers_to_other_authorized_committee_period** | **float** |  | [optional] 
**transfers_to_other_authorized_committee_ytd** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.committee_reports_house_senate import CommitteeReportsHouseSenate

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeReportsHouseSenate from a JSON string
committee_reports_house_senate_instance = CommitteeReportsHouseSenate.from_json(json)
# print the JSON string representation of the object
print(CommitteeReportsHouseSenate.to_json())

# convert the object into a dict
committee_reports_house_senate_dict = committee_reports_house_senate_instance.to_dict()
# create an instance of CommitteeReportsHouseSenate from a dict
committee_reports_house_senate_from_dict = CommitteeReportsHouseSenate.from_dict(committee_reports_house_senate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


