# CandidateSearchPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CandidateSearch]**](CandidateSearch.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_search_page import CandidateSearchPage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateSearchPage from a JSON string
candidate_search_page_instance = CandidateSearchPage.from_json(json)
# print the JSON string representation of the object
print(CandidateSearchPage.to_json())

# convert the object into a dict
candidate_search_page_dict = candidate_search_page_instance.to_dict()
# create an instance of CandidateSearchPage from a dict
candidate_search_page_from_dict = CandidateSearchPage.from_dict(candidate_search_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


