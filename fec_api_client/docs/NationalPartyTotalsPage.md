# NationalPartyTotalsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[NationalPartyTotals]**](NationalPartyTotals.md) |  | [optional] 

## Example

```python
from openapi_client.models.national_party_totals_page import NationalPartyTotalsPage

# TODO update the JSON string below
json = "{}"
# create an instance of NationalPartyTotalsPage from a JSON string
national_party_totals_page_instance = NationalPartyTotalsPage.from_json(json)
# print the JSON string representation of the object
print(NationalPartyTotalsPage.to_json())

# convert the object into a dict
national_party_totals_page_dict = national_party_totals_page_instance.to_dict()
# create an instance of NationalPartyTotalsPage from a dict
national_party_totals_page_from_dict = NationalPartyTotalsPage.from_dict(national_party_totals_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


