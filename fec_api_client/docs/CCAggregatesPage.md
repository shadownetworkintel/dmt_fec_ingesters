# CCAggregatesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CCAggregates]**](CCAggregates.md) |  | [optional] 

## Example

```python
from openapi_client.models.cc_aggregates_page import CCAggregatesPage

# TODO update the JSON string below
json = "{}"
# create an instance of CCAggregatesPage from a JSON string
cc_aggregates_page_instance = CCAggregatesPage.from_json(json)
# print the JSON string representation of the object
print(CCAggregatesPage.to_json())

# convert the object into a dict
cc_aggregates_page_dict = cc_aggregates_page_instance.to_dict()
# create an instance of CCAggregatesPage from a dict
cc_aggregates_page_from_dict = CCAggregatesPage.from_dict(cc_aggregates_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


