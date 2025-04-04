# TotalByOfficeByPartyPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[TotalByOfficeByParty]**](TotalByOfficeByParty.md) |  | [optional] 

## Example

```python
from openapi_client.models.total_by_office_by_party_page import TotalByOfficeByPartyPage

# TODO update the JSON string below
json = "{}"
# create an instance of TotalByOfficeByPartyPage from a JSON string
total_by_office_by_party_page_instance = TotalByOfficeByPartyPage.from_json(json)
# print the JSON string representation of the object
print(TotalByOfficeByPartyPage.to_json())

# convert the object into a dict
total_by_office_by_party_page_dict = total_by_office_by_party_page_instance.to_dict()
# create an instance of TotalByOfficeByPartyPage from a dict
total_by_office_by_party_page_from_dict = TotalByOfficeByPartyPage.from_dict(total_by_office_by_party_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


