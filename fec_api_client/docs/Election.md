# Election


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_election_year** | **int** |  | [optional] 
**candidate_id** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**candidate_pcc_id** | **str** | The candidate&#39;s primary campaign committee ID | [optional] 
**candidate_pcc_name** | **str** | The candidate&#39;s primary campaign committee name | [optional] 
**cash_on_hand_end_period** | **float** |  | [optional] 
**committee_ids** | **List[str]** |  | [optional] 
**coverage_end_date** | **date** |  | [optional] 
**incumbent_challenge_full** | **str** |  | [optional] 
**party_full** | **str** |  | [optional] 
**total_disbursements** | **float** |  | [optional] 
**total_receipts** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.election import Election

# TODO update the JSON string below
json = "{}"
# create an instance of Election from a JSON string
election_instance = Election.from_json(json)
# print the JSON string representation of the object
print(Election.to_json())

# convert the object into a dict
election_dict = election_instance.to_dict()
# create an instance of Election from a dict
election_from_dict = Election.from_dict(election_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


