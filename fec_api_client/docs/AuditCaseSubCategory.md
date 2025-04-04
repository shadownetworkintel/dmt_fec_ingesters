# AuditCaseSubCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_category_id** | **str** |  | [optional] 
**sub_category_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.audit_case_sub_category import AuditCaseSubCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCaseSubCategory from a JSON string
audit_case_sub_category_instance = AuditCaseSubCategory.from_json(json)
# print the JSON string representation of the object
print(AuditCaseSubCategory.to_json())

# convert the object into a dict
audit_case_sub_category_dict = audit_case_sub_category_instance.to_dict()
# create an instance of AuditCaseSubCategory from a dict
audit_case_sub_category_from_dict = AuditCaseSubCategory.from_dict(audit_case_sub_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


