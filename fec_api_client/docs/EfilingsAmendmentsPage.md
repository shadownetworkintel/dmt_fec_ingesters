# EfilingsAmendmentsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[EfilingsAmendments]**](EfilingsAmendments.md) |  | [optional] 

## Example

```python
from openapi_client.models.efilings_amendments_page import EfilingsAmendmentsPage

# TODO update the JSON string below
json = "{}"
# create an instance of EfilingsAmendmentsPage from a JSON string
efilings_amendments_page_instance = EfilingsAmendmentsPage.from_json(json)
# print the JSON string representation of the object
print(EfilingsAmendmentsPage.to_json())

# convert the object into a dict
efilings_amendments_page_dict = efilings_amendments_page_instance.to_dict()
# create an instance of EfilingsAmendmentsPage from a dict
efilings_amendments_page_from_dict = EfilingsAmendmentsPage.from_dict(efilings_amendments_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


