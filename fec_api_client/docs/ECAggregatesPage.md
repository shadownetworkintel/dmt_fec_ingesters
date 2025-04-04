# ECAggregatesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ECAggregates]**](ECAggregates.md) |  | [optional] 

## Example

```python
from openapi_client.models.ec_aggregates_page import ECAggregatesPage

# TODO update the JSON string below
json = "{}"
# create an instance of ECAggregatesPage from a JSON string
ec_aggregates_page_instance = ECAggregatesPage.from_json(json)
# print the JSON string representation of the object
print(ECAggregatesPage.to_json())

# convert the object into a dict
ec_aggregates_page_dict = ec_aggregates_page_instance.to_dict()
# create an instance of ECAggregatesPage from a dict
ec_aggregates_page_from_dict = ECAggregatesPage.from_dict(ec_aggregates_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


