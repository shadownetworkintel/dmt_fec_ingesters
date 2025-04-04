# CommitteeTotalsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeTotals]**](CommitteeTotals.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_totals_page import CommitteeTotalsPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeTotalsPage from a JSON string
committee_totals_page_instance = CommitteeTotalsPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeTotalsPage.to_json())

# convert the object into a dict
committee_totals_page_dict = committee_totals_page_instance.to_dict()
# create an instance of CommitteeTotalsPage from a dict
committee_totals_page_from_dict = CommitteeTotalsPage.from_dict(committee_totals_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


