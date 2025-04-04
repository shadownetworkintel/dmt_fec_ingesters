# AuditCaseSubCategoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[AuditCaseSubCategory]**](AuditCaseSubCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_case_sub_category_page import AuditCaseSubCategoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCaseSubCategoryPage from a JSON string
audit_case_sub_category_page_instance = AuditCaseSubCategoryPage.from_json(json)
# print the JSON string representation of the object
print(AuditCaseSubCategoryPage.to_json())

# convert the object into a dict
audit_case_sub_category_page_dict = audit_case_sub_category_page_instance.to_dict()
# create an instance of AuditCaseSubCategoryPage from a dict
audit_case_sub_category_page_from_dict = AuditCaseSubCategoryPage.from_dict(audit_case_sub_category_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


