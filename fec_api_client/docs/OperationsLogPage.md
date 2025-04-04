# OperationsLogPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[OperationsLog]**](OperationsLog.md) |  | [optional] 

## Example

```python
from openapi_client.models.operations_log_page import OperationsLogPage

# TODO update the JSON string below
json = "{}"
# create an instance of OperationsLogPage from a JSON string
operations_log_page_instance = OperationsLogPage.from_json(json)
# print the JSON string representation of the object
print(OperationsLogPage.to_json())

# convert the object into a dict
operations_log_page_dict = operations_log_page_instance.to_dict()
# create an instance of OperationsLogPage from a dict
operations_log_page_from_dict = OperationsLogPage.from_dict(operations_log_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


