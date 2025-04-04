# CandidateFlagsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CandidateFlags]**](CandidateFlags.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_flags_page import CandidateFlagsPage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateFlagsPage from a JSON string
candidate_flags_page_instance = CandidateFlagsPage.from_json(json)
# print the JSON string representation of the object
print(CandidateFlagsPage.to_json())

# convert the object into a dict
candidate_flags_page_dict = candidate_flags_page_instance.to_dict()
# create an instance of CandidateFlagsPage from a dict
candidate_flags_page_from_dict = CandidateFlagsPage.from_dict(candidate_flags_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


