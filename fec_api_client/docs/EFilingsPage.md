# EFilingsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[EFilings]**](EFilings.md) |  | [optional] 

## Example

```python
from openapi_client.models.e_filings_page import EFilingsPage

# TODO update the JSON string below
json = "{}"
# create an instance of EFilingsPage from a JSON string
e_filings_page_instance = EFilingsPage.from_json(json)
# print the JSON string representation of the object
print(EFilingsPage.to_json())

# convert the object into a dict
e_filings_page_dict = e_filings_page_instance.to_dict()
# create an instance of EFilingsPage from a dict
e_filings_page_from_dict = EFilingsPage.from_dict(e_filings_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


