# CommitteeReportsPresidentialPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeReportsPresidential]**](CommitteeReportsPresidential.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_reports_presidential_page import CommitteeReportsPresidentialPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeReportsPresidentialPage from a JSON string
committee_reports_presidential_page_instance = CommitteeReportsPresidentialPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeReportsPresidentialPage.to_json())

# convert the object into a dict
committee_reports_presidential_page_dict = committee_reports_presidential_page_instance.to_dict()
# create an instance of CommitteeReportsPresidentialPage from a dict
committee_reports_presidential_page_from_dict = CommitteeReportsPresidentialPage.from_dict(committee_reports_presidential_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


