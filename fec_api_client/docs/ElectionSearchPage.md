# ElectionSearchPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ElectionSearch]**](ElectionSearch.md) |  | [optional] 

## Example

```python
from openapi_client.models.election_search_page import ElectionSearchPage

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionSearchPage from a JSON string
election_search_page_instance = ElectionSearchPage.from_json(json)
# print the JSON string representation of the object
print(ElectionSearchPage.to_json())

# convert the object into a dict
election_search_page_dict = election_search_page_instance.to_dict()
# create an instance of ElectionSearchPage from a dict
election_search_page_from_dict = ElectionSearchPage.from_dict(election_search_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


