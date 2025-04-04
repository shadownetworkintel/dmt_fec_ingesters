# AuditCategoryRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_category_id** | **str** |  | [optional] 
**sub_category_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.audit_category_relation import AuditCategoryRelation

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCategoryRelation from a JSON string
audit_category_relation_instance = AuditCategoryRelation.from_json(json)
# print the JSON string representation of the object
print(AuditCategoryRelation.to_json())

# convert the object into a dict
audit_category_relation_dict = audit_category_relation_instance.to_dict()
# create an instance of AuditCategoryRelation from a dict
audit_category_relation_from_dict = AuditCategoryRelation.from_dict(audit_category_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


