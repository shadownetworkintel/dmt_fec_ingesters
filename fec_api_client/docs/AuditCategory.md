# AuditCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_category_id** | **str** |  | [optional] 
**primary_category_name** | **str** |  | [optional] 
**sub_category_list** | [**List[AuditCategoryRelation]**](AuditCategoryRelation.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_category import AuditCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCategory from a JSON string
audit_category_instance = AuditCategory.from_json(json)
# print the JSON string representation of the object
print(AuditCategory.to_json())

# convert the object into a dict
audit_category_dict = audit_category_instance.to_dict()
# create an instance of AuditCategory from a dict
audit_category_from_dict = AuditCategory.from_dict(audit_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


