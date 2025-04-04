# ScheduleBByRecipientPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**SeekInfo**](SeekInfo.md) |  | [optional] 
**results** | [**List[ScheduleBByRecipient]**](ScheduleBByRecipient.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_bby_recipient_page import ScheduleBByRecipientPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBByRecipientPage from a JSON string
schedule_bby_recipient_page_instance = ScheduleBByRecipientPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleBByRecipientPage.to_json())

# convert the object into a dict
schedule_bby_recipient_page_dict = schedule_bby_recipient_page_instance.to_dict()
# create an instance of ScheduleBByRecipientPage from a dict
schedule_bby_recipient_page_from_dict = ScheduleBByRecipientPage.from_dict(schedule_bby_recipient_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


