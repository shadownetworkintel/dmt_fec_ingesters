# TotalByOffice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_year** | **int** |  | [optional] 
**office** | **str** |  | [optional] 
**total_disbursements** | **float** |  | [optional] 
**total_individual_itemized_contributions** | **float** |  | [optional] 
**total_other_political_committee_contributions** | **float** |  | [optional] 
**total_receipts** | **float** |  | [optional] 
**total_transfers_from_other_authorized_committee** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.total_by_office import TotalByOffice

# TODO update the JSON string below
json = "{}"
# create an instance of TotalByOffice from a JSON string
total_by_office_instance = TotalByOffice.from_json(json)
# print the JSON string representation of the object
print(TotalByOffice.to_json())

# convert the object into a dict
total_by_office_dict = total_by_office_instance.to_dict()
# create an instance of TotalByOffice from a dict
total_by_office_from_dict = TotalByOffice.from_dict(total_by_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


