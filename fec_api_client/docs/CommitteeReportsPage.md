# CommitteeReportsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeReports]**](CommitteeReports.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_reports_page import CommitteeReportsPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeReportsPage from a JSON string
committee_reports_page_instance = CommitteeReportsPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeReportsPage.to_json())

# convert the object into a dict
committee_reports_page_dict = committee_reports_page_instance.to_dict()
# create an instance of CommitteeReportsPage from a dict
committee_reports_page_from_dict = CommitteeReportsPage.from_dict(committee_reports_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


