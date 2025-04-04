# PresidentialBySizePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[PresidentialBySize]**](PresidentialBySize.md) |  | [optional] 

## Example

```python
from openapi_client.models.presidential_by_size_page import PresidentialBySizePage

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialBySizePage from a JSON string
presidential_by_size_page_instance = PresidentialBySizePage.from_json(json)
# print the JSON string representation of the object
print(PresidentialBySizePage.to_json())

# convert the object into a dict
presidential_by_size_page_dict = presidential_by_size_page_instance.to_dict()
# create an instance of PresidentialBySizePage from a dict
presidential_by_size_page_from_dict = PresidentialBySizePage.from_dict(presidential_by_size_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


