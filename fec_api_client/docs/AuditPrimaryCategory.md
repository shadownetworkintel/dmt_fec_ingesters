# AuditPrimaryCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_category_id** | **str** |  | [optional] 
**primary_category_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.audit_primary_category import AuditPrimaryCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AuditPrimaryCategory from a JSON string
audit_primary_category_instance = AuditPrimaryCategory.from_json(json)
# print the JSON string representation of the object
print(AuditPrimaryCategory.to_json())

# convert the object into a dict
audit_primary_category_dict = audit_primary_category_instance.to_dict()
# create an instance of AuditPrimaryCategory from a dict
audit_primary_category_from_dict = AuditPrimaryCategory.from_dict(audit_primary_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


