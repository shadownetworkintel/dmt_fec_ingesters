# AuditCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_case_id** | **str** |  | [optional] 
**audit_id** | **int** |  | [optional] 
**candidate_id** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**committee_description** | **str** |  | [optional] 
**committee_designation** | **str** |  | [optional] 
**committee_id** | **str** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**committee_type** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**far_release_date** | **date** |  | [optional] 
**link_to_report** | **str** |  | [optional] 
**primary_category_list** | [**List[AuditCaseCategoryRelation]**](AuditCaseCategoryRelation.md) |  | [optional] 

## Example

```python
from openapi_client.models.audit_case import AuditCase

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCase from a JSON string
audit_case_instance = AuditCase.from_json(json)
# print the JSON string representation of the object
print(AuditCase.to_json())

# convert the object into a dict
audit_case_dict = audit_case_instance.to_dict()
# create an instance of AuditCase from a dict
audit_case_from_dict = AuditCase.from_dict(audit_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


