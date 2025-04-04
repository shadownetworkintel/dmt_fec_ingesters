# AuditPrimaryCategoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[AuditPrimaryCategory]**](AuditPrimaryCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_primary_category_page import AuditPrimaryCategoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditPrimaryCategoryPage from a JSON string
audit_primary_category_page_instance = AuditPrimaryCategoryPage.from_json(json)
# print the JSON string representation of the object
print(AuditPrimaryCategoryPage.to_json())

# convert the object into a dict
audit_primary_category_page_dict = audit_primary_category_page_instance.to_dict()
# create an instance of AuditPrimaryCategoryPage from a dict
audit_primary_category_page_from_dict = AuditPrimaryCategoryPage.from_dict(audit_primary_category_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


