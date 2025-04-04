# PacSponsorCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sponsor_candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**sponsor_candidate_name** | **str** | Name of candidate running for office | [optional] 

## Example

```python
from openapi_client.models.pac_sponsor_candidate import PacSponsorCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of PacSponsorCandidate from a JSON string
pac_sponsor_candidate_instance = PacSponsorCandidate.from_json(json)
# print the JSON string representation of the object
print(PacSponsorCandidate.to_json())

# convert the object into a dict
pac_sponsor_candidate_dict = pac_sponsor_candidate_instance.to_dict()
# create an instance of PacSponsorCandidate from a dict
pac_sponsor_candidate_from_dict = PacSponsorCandidate.from_dict(pac_sponsor_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


