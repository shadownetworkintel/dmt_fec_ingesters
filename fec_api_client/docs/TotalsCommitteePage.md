# TotalsCommitteePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[TotalsCommittee]**](TotalsCommittee.md) |  | [optional] 

## Example

```python
from openapi_client.models.totals_committee_page import TotalsCommitteePage

# TODO update the JSON string below
json = "{}"
# create an instance of TotalsCommitteePage from a JSON string
totals_committee_page_instance = TotalsCommitteePage.from_json(json)
# print the JSON string representation of the object
print(TotalsCommitteePage.to_json())

# convert the object into a dict
totals_committee_page_dict = totals_committee_page_instance.to_dict()
# create an instance of TotalsCommitteePage from a dict
totals_committee_page_from_dict = TotalsCommitteePage.from_dict(totals_committee_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


