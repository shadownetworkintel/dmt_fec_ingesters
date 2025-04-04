# NationalPartyScheduleB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_indicator** | **str** |  | [optional] 
**amendment_indicator_desc** | **str** |  | [optional] 
**back_reference_schedule_id** | **str** |  | [optional] 
**back_reference_transaction_id** | **str** |  | [optional] 
**benef_committee_name** | **str** |  | [optional] 
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
**category_code** | **str** |  | [optional] 
**category_code_desc** | **str** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**disbursement_amount** | **float** |  | [optional] 
**disbursement_date** | **date** |  | [optional] 
**disbursement_description** | **str** |  | [optional] 
**disbursement_purpose_category** | **str** |  | [optional] 
**disbursement_type** | **str** |  | [optional] 
**disbursement_type_desc** | **str** |  | [optional] 
**election_type** | **str** |  | [optional] 
**election_type_desc** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_type_desc** | **str** |  | [optional] 
**fec_election_type_desc** | **str** |  | [optional] 
**fec_election_type_year** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**filing_form** | **str** |  | [optional] 
**filing_frequency** | **str** |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**is_active** | **bool** |  | [optional] 
**line_number** | **str** |  | [optional] 
**line_number_label** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**memo_cd** | **str** |  | [optional] 
**memo_cd_desc** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**national_cmte_nonfed_acct** | **str** |  | [optional] 
**orig_sub_id** | **int** |  | [optional] 
**original_sub_id** | **int** |  | [optional] 
**party** | **str** |  | [optional] 
**party_account** | **str** |  | [optional] 
**party_full** | **str** |  | [optional] 
**payee_employer** | **str** |  | [optional] 
**payee_first_name** | **str** |  | [optional] 
**payee_last_name** | **str** |  | [optional] 
**payee_middle_name** | **str** |  | [optional] 
**payee_occupation** | **str** |  | [optional] 
**payee_prefix** | **str** |  | [optional] 
**payee_suffix** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**recipient_city** | **str** |  | [optional] 
**recipient_committee_designation** | **str** |  | [optional] 
**recipient_committee_designation_full** | **str** |  | [optional] 
**recipient_committee_id** | **str** |  | [optional] 
**recipient_committee_name** | **str** |  | [optional] 
**recipient_committee_org** | **str** |  | [optional] 
**recipient_committee_org_full** | **str** |  | [optional] 
**recipient_committee_party** | **str** |  | [optional] 
**recipient_committee_party_full** | **str** |  | [optional] 
**recipient_committee_state** | **str** |  | [optional] 
**recipient_committee_state_full** | **str** |  | [optional] 
**recipient_committee_type** | **str** |  | [optional] 
**recipient_committee_type_full** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_state** | **str** |  | [optional] 
**recipient_street1** | **str** |  | [optional] 
**recipient_street2** | **str** |  | [optional] 
**recipient_zip** | **str** |  | [optional] 
**ref_disp_excess_flg** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**report_year** | **int** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_desc** | **str** |  | [optional] 
**semi_an_bundled_refund** | **float** |  | [optional] 
**spender_committee_designation** | **str** |  | [optional] 
**spender_committee_designation_full** | **str** |  | [optional] 
**spender_committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**spender_committee_type_full** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_full** | **str** |  | [optional] 
**sub_id** | **int** |  | [optional] 
**tran_id** | **str** |  | [optional] 
**treasurer_name** | **str** |  | [optional] 
**two_year_transaction_period** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.national_party_schedule_b import NationalPartyScheduleB

# TODO update the JSON string below
json = "{}"
# create an instance of NationalPartyScheduleB from a JSON string
national_party_schedule_b_instance = NationalPartyScheduleB.from_json(json)
# print the JSON string representation of the object
print(NationalPartyScheduleB.to_json())

# convert the object into a dict
national_party_schedule_b_dict = national_party_schedule_b_instance.to_dict()
# create an instance of NationalPartyScheduleB from a dict
national_party_schedule_b_from_dict = NationalPartyScheduleB.from_dict(national_party_schedule_b_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


