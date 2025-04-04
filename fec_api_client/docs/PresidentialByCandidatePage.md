# PresidentialByCandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[PresidentialByCandidate]**](PresidentialByCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.presidential_by_candidate_page import PresidentialByCandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialByCandidatePage from a JSON string
presidential_by_candidate_page_instance = PresidentialByCandidatePage.from_json(json)
# print the JSON string representation of the object
print(PresidentialByCandidatePage.to_json())

# convert the object into a dict
presidential_by_candidate_page_dict = presidential_by_candidate_page_instance.to_dict()
# create an instance of PresidentialByCandidatePage from a dict
presidential_by_candidate_page_from_dict = PresidentialByCandidatePage.from_dict(presidential_by_candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


