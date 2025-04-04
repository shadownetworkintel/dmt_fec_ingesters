# EntityReceiptDisbursementTotalsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[EntityReceiptDisbursementTotals]**](EntityReceiptDisbursementTotals.md) |  | [optional] 

## Example

```python
from openapi_client.models.entity_receipt_disbursement_totals_page import EntityReceiptDisbursementTotalsPage

# TODO update the JSON string below
json = "{}"
# create an instance of EntityReceiptDisbursementTotalsPage from a JSON string
entity_receipt_disbursement_totals_page_instance = EntityReceiptDisbursementTotalsPage.from_json(json)
# print the JSON string representation of the object
print(EntityReceiptDisbursementTotalsPage.to_json())

# convert the object into a dict
entity_receipt_disbursement_totals_page_dict = entity_receipt_disbursement_totals_page_instance.to_dict()
# create an instance of EntityReceiptDisbursementTotalsPage from a dict
entity_receipt_disbursement_totals_page_from_dict = EntityReceiptDisbursementTotalsPage.from_dict(entity_receipt_disbursement_totals_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


