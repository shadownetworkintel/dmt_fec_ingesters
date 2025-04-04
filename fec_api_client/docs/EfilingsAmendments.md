# EfilingsAmendments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_chain** | **List[int]** |  | [optional] 
**depth** | **float** |  | [optional] 
**file_number** | **int** | Filing ID number | [optional] 
**last** | **float** |  | [optional] 
**longest_chain** | **float** |  | [optional] 
**most_recent_filing** | **float** |  | [optional] 
**previous_file_number** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.efilings_amendments import EfilingsAmendments

# TODO update the JSON string below
json = "{}"
# create an instance of EfilingsAmendments from a JSON string
efilings_amendments_instance = EfilingsAmendments.from_json(json)
# print the JSON string representation of the object
print(EfilingsAmendments.to_json())

# convert the object into a dict
efilings_amendments_dict = efilings_amendments_instance.to_dict()
# create an instance of EfilingsAmendments from a dict
efilings_amendments_from_dict = EfilingsAmendments.from_dict(efilings_amendments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


