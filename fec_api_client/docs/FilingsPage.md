# FilingsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[Filings]**](Filings.md) |  | [optional] 

## Example

```python
from openapi_client.models.filings_page import FilingsPage

# TODO update the JSON string below
json = "{}"
# create an instance of FilingsPage from a JSON string
filings_page_instance = FilingsPage.from_json(json)
# print the JSON string representation of the object
print(FilingsPage.to_json())

# convert the object into a dict
filings_page_dict = filings_page_instance.to_dict()
# create an instance of FilingsPage from a dict
filings_page_from_dict = FilingsPage.from_dict(filings_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


