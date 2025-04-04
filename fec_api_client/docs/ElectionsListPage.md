# ElectionsListPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ElectionsList]**](ElectionsList.md) |  | [optional] 

## Example

```python
from openapi_client.models.elections_list_page import ElectionsListPage

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionsListPage from a JSON string
elections_list_page_instance = ElectionsListPage.from_json(json)
# print the JSON string representation of the object
print(ElectionsListPage.to_json())

# convert the object into a dict
elections_list_page_dict = elections_list_page_instance.to_dict()
# create an instance of ElectionsListPage from a dict
elections_list_page_from_dict = ElectionsListPage.from_dict(elections_list_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


