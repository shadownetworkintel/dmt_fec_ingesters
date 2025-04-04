# CommitteeReportsHouseSenatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeReportsHouseSenate]**](CommitteeReportsHouseSenate.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_reports_house_senate_page import CommitteeReportsHouseSenatePage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeReportsHouseSenatePage from a JSON string
committee_reports_house_senate_page_instance = CommitteeReportsHouseSenatePage.from_json(json)
# print the JSON string representation of the object
print(CommitteeReportsHouseSenatePage.to_json())

# convert the object into a dict
committee_reports_house_senate_page_dict = committee_reports_house_senate_page_instance.to_dict()
# create an instance of CommitteeReportsHouseSenatePage from a dict
committee_reports_house_senate_page_from_dict = CommitteeReportsHouseSenatePage.from_dict(committee_reports_house_senate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


