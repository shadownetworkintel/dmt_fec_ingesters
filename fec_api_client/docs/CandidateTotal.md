# CandidateTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
**candidate_inactive** | **bool** |  True indicates that a candidate is inactive.  | [optional] 
**cash_on_hand_end_period** | **float** | Ending cash balance on the most recent filing | [optional] 
**coverage_end_date** | **date** | Ending date of the reporting period | [optional] 
**coverage_start_date** | **date** | Beginning date of the reporting period | [optional] 
**cycle** | **int** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | 
**debts_owed_by_committee** | **float** | Debts owed by the committee | [optional] 
**disbursements** | **float** |  | [optional] 
**district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**district_number** | **int** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**election_year** | **int** | Year of election | [optional] 
**federal_funds_flag** | **bool** | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
**has_raised_funds** | **bool** | A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
**individual_itemized_contributions** | **float** |  | [optional] 
**is_election** | **bool** |  | 
**office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**other_political_committee_contributions** | **float** |  | [optional] 
**party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**receipts** | **float** |  | [optional] 
**state** | **str** | US state or territory where a candidate runs for office | [optional] 
**state_full** | **str** | US state or territory where a candidate runs for office | [optional] 
**transfers_from_other_authorized_committee** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.candidate_total import CandidateTotal

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateTotal from a JSON string
candidate_total_instance = CandidateTotal.from_json(json)
# print the JSON string representation of the object
print(CandidateTotal.to_json())

# convert the object into a dict
candidate_total_dict = candidate_total_instance.to_dict()
# create an instance of CandidateTotal from a dict
candidate_total_from_dict = CandidateTotal.from_dict(candidate_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


