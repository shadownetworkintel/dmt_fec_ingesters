# NationalPartyTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  | 
**committee_name** | **str** |  | [optional] 
**total_disbursements** | **float** |  | [optional] 
**total_receipts** | **float** |  | [optional] 
**two_year_transaction_period** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.national_party_totals import NationalPartyTotals

# TODO update the JSON string below
json = "{}"
# create an instance of NationalPartyTotals from a JSON string
national_party_totals_instance = NationalPartyTotals.from_json(json)
# print the JSON string representation of the object
print(NationalPartyTotals.to_json())

# convert the object into a dict
national_party_totals_dict = national_party_totals_instance.to_dict()
# create an instance of NationalPartyTotals from a dict
national_party_totals_from_dict = NationalPartyTotals.from_dict(national_party_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


