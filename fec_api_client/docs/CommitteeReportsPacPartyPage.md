# CommitteeReportsPacPartyPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeReportsPacParty]**](CommitteeReportsPacParty.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_reports_pac_party_page import CommitteeReportsPacPartyPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeReportsPacPartyPage from a JSON string
committee_reports_pac_party_page_instance = CommitteeReportsPacPartyPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeReportsPacPartyPage.to_json())

# convert the object into a dict
committee_reports_pac_party_page_dict = committee_reports_pac_party_page_instance.to_dict()
# create an instance of CommitteeReportsPacPartyPage from a dict
committee_reports_pac_party_page_from_dict = CommitteeReportsPacPartyPage.from_dict(committee_reports_pac_party_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


