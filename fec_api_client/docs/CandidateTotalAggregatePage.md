# CandidateTotalAggregatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CandidateTotalAggregate]**](CandidateTotalAggregate.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_total_aggregate_page import CandidateTotalAggregatePage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateTotalAggregatePage from a JSON string
candidate_total_aggregate_page_instance = CandidateTotalAggregatePage.from_json(json)
# print the JSON string representation of the object
print(CandidateTotalAggregatePage.to_json())

# convert the object into a dict
candidate_total_aggregate_page_dict = candidate_total_aggregate_page_instance.to_dict()
# create an instance of CandidateTotalAggregatePage from a dict
candidate_total_aggregate_page_from_dict = CandidateTotalAggregatePage.from_dict(candidate_total_aggregate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


