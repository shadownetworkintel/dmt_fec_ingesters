# PresidentialByStatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[PresidentialByState]**](PresidentialByState.md) |  | [optional] 

## Example

```python
from openapi_client.models.presidential_by_state_page import PresidentialByStatePage

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialByStatePage from a JSON string
presidential_by_state_page_instance = PresidentialByStatePage.from_json(json)
# print the JSON string representation of the object
print(PresidentialByStatePage.to_json())

# convert the object into a dict
presidential_by_state_page_dict = presidential_by_state_page_instance.to_dict()
# create an instance of PresidentialByStatePage from a dict
presidential_by_state_page_from_dict = PresidentialByStatePage.from_dict(presidential_by_state_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


