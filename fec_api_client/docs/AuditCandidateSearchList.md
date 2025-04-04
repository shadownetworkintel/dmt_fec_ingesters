# AuditCandidateSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AuditCandidateSearch]**](AuditCandidateSearch.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_candidate_search_list import AuditCandidateSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCandidateSearchList from a JSON string
audit_candidate_search_list_instance = AuditCandidateSearchList.from_json(json)
# print the JSON string representation of the object
print(AuditCandidateSearchList.to_json())

# convert the object into a dict
audit_candidate_search_list_dict = audit_candidate_search_list_instance.to_dict()
# create an instance of AuditCandidateSearchList from a dict
audit_candidate_search_list_from_dict = AuditCandidateSearchList.from_dict(audit_candidate_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


