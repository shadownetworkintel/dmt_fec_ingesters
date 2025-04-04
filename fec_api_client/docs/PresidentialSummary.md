# PresidentialSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_contributions_less_repayments** | **float** |  | [optional] 
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrats   -P00000003    Republicans  | [optional] 
**candidate_last_name** | **str** |  Candidate last name  | [optional] 
**candidate_name** | **str** | Name of candidate running for office | [optional] 
**candidate_party_affiliation** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**cash_on_hand_end** | **float** |  | [optional] 
**committee_designation** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**debts_owed_by_committee** | **float** |  | [optional] 
**disbursements_less_offsets** | **float** |  | [optional] 
**election_year** | **int** | Year of election | [optional] 
**exempt_legal_accounting_disbursement** | **float** |  | [optional] 
**federal_funds** | **float** |  | [optional] 
**fundraising_disbursements** | **float** |  | [optional] 
**individual_contributions_less_refunds** | **float** |  | [optional] 
**net_receipts** | **float** |  | [optional] 
**offsets_to_operating_expenditures** | **float** |  | [optional] 
**operating_expenditures** | **float** |  | [optional] 
**other_disbursements** | **float** |  | [optional] 
**pac_contributions_less_refunds** | **float** |  | [optional] 
**party_contributions_less_refunds** | **float** |  | [optional] 
**repayments_loans_made_by_candidate** | **float** |  | [optional] 
**repayments_other_loans** | **float** |  | [optional] 
**rounded_net_receipts** | **float** |  | [optional] 
**total_contribution_refunds** | **float** |  | [optional] 
**total_loan_repayments_made** | **float** |  | [optional] 
**transfers_from_affiliated_committees** | **float** |  | [optional] 
**transfers_to_other_authorized_committees** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.presidential_summary import PresidentialSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialSummary from a JSON string
presidential_summary_instance = PresidentialSummary.from_json(json)
# print the JSON string representation of the object
print(PresidentialSummary.to_json())

# convert the object into a dict
presidential_summary_dict = presidential_summary_instance.to_dict()
# create an instance of PresidentialSummary from a dict
presidential_summary_from_dict = PresidentialSummary.from_dict(presidential_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


