# AuditCaseCategoryRelationPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[AuditCaseCategoryRelation]**](AuditCaseCategoryRelation.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_case_category_relation_page import AuditCaseCategoryRelationPage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCaseCategoryRelationPage from a JSON string
audit_case_category_relation_page_instance = AuditCaseCategoryRelationPage.from_json(json)
# print the JSON string representation of the object
print(AuditCaseCategoryRelationPage.to_json())

# convert the object into a dict
audit_case_category_relation_page_dict = audit_case_category_relation_page_instance.to_dict()
# create an instance of AuditCaseCategoryRelationPage from a dict
audit_case_category_relation_page_from_dict = AuditCaseCategoryRelationPage.from_dict(audit_case_category_relation_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


