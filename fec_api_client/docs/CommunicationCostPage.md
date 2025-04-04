# CommunicationCostPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommunicationCost]**](CommunicationCost.md) |  | [optional] 

## Example

```python
from openapi_client.models.communication_cost_page import CommunicationCostPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCostPage from a JSON string
communication_cost_page_instance = CommunicationCostPage.from_json(json)
# print the JSON string representation of the object
print(CommunicationCostPage.to_json())

# convert the object into a dict
communication_cost_page_dict = communication_cost_page_instance.to_dict()
# create an instance of CommunicationCostPage from a dict
communication_cost_page_from_dict = CommunicationCostPage.from_dict(communication_cost_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


