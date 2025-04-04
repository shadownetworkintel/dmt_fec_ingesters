# NationalPartyScheduleA


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
**committee_designation** | **str** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**contribution_receipt_amount** | **float** |  | [optional] 
**contribution_receipt_date** | **date** |  | [optional] 
**contributor_aggregate_ytd** | **float** |  | [optional] 
**contributor_city** | **str** | City of contributor | [optional] 
**contributor_committee_designation** | **str** |  | [optional] 
**contributor_committee_designation_full** | **str** |  | [optional] 
**contributor_committee_name** | **str** |  | [optional] 
**contributor_committee_organization** | **str** |  | [optional] 
**contributor_committee_organization_full** | **str** |  | [optional] 
**contributor_committee_party** | **str** |  | [optional] 
**contributor_committee_party_full** | **str** |  | [optional] 
**contributor_committee_state** | **str** |  | [optional] 
**contributor_committee_state_full** | **str** |  | [optional] 
**contributor_committee_type** | **str** |  | [optional] 
**contributor_committee_type_full** | **str** |  | [optional] 
**contributor_employer** | **str** | Employer of contributor, filers need to make an effort to gather this information | [optional] 
**contributor_first_name** | **str** |  | [optional] 
**contributor_id** | **str** | The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
**contributor_last_name** | **str** |  | [optional] 
**contributor_middle_name** | **str** |  | [optional] 
**contributor_name** | **str** |  | [optional] 
**contributor_occupation** | **str** |  | [optional] 
**contributor_prefix** | **str** |  | [optional] 
**contributor_state** | **str** | State of contributor | [optional] 
**contributor_street_1** | **str** |  | [optional] 
**contributor_street_2** | **str** |  | [optional] 
**contributor_suffix** | **str** |  | [optional] 
**contributor_zip** | **str** | Zip code of contributor | [optional] 
**donor_committee_name** | **str** |  | [optional] 
**election_type** | **str** |  | [optional] 
**election_type_desc** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_type_desc** | **str** |  | [optional] 
**fec_election_type_desc** | **str** |  | [optional] 
**fec_election_year** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**filing_form** | **str** |  | [optional] 
**filing_frequency** | **str** |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**increased_limit** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_individual** | **bool** |  | [optional] 
**line_num** | **str** |  | [optional] 
**line_number_label** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**memo_cd** | **str** |  | [optional] 
**memo_cd_desc** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**national_cmte_nonfed_acct** | **str** |  | [optional] 
**orig_sub_id** | **int** |  | [optional] 
**original_sub_id** | **int** |  | [optional] 
**party** | **str** |  | [optional] 
**party_account_type** | **str** |  | [optional] 
**party_full** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**receipt_desc** | **str** |  | [optional] 
**receipt_type** | **str** |  | [optional] 
**receipt_type_desc** | **str** |  | [optional] 
**recipient_committee_designation** | **str** |  | [optional] 
**recipient_committee_designation_full** | **str** |  | [optional] 
**recipient_committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**recipient_committee_type_full** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**report_year** | **int** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_desc** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_full** | **str** |  | [optional] 
**sub_id** | **int** |  | [optional] 
**tran_id** | **str** |  | [optional] 
**treasurer_name** | **str** |  | [optional] 
**two_year_transaction_period** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.national_party_schedule_a import NationalPartyScheduleA

# TODO update the JSON string below
json = "{}"
# create an instance of NationalPartyScheduleA from a JSON string
national_party_schedule_a_instance = NationalPartyScheduleA.from_json(json)
# print the JSON string representation of the object
print(NationalPartyScheduleA.to_json())

# convert the object into a dict
national_party_schedule_a_dict = national_party_schedule_a_instance.to_dict()
# create an instance of NationalPartyScheduleA from a dict
national_party_schedule_a_from_dict = NationalPartyScheduleA.from_dict(national_party_schedule_a_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


