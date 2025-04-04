# ScheduleA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_indicator** | **str** |  | [optional] 
**amendment_indicator_desc** | **str** |  | [optional] 
**back_reference_schedule_name** | **str** |  | [optional] 
**back_reference_transaction_id** | **str** |  | [optional] 
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
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**conduit_committee_city** | **str** |  | [optional] 
**conduit_committee_id** | **str** |  | [optional] 
**conduit_committee_name** | **str** |  | [optional] 
**conduit_committee_state** | **str** |  | [optional] 
**conduit_committee_street1** | **str** |  | [optional] 
**conduit_committee_street2** | **str** |  | [optional] 
**conduit_committee_zip** | **str** |  | [optional] 
**contribution_receipt_amount** | **float** |  | [optional] 
**contribution_receipt_date** | **date** |  | [optional] 
**contributor** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**contributor_aggregate_ytd** | **float** | Total amount received from this source for the year to date. Starting 2000, it is aggregated on an election-cycle basis in F3 and F3P, and calendar year in F3X. | [optional] 
**contributor_city** | **str** | City of contributor | [optional] 
**contributor_employer** | **str** | Employer of contributor, filers need to make an effort to gather this information | [optional] 
**contributor_first_name** | **str** |  | [optional] 
**contributor_id** | **str** | The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
**contributor_last_name** | **str** |  | [optional] 
**contributor_middle_name** | **str** |  | [optional] 
**contributor_name** | **str** | Name of contributor | [optional] 
**contributor_occupation** | **str** | Occupation of contributor, filers need to make an effort to gather this information | [optional] 
**contributor_prefix** | **str** |  | [optional] 
**contributor_state** | **str** | State of contributor | [optional] 
**contributor_street_1** | **str** |  | [optional] 
**contributor_street_2** | **str** |  | [optional] 
**contributor_suffix** | **str** |  | [optional] 
**contributor_zip** | **str** | Zip code of contributor | [optional] 
**donor_committee_name** | **str** |  | [optional] 
**election_type** | **str** |  | [optional] 
**election_type_full** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_type_desc** | **str** |  | [optional] 
**fec_election_type_desc** | **str** |  | [optional] 
**fec_election_year** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**filing_form** | **str** |  | [optional] 
**image_number** | **str** |  | [optional] 
**increased_limit** | **str** |  | [optional] 
**is_individual** | **bool** |  | [optional] 
**line_number** | **str** |  | [optional] 
**line_number_label** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**load_date** | **datetime** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_code_full** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**memoed_subtotal** | **bool** |  | [optional] 
**national_committee_nonfederal_account** | **str** |  | [optional] 
**original_sub_id** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**receipt_type** | **str** |  | [optional] 
**receipt_type_desc** | **str** |  | [optional] 
**receipt_type_full** | **str** |  | [optional] 
**recipient_committee_designation** | **str** |  | [optional] 
**recipient_committee_org_type** | **str** |  | [optional] 
**recipient_committee_type** | **str** |  | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_year** | **int** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_full** | **str** |  | [optional] 
**sub_id** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**two_year_transaction_period** | **int** |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
**unused_contbr_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_a import ScheduleA

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleA from a JSON string
schedule_a_instance = ScheduleA.from_json(json)
# print the JSON string representation of the object
print(ScheduleA.to_json())

# convert the object into a dict
schedule_a_dict = schedule_a_instance.to_dict()
# create an instance of ScheduleA from a dict
schedule_a_from_dict = ScheduleA.from_dict(schedule_a_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


