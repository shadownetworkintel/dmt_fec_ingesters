# AuditCategoryRelationPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[AuditCategoryRelation]**](AuditCategoryRelation.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_category_relation_page import AuditCategoryRelationPage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCategoryRelationPage from a JSON string
audit_category_relation_page_instance = AuditCategoryRelationPage.from_json(json)
# print the JSON string representation of the object
print(AuditCategoryRelationPage.to_json())

# convert the object into a dict
audit_category_relation_page_dict = audit_category_relation_page_instance.to_dict()
# create an instance of AuditCategoryRelationPage from a dict
audit_category_relation_page_from_dict = AuditCategoryRelationPage.from_dict(audit_category_relation_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


