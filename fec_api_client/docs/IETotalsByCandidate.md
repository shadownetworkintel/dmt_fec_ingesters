# IETotalsByCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**support_oppose_indicator** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.ie_totals_by_candidate import IETotalsByCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of IETotalsByCandidate from a JSON string
ie_totals_by_candidate_instance = IETotalsByCandidate.from_json(json)
# print the JSON string representation of the object
print(IETotalsByCandidate.to_json())

# convert the object into a dict
ie_totals_by_candidate_dict = ie_totals_by_candidate_instance.to_dict()
# create an instance of IETotalsByCandidate from a dict
ie_totals_by_candidate_from_dict = IETotalsByCandidate.from_dict(ie_totals_by_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


