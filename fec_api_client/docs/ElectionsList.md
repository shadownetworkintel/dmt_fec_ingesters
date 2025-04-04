# ElectionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle** | **int** |  | [optional] 
**district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**state** | **str** | US state or territory | [optional] 

## Example

```python
from openapi_client.models.elections_list import ElectionsList

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionsList from a JSON string
elections_list_instance = ElectionsList.from_json(json)
# print the JSON string representation of the object
print(ElectionsList.to_json())

# convert the object into a dict
elections_list_dict = elections_list_instance.to_dict()
# create an instance of ElectionsList from a dict
elections_list_from_dict = ElectionsList.from_dict(elections_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


