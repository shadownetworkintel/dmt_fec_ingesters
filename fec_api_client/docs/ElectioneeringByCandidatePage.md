# ElectioneeringByCandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ElectioneeringByCandidate]**](ElectioneeringByCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.electioneering_by_candidate_page import ElectioneeringByCandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of ElectioneeringByCandidatePage from a JSON string
electioneering_by_candidate_page_instance = ElectioneeringByCandidatePage.from_json(json)
# print the JSON string representation of the object
print(ElectioneeringByCandidatePage.to_json())

# convert the object into a dict
electioneering_by_candidate_page_dict = electioneering_by_candidate_page_instance.to_dict()
# create an instance of ElectioneeringByCandidatePage from a dict
electioneering_by_candidate_page_from_dict = ElectioneeringByCandidatePage.from_dict(electioneering_by_candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


