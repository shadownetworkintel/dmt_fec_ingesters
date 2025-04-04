# BaseF3PFilingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[BaseF3PFiling]**](BaseF3PFiling.md) |  | [optional] 

## Example

```python
from openapi_client.models.base_f3_p_filing_page import BaseF3PFilingPage

# TODO update the JSON string below
json = "{}"
# create an instance of BaseF3PFilingPage from a JSON string
base_f3_p_filing_page_instance = BaseF3PFilingPage.from_json(json)
# print the JSON string representation of the object
print(BaseF3PFilingPage.to_json())

# convert the object into a dict
base_f3_p_filing_page_dict = base_f3_p_filing_page_instance.to_dict()
# create an instance of BaseF3PFilingPage from a dict
base_f3_p_filing_page_from_dict = BaseF3PFilingPage.from_dict(base_f3_p_filing_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


