# ElectioneeringByCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**committee_id** | **str** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**count** | **int** |  Number of records making up the total.  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.electioneering_by_candidate import ElectioneeringByCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of ElectioneeringByCandidate from a JSON string
electioneering_by_candidate_instance = ElectioneeringByCandidate.from_json(json)
# print the JSON string representation of the object
print(ElectioneeringByCandidate.to_json())

# convert the object into a dict
electioneering_by_candidate_dict = electioneering_by_candidate_instance.to_dict()
# create an instance of ElectioneeringByCandidate from a dict
electioneering_by_candidate_from_dict = ElectioneeringByCandidate.from_dict(electioneering_by_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


