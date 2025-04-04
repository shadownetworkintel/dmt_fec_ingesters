# CandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[Candidate]**](Candidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_page import CandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidatePage from a JSON string
candidate_page_instance = CandidatePage.from_json(json)
# print the JSON string representation of the object
print(CandidatePage.to_json())

# convert the object into a dict
candidate_page_dict = candidate_page_instance.to_dict()
# create an instance of CandidatePage from a dict
candidate_page_from_dict = CandidatePage.from_dict(candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


