# BaseF3XFilingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[BaseF3XFiling]**](BaseF3XFiling.md) |  | [optional] 

## Example

```python
from openapi_client.models.base_f3_x_filing_page import BaseF3XFilingPage

# TODO update the JSON string below
json = "{}"
# create an instance of BaseF3XFilingPage from a JSON string
base_f3_x_filing_page_instance = BaseF3XFilingPage.from_json(json)
# print the JSON string representation of the object
print(BaseF3XFilingPage.to_json())

# convert the object into a dict
base_f3_x_filing_page_dict = base_f3_x_filing_page_instance.to_dict()
# create an instance of BaseF3XFilingPage from a dict
base_f3_x_filing_page_from_dict = BaseF3XFilingPage.from_dict(base_f3_x_filing_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


