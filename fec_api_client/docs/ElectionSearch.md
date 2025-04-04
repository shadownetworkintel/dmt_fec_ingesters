# ElectionSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_status** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**district** | **str** |  | [optional] 
**incumbent_id** | **str** |  | [optional] 
**incumbent_name** | **str** |  | [optional] 
**office** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.election_search import ElectionSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionSearch from a JSON string
election_search_instance = ElectionSearch.from_json(json)
# print the JSON string representation of the object
print(ElectionSearch.to_json())

# convert the object into a dict
election_search_dict = election_search_instance.to_dict()
# create an instance of ElectionSearch from a dict
election_search_from_dict = ElectionSearch.from_dict(election_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


