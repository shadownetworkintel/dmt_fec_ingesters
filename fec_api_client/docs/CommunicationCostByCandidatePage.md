# CommunicationCostByCandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommunicationCostByCandidate]**](CommunicationCostByCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.communication_cost_by_candidate_page import CommunicationCostByCandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCostByCandidatePage from a JSON string
communication_cost_by_candidate_page_instance = CommunicationCostByCandidatePage.from_json(json)
# print the JSON string representation of the object
print(CommunicationCostByCandidatePage.to_json())

# convert the object into a dict
communication_cost_by_candidate_page_dict = communication_cost_by_candidate_page_instance.to_dict()
# create an instance of CommunicationCostByCandidatePage from a dict
communication_cost_by_candidate_page_from_dict = CommunicationCostByCandidatePage.from_dict(communication_cost_by_candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


