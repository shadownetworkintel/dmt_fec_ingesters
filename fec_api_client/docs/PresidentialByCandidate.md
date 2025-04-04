# PresidentialByCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrats   -P00000003    Republicans  | [optional] 
**candidate_last_name** | **str** |  Candidate last name  | [optional] 
**candidate_party_affiliation** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**contributor_state** | **str** | State of contributor | [optional] 
**election_year** | **int** | Year of election | [optional] 
**net_receipts** | **float** |  | [optional] 
**rounded_net_receipts** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.presidential_by_candidate import PresidentialByCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialByCandidate from a JSON string
presidential_by_candidate_instance = PresidentialByCandidate.from_json(json)
# print the JSON string representation of the object
print(PresidentialByCandidate.to_json())

# convert the object into a dict
presidential_by_candidate_dict = presidential_by_candidate_instance.to_dict()
# create an instance of PresidentialByCandidate from a dict
presidential_by_candidate_from_dict = PresidentialByCandidate.from_dict(presidential_by_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


