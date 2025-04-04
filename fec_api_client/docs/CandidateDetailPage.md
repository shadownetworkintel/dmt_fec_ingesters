# CandidateDetailPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CandidateDetail]**](CandidateDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.candidate_detail_page import CandidateDetailPage

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateDetailPage from a JSON string
candidate_detail_page_instance = CandidateDetailPage.from_json(json)
# print the JSON string representation of the object
print(CandidateDetailPage.to_json())

# convert the object into a dict
candidate_detail_page_dict = candidate_detail_page_instance.to_dict()
# create an instance of CandidateDetailPage from a dict
candidate_detail_page_from_dict = CandidateDetailPage.from_dict(candidate_detail_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


