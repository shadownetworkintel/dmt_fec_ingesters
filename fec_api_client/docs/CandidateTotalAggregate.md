# CandidateTotalAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**district** | **str** |  | [optional] 
**district_number** | **int** |  | [optional] 
**election_year** | **int** |  | [optional] 
**office** | **str** |  | [optional] 
**party** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_full** | **str** |  | [optional] 
**total_cash_on_hand_end_period** | **float** |  | [optional] 
**total_debts_owed_by_committee** | **float** |  | [optional] 
**total_disbursements** | **float** |  | [optional] 
**total_individual_itemized_contributions** | **float** |  | [optional] 
**total_other_political_committee_contributions** | **float** |  | [optional] 
**total_receipts** | **float** |  | [optional] 
**total_transfers_from_other_authorized_committee** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.candidate_total_aggregate import CandidateTotalAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateTotalAggregate from a JSON string
candidate_total_aggregate_instance = CandidateTotalAggregate.from_json(json)
# print the JSON string representation of the object
print(CandidateTotalAggregate.to_json())

# convert the object into a dict
candidate_total_aggregate_dict = candidate_total_aggregate_instance.to_dict()
# create an instance of CandidateTotalAggregate from a dict
candidate_total_aggregate_from_dict = CandidateTotalAggregate.from_dict(candidate_total_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


