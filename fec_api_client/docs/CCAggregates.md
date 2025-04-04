# CCAggregates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate** | **object** |  | [optional] 
**candidate_id** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**committee** | **object** |  | [optional] 
**committee_id** | **str** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**cycle** | **int** |  | [optional] 
**support_oppose_indicator** | **str** | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.cc_aggregates import CCAggregates

# TODO update the JSON string below
json = "{}"
# create an instance of CCAggregates from a JSON string
cc_aggregates_instance = CCAggregates.from_json(json)
# print the JSON string representation of the object
print(CCAggregates.to_json())

# convert the object into a dict
cc_aggregates_dict = cc_aggregates_instance.to_dict()
# create an instance of CCAggregates from a dict
cc_aggregates_from_dict = CCAggregates.from_dict(cc_aggregates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


