# NationalPartyScheduleBPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[NationalPartyScheduleB]**](NationalPartyScheduleB.md) |  | [optional] 

## Example

```python
from openapi_client.models.national_party_schedule_b_page import NationalPartyScheduleBPage

# TODO update the JSON string below
json = "{}"
# create an instance of NationalPartyScheduleBPage from a JSON string
national_party_schedule_b_page_instance = NationalPartyScheduleBPage.from_json(json)
# print the JSON string representation of the object
print(NationalPartyScheduleBPage.to_json())

# convert the object into a dict
national_party_schedule_b_page_dict = national_party_schedule_b_page_instance.to_dict()
# create an instance of NationalPartyScheduleBPage from a dict
national_party_schedule_b_page_from_dict = NationalPartyScheduleBPage.from_dict(national_party_schedule_b_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


