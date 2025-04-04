# CandidateSearchBaseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**office_sought** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.candidate_search_base_schema import CandidateSearchBaseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateSearchBaseSchema from a JSON string
candidate_search_base_schema_instance = CandidateSearchBaseSchema.from_json(json)
# print the JSON string representation of the object
print(CandidateSearchBaseSchema.to_json())

# convert the object into a dict
candidate_search_base_schema_dict = candidate_search_base_schema_instance.to_dict()
# create an instance of CandidateSearchBaseSchema from a dict
candidate_search_base_schema_from_dict = CandidateSearchBaseSchema.from_dict(candidate_search_base_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


