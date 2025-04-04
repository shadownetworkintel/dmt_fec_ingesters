# ElectioneeringPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**SeekInfo**](SeekInfo.md) |  | [optional] 
**results** | [**List[Electioneering]**](Electioneering.md) |  | [optional] 

## Example

```python
from openapi_client.models.electioneering_page import ElectioneeringPage

# TODO update the JSON string below
json = "{}"
# create an instance of ElectioneeringPage from a JSON string
electioneering_page_instance = ElectioneeringPage.from_json(json)
# print the JSON string representation of the object
print(ElectioneeringPage.to_json())

# convert the object into a dict
electioneering_page_dict = electioneering_page_instance.to_dict()
# create an instance of ElectioneeringPage from a dict
electioneering_page_from_dict = ElectioneeringPage.from_dict(electioneering_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


