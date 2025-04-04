# CommitteeTotalsPacPartyPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeTotalsPacParty]**](CommitteeTotalsPacParty.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_totals_pac_party_page import CommitteeTotalsPacPartyPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeTotalsPacPartyPage from a JSON string
committee_totals_pac_party_page_instance = CommitteeTotalsPacPartyPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeTotalsPacPartyPage.to_json())

# convert the object into a dict
committee_totals_pac_party_page_dict = committee_totals_pac_party_page_instance.to_dict()
# create an instance of CommitteeTotalsPacPartyPage from a dict
committee_totals_pac_party_page_from_dict = CommitteeTotalsPacPartyPage.from_dict(committee_totals_pac_party_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


