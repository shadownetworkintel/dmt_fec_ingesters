# CCTotalsByCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**support_oppose_indicator** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.cc_totals_by_candidate import CCTotalsByCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of CCTotalsByCandidate from a JSON string
cc_totals_by_candidate_instance = CCTotalsByCandidate.from_json(json)
# print the JSON string representation of the object
print(CCTotalsByCandidate.to_json())

# convert the object into a dict
cc_totals_by_candidate_dict = cc_totals_by_candidate_instance.to_dict()
# create an instance of CCTotalsByCandidate from a dict
cc_totals_by_candidate_from_dict = CCTotalsByCandidate.from_dict(cc_totals_by_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


