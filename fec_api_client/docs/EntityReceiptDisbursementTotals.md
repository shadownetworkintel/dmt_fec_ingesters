# EntityReceiptDisbursementTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cumulative_candidate_disbursements** | **float** | Cumulative candidate disbursements in a two year period, adjusted to avoid double counting. | [optional] 
**cumulative_candidate_receipts** | **float** | Cumulative candidate receipts in a two year period, adjusted to avoid double counting. | [optional] 
**cumulative_pac_disbursements** | **float** | Cumulative PAC disbursements in a two year period, adjusted to avoid double counting. | [optional] 
**cumulative_pac_receipts** | **float** | Cumulative PAC recipts in a two year period, adjusted to avoid double counting. | [optional] 
**cumulative_party_disbursements** | **float** | Cumulative party disbursements in a two year period, adjusted to avoid double counting. | [optional] 
**cumulative_party_receipts** | **float** | Cumulative party receipts in a two year period, adjusted to avoid double counting. | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**end_date** | **date** | The cumulative total for this month. | [optional] 

## Example

```python
from openapi_client.models.entity_receipt_disbursement_totals import EntityReceiptDisbursementTotals

# TODO update the JSON string below
json = "{}"
# create an instance of EntityReceiptDisbursementTotals from a JSON string
entity_receipt_disbursement_totals_instance = EntityReceiptDisbursementTotals.from_json(json)
# print the JSON string representation of the object
print(EntityReceiptDisbursementTotals.to_json())

# convert the object into a dict
entity_receipt_disbursement_totals_dict = entity_receipt_disbursement_totals_instance.to_dict()
# create an instance of EntityReceiptDisbursementTotals from a dict
entity_receipt_disbursement_totals_from_dict = EntityReceiptDisbursementTotals.from_dict(entity_receipt_disbursement_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


