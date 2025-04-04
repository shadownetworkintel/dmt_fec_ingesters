# AuditCasePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[AuditCase]**](AuditCase.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_case_page import AuditCasePage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCasePage from a JSON string
audit_case_page_instance = AuditCasePage.from_json(json)
# print the JSON string representation of the object
print(AuditCasePage.to_json())

# convert the object into a dict
audit_case_page_dict = audit_case_page_instance.to_dict()
# create an instance of AuditCasePage from a dict
audit_case_page_from_dict = AuditCasePage.from_dict(audit_case_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


