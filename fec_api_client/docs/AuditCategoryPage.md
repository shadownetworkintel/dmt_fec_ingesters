# AuditCategoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[AuditCategory]**](AuditCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_category_page import AuditCategoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCategoryPage from a JSON string
audit_category_page_instance = AuditCategoryPage.from_json(json)
# print the JSON string representation of the object
print(AuditCategoryPage.to_json())

# convert the object into a dict
audit_category_page_dict = audit_category_page_instance.to_dict()
# create an instance of AuditCategoryPage from a dict
audit_category_page_from_dict = AuditCategoryPage.from_dict(audit_category_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


