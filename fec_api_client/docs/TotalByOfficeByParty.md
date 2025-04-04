# TotalByOfficeByParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_year** | **int** |  | [optional] 
**office** | **str** |  | [optional] 
**party** | **str** |  | [optional] 
**total_disbursements** | **float** |  | [optional] 
**total_receipts** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.total_by_office_by_party import TotalByOfficeByParty

# TODO update the JSON string below
json = "{}"
# create an instance of TotalByOfficeByParty from a JSON string
total_by_office_by_party_instance = TotalByOfficeByParty.from_json(json)
# print the JSON string representation of the object
print(TotalByOfficeByParty.to_json())

# convert the object into a dict
total_by_office_by_party_dict = total_by_office_by_party_instance.to_dict()
# create an instance of TotalByOfficeByParty from a dict
total_by_office_by_party_from_dict = TotalByOfficeByParty.from_dict(total_by_office_by_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


