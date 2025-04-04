# StateElectionOfficeInfoPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[StateElectionOfficeInfo]**](StateElectionOfficeInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.state_election_office_info_page import StateElectionOfficeInfoPage

# TODO update the JSON string below
json = "{}"
# create an instance of StateElectionOfficeInfoPage from a JSON string
state_election_office_info_page_instance = StateElectionOfficeInfoPage.from_json(json)
# print the JSON string representation of the object
print(StateElectionOfficeInfoPage.to_json())

# convert the object into a dict
state_election_office_info_page_dict = state_election_office_info_page_instance.to_dict()
# create an instance of StateElectionOfficeInfoPage from a dict
state_election_office_info_page_from_dict = StateElectionOfficeInfoPage.from_dict(state_election_office_info_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


