# NationalPartyScheduleAPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[NationalPartyScheduleA]**](NationalPartyScheduleA.md) |  | [optional] 

## Example

```python
from openapi_client.models.national_party_schedule_a_page import NationalPartyScheduleAPage

# TODO update the JSON string below
json = "{}"
# create an instance of NationalPartyScheduleAPage from a JSON string
national_party_schedule_a_page_instance = NationalPartyScheduleAPage.from_json(json)
# print the JSON string representation of the object
print(NationalPartyScheduleAPage.to_json())

# convert the object into a dict
national_party_schedule_a_page_dict = national_party_schedule_a_page_instance.to_dict()
# create an instance of NationalPartyScheduleAPage from a dict
national_party_schedule_a_page_from_dict = NationalPartyScheduleAPage.from_dict(national_party_schedule_a_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


