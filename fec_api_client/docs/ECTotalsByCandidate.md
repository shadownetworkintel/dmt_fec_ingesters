# ECTotalsByCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.ec_totals_by_candidate import ECTotalsByCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of ECTotalsByCandidate from a JSON string
ec_totals_by_candidate_instance = ECTotalsByCandidate.from_json(json)
# print the JSON string representation of the object
print(ECTotalsByCandidate.to_json())

# convert the object into a dict
ec_totals_by_candidate_dict = ec_totals_by_candidate_instance.to_dict()
# create an instance of ECTotalsByCandidate from a dict
ec_totals_by_candidate_from_dict = ECTotalsByCandidate.from_dict(ec_totals_by_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


