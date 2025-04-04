# CandidateTotalPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CandidateTotal]**](CandidateTotal.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_total_page import CandidateTotalPage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateTotalPage from a JSON string
candidate_total_page_instance = CandidateTotalPage.from_json(json)
# print the JSON string representation of the object
print(CandidateTotalPage.to_json())

# convert the object into a dict
candidate_total_page_dict = candidate_total_page_instance.to_dict()
# create an instance of CandidateTotalPage from a dict
candidate_total_page_from_dict = CandidateTotalPage.from_dict(candidate_total_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


