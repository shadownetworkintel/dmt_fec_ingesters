# PresidentialSummaryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[PresidentialSummary]**](PresidentialSummary.md) |  | [optional] 

## Example

```python
from openapi_client.models.presidential_summary_page import PresidentialSummaryPage

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialSummaryPage from a JSON string
presidential_summary_page_instance = PresidentialSummaryPage.from_json(json)
# print the JSON string representation of the object
print(PresidentialSummaryPage.to_json())

# convert the object into a dict
presidential_summary_page_dict = presidential_summary_page_instance.to_dict()
# create an instance of PresidentialSummaryPage from a dict
presidential_summary_page_from_dict = PresidentialSummaryPage.from_dict(presidential_summary_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


