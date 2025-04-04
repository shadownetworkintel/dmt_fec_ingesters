# StateElectionOfficeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**mailing_address1** | **str** |  | [optional] 
**mailing_address2** | **str** |  | [optional] 
**mailing_city** | **str** |  | [optional] 
**mailing_state** | **str** |  | [optional] 
**mailing_zipcode** | **str** |  | [optional] 
**office_name** | **str** |  | [optional] 
**office_type** | **str** |  | 
**primary_phone_number** | **str** |  | [optional] 
**secondary_phone_number** | **str** |  | [optional] 
**state** | **str** |  | 
**state_full_name** | **str** |  | [optional] 
**website_url1** | **str** |  | [optional] 
**website_url2** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.state_election_office_info import StateElectionOfficeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StateElectionOfficeInfo from a JSON string
state_election_office_info_instance = StateElectionOfficeInfo.from_json(json)
# print the JSON string representation of the object
print(StateElectionOfficeInfo.to_json())

# convert the object into a dict
state_election_office_info_dict = state_election_office_info_instance.to_dict()
# create an instance of StateElectionOfficeInfo from a dict
state_election_office_info_from_dict = StateElectionOfficeInfo.from_dict(state_election_office_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


