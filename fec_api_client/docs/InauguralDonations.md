# InauguralDonations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**contributor_name** | **str** | Name of contributor | 
**cycle** | **int** |  | [optional] 
**total_donation** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.inaugural_donations import InauguralDonations

# TODO update the JSON string below
json = "{}"
# create an instance of InauguralDonations from a JSON string
inaugural_donations_instance = InauguralDonations.from_json(json)
# print the JSON string representation of the object
print(InauguralDonations.to_json())

# convert the object into a dict
inaugural_donations_dict = inaugural_donations_instance.to_dict()
# create an instance of InauguralDonations from a dict
inaugural_donations_from_dict = InauguralDonations.from_dict(inaugural_donations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


