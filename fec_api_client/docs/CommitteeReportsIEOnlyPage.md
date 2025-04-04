# CommitteeReportsIEOnlyPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeReportsIEOnly]**](CommitteeReportsIEOnly.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_reports_ie_only_page import CommitteeReportsIEOnlyPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeReportsIEOnlyPage from a JSON string
committee_reports_ie_only_page_instance = CommitteeReportsIEOnlyPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeReportsIEOnlyPage.to_json())

# convert the object into a dict
committee_reports_ie_only_page_dict = committee_reports_ie_only_page_instance.to_dict()
# create an instance of CommitteeReportsIEOnlyPage from a dict
committee_reports_ie_only_page_from_dict = CommitteeReportsIEOnlyPage.from_dict(committee_reports_ie_only_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


