# CandidateFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
**federal_funds_flag** | **bool** | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
**has_raised_funds** | **bool** | A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 

## Example

```python
from openapi_client.models.candidate_flags import CandidateFlags

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateFlags from a JSON string
candidate_flags_instance = CandidateFlags.from_json(json)
# print the JSON string representation of the object
print(CandidateFlags.to_json())

# convert the object into a dict
candidate_flags_dict = candidate_flags_instance.to_dict()
# create an instance of CandidateFlags from a dict
candidate_flags_from_dict = CandidateFlags.from_dict(candidate_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


