# CommitteeSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.committee_search import CommitteeSearch

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeSearch from a JSON string
committee_search_instance = CommitteeSearch.from_json(json)
# print the JSON string representation of the object
print(CommitteeSearch.to_json())

# convert the object into a dict
committee_search_dict = committee_search_instance.to_dict()
# create an instance of CommitteeSearch from a dict
committee_search_from_dict = CommitteeSearch.from_dict(committee_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


