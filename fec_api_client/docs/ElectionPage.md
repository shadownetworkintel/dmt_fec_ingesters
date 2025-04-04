# ElectionPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[Election]**](Election.md) |  | [optional] 

## Example

```python
from openapi_client.models.election_page import ElectionPage

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionPage from a JSON string
election_page_instance = ElectionPage.from_json(json)
# print the JSON string representation of the object
print(ElectionPage.to_json())

# convert the object into a dict
election_page_dict = election_page_instance.to_dict()
# create an instance of ElectionPage from a dict
election_page_from_dict = ElectionPage.from_dict(election_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


