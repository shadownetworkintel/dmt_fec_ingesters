# ECAggregates


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
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.ec_aggregates import ECAggregates

# TODO update the JSON string below
json = "{}"
# create an instance of ECAggregates from a JSON string
ec_aggregates_instance = ECAggregates.from_json(json)
# print the JSON string representation of the object
print(ECAggregates.to_json())

# convert the object into a dict
ec_aggregates_dict = ec_aggregates_instance.to_dict()
# create an instance of ECAggregates from a dict
ec_aggregates_from_dict = ECAggregates.from_dict(ec_aggregates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


