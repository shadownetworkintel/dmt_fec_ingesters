# ScheduleE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_code** | **str** |  | [optional] 
**action_code_full** | **str** |  | [optional] 
**amendment_indicator** | **str** | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
**amendment_number** | **int** |  Number of times the report has been amended.  | [optional] 
**back_reference_schedule_name** | **str** |  | [optional] 
**back_reference_transaction_id** | **str** |  | [optional] 
**candidate** | **object** |  | [optional] 
**candidate_first_name** | **str** |  | [optional] 
**candidate_id** | **str** |  | [optional] 
**candidate_last_name** | **str** |  | [optional] 
**candidate_middle_name** | **str** |  | [optional] 
**candidate_name** | **str** | Name of candidate running for office | [optional] 
**candidate_office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**candidate_office_district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**candidate_office_state** | **str** | US state or territory | [optional] 
**candidate_party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**candidate_prefix** | **str** |  | [optional] 
**candidate_suffix** | **str** |  | [optional] 
**category_code** | **str** |  | [optional] 
**category_code_full** | **str** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**conduit_committee_city** | **str** |  | [optional] 
**conduit_committee_id** | **str** |  | [optional] 
**conduit_committee_name** | **str** |  | [optional] 
**conduit_committee_state** | **str** |  | [optional] 
**conduit_committee_street1** | **str** |  | [optional] 
**conduit_committee_street2** | **str** |  | [optional] 
**conduit_committee_zip** | **str** |  | [optional] 
**disbursement_dt** | **date** |  | [optional] 
**dissemination_date** | **date** |  | [optional] 
**election_type** | **str** | Election type  Convention, Primary, General, Special, Runoff etc.  | [optional] 
**election_type_full** | **str** | Election type  Convention, Primary, General, Special, Runoff etc.  | [optional] 
**expenditure_amount** | **float** |  | [optional] 
**expenditure_date** | **date** |  | [optional] 
**expenditure_description** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**filer_first_name** | **str** |  | [optional] 
**filer_last_name** | **str** |  | [optional] 
**filer_middle_name** | **str** |  | [optional] 
**filer_prefix** | **str** |  | [optional] 
**filer_suffix** | **str** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**filing_form** | **str** |  | [optional] 
**form_line_number** | **str** |  | [optional] 
**image_number** | **str** |  | [optional] 
**independent_sign_date** | **date** |  | [optional] 
**independent_sign_name** | **str** |  | [optional] 
**is_notice** | **bool** |  | [optional] 
**line_number** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_code_full** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**memoed_subtotal** | **bool** |  | [optional] 
**most_recent** | **bool** |  Report is either new or is the most-recently filed amendment  | [optional] 
**notary_commission_expiration_date** | **date** |  | [optional] 
**notary_sign_date** | **date** |  | [optional] 
**notary_sign_name** | **str** |  | [optional] 
**office_total_ytd** | **float** |  | [optional] 
**original_sub_id** | **str** |  | [optional] 
**payee_city** | **str** |  | [optional] 
**payee_first_name** | **str** |  | [optional] 
**payee_last_name** | **str** |  | [optional] 
**payee_middle_name** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**payee_prefix** | **str** |  | [optional] 
**payee_state** | **str** |  | [optional] 
**payee_street_1** | **str** |  | [optional] 
**payee_street_2** | **str** |  | [optional] 
**payee_suffix** | **str** |  | [optional] 
**payee_zip** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**previous_file_number** | **int** |  | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_year** | **float** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_full** | **str** |  | [optional] 
**sub_id** | **str** |  | [optional] 
**support_oppose_indicator** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_e import ScheduleE

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleE from a JSON string
schedule_e_instance = ScheduleE.from_json(json)
# print the JSON string representation of the object
print(ScheduleE.to_json())

# convert the object into a dict
schedule_e_dict = schedule_e_instance.to_dict()
# create an instance of ScheduleE from a dict
schedule_e_from_dict = ScheduleE.from_dict(schedule_e_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


