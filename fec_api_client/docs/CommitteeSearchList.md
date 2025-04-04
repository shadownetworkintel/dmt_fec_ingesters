# CommitteeSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CommitteeSearch]**](CommitteeSearch.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_search_list import CommitteeSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeSearchList from a JSON string
committee_search_list_instance = CommitteeSearchList.from_json(json)
# print the JSON string representation of the object
print(CommitteeSearchList.to_json())

# convert the object into a dict
committee_search_list_dict = committee_search_list_instance.to_dict()
# create an instance of CommitteeSearchList from a dict
committee_search_list_from_dict = CommitteeSearchList.from_dict(committee_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


