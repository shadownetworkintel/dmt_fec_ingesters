# InauguralDonationsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[InauguralDonations]**](InauguralDonations.md) |  | [optional] 

## Example

```python
from openapi_client.models.inaugural_donations_page import InauguralDonationsPage

# TODO update the JSON string below
json = "{}"
# create an instance of InauguralDonationsPage from a JSON string
inaugural_donations_page_instance = InauguralDonationsPage.from_json(json)
# print the JSON string representation of the object
print(InauguralDonationsPage.to_json())

# convert the object into a dict
inaugural_donations_page_dict = inaugural_donations_page_instance.to_dict()
# create an instance of InauguralDonationsPage from a dict
inaugural_donations_page_from_dict = InauguralDonationsPage.from_dict(inaugural_donations_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


