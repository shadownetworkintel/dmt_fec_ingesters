# AuditCaseCategoryRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_category_id** | **str** |  | [optional] 
**primary_category_name** | **str** |  | [optional] 
**sub_category_list** | [**List[AuditCaseSubCategory]**](AuditCaseSubCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_case_category_relation import AuditCaseCategoryRelation

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCaseCategoryRelation from a JSON string
audit_case_category_relation_instance = AuditCaseCategoryRelation.from_json(json)
# print the JSON string representation of the object
print(AuditCaseCategoryRelation.to_json())

# convert the object into a dict
audit_case_category_relation_dict = audit_case_category_relation_instance.to_dict()
# create an instance of AuditCaseCategoryRelation from a dict
audit_case_category_relation_from_dict = AuditCaseCategoryRelation.from_dict(audit_case_category_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


