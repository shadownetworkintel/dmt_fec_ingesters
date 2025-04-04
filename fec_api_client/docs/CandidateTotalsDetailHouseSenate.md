# CandidateTotalsDetailHouseSenate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_other_loans** | **float** |  | [optional] 
**candidate_contribution** | **float** |  | [optional] 
**candidate_election_year** | **int** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | 
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
**contribution_refunds** | **float** |  | [optional] 
**contributions** | **float** |  | [optional] 
**coverage_end_date** | **datetime** |  | [optional] 
**coverage_start_date** | **datetime** |  | [optional] 
**cycle** | **int** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | 
**disbursements** | **float** |  | [optional] 
**election_full** | **bool** |  | 
**exempt_legal_accounting_disbursement** | **float** |  | [optional] 
**federal_funds** | **float** |  | [optional] 
**fundraising_disbursements** | **float** |  | [optional] 
**individual_contributions** | **float** |  | [optional] 
**individual_itemized_contributions** | **float** |  | [optional] 
**individual_unitemized_contributions** | **float** |  | [optional] 
**last_beginning_image_number** | **str** |  | [optional] 
**last_cash_on_hand_end_period** | **float** |  | [optional] 
**last_debts_owed_by_committee** | **float** |  | [optional] 
**last_debts_owed_to_committee** | **float** |  | [optional] 
**last_net_contributions** | **float** |  | [optional] 
**last_net_operating_expenditures** | **float** |  | [optional] 
**last_report_type_full** | **str** |  | [optional] 
**last_report_year** | **int** |  | [optional] 
**loan_repayments** | **float** |  | [optional] 
**loan_repayments_candidate_loans** | **float** |  | [optional] 
**loan_repayments_other_loans** | **float** |  | [optional] 
**loans** | **float** |  | [optional] 
**loans_made_by_candidate** | **float** |  | [optional] 
**net_contributions** | **float** |  | [optional] 
**net_operating_expenditures** | **float** |  | [optional] 
**offsets_to_fundraising_expenditures** | **float** |  | [optional] 
**offsets_to_legal_accounting** | **float** |  | [optional] 
**offsets_to_operating_expenditures** | **float** |  | [optional] 
**operating_expenditures** | **float** |  | [optional] 
**other_disbursements** | **float** |  | [optional] 
**other_political_committee_contributions** | **float** |  | [optional] 
**other_receipts** | **float** |  | [optional] 
**political_party_committee_contributions** | **float** |  | [optional] 
**receipts** | **float** |  | [optional] 
**refunded_individual_contributions** | **float** |  | [optional] 
**refunded_other_political_committee_contributions** | **float** |  | [optional] 
**refunded_political_party_committee_contributions** | **float** |  | [optional] 
**total_offsets_to_operating_expenditures** | **float** |  | [optional] 
**transaction_coverage_date** | **datetime** |  | [optional] 
**transfers_from_other_authorized_committee** | **float** |  | [optional] 
**transfers_to_other_authorized_committee** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.candidate_totals_detail_house_senate import CandidateTotalsDetailHouseSenate

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateTotalsDetailHouseSenate from a JSON string
candidate_totals_detail_house_senate_instance = CandidateTotalsDetailHouseSenate.from_json(json)
# print the JSON string representation of the object
print(CandidateTotalsDetailHouseSenate.to_json())

# convert the object into a dict
candidate_totals_detail_house_senate_dict = candidate_totals_detail_house_senate_instance.to_dict()
# create an instance of CandidateTotalsDetailHouseSenate from a dict
candidate_totals_detail_house_senate_from_dict = CandidateTotalsDetailHouseSenate.from_dict(candidate_totals_detail_house_senate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


