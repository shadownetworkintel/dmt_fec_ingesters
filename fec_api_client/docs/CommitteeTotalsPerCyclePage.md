# CommitteeTotalsPerCyclePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeTotalsPerCycle]**](CommitteeTotalsPerCycle.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_totals_per_cycle_page import CommitteeTotalsPerCyclePage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeTotalsPerCyclePage from a JSON string
committee_totals_per_cycle_page_instance = CommitteeTotalsPerCyclePage.from_json(json)
# print the JSON string representation of the object
print(CommitteeTotalsPerCyclePage.to_json())

# convert the object into a dict
committee_totals_per_cycle_page_dict = committee_totals_per_cycle_page_instance.to_dict()
# create an instance of CommitteeTotalsPerCyclePage from a dict
committee_totals_per_cycle_page_from_dict = CommitteeTotalsPerCyclePage.from_dict(committee_totals_per_cycle_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


