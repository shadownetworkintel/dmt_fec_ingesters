# ElectionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**disbursements** | **float** |  | [optional] 
**independent_expenditures** | **float** |  | [optional] 
**receipts** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.election_summary import ElectionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionSummary from a JSON string
election_summary_instance = ElectionSummary.from_json(json)
# print the JSON string representation of the object
print(ElectionSummary.to_json())

# convert the object into a dict
election_summary_dict = election_summary_instance.to_dict()
# create an instance of ElectionSummary from a dict
election_summary_from_dict = ElectionSummary.from_dict(election_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


