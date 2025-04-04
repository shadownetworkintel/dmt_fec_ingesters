# CandidateSearchListSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CandidateSearchBaseSchema]**](CandidateSearchBaseSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_search_list_schema import CandidateSearchListSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateSearchListSchema from a JSON string
candidate_search_list_schema_instance = CandidateSearchListSchema.from_json(json)
# print the JSON string representation of the object
print(CandidateSearchListSchema.to_json())

# convert the object into a dict
candidate_search_list_schema_dict = candidate_search_list_schema_instance.to_dict()
# create an instance of CandidateSearchListSchema from a dict
candidate_search_list_schema_from_dict = CandidateSearchListSchema.from_dict(candidate_search_list_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


