# PresidentialByState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrats   -P00000003    Republicans  | [optional] 
**contribution_receipt_amount** | **float** |  | [optional] 
**contribution_state** | **str** | State of contributor | [optional] 
**election_year** | **int** | Year of election | [optional] 

## Example

```python
from openapi_client.models.presidential_by_state import PresidentialByState

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialByState from a JSON string
presidential_by_state_instance = PresidentialByState.from_json(json)
# print the JSON string representation of the object
print(PresidentialByState.to_json())

# convert the object into a dict
presidential_by_state_dict = presidential_by_state_instance.to_dict()
# create an instance of PresidentialByState from a dict
presidential_by_state_from_dict = PresidentialByState.from_dict(presidential_by_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


