# AuditCommitteeSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AuditCommitteeSearch]**](AuditCommitteeSearch.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_committee_search_list import AuditCommitteeSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCommitteeSearchList from a JSON string
audit_committee_search_list_instance = AuditCommitteeSearchList.from_json(json)
# print the JSON string representation of the object
print(AuditCommitteeSearchList.to_json())

# convert the object into a dict
audit_committee_search_list_dict = audit_committee_search_list_instance.to_dict()
# create an instance of AuditCommitteeSearchList from a dict
audit_committee_search_list_from_dict = AuditCommitteeSearchList.from_dict(audit_committee_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


