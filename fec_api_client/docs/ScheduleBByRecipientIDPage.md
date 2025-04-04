# ScheduleBByRecipientIDPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleBByRecipientID]**](ScheduleBByRecipientID.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_bby_recipient_id_page import ScheduleBByRecipientIDPage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBByRecipientIDPage from a JSON string
schedule_bby_recipient_id_page_instance = ScheduleBByRecipientIDPage.from_json(json)
# print the JSON string representation of the object
print(ScheduleBByRecipientIDPage.to_json())

# convert the object into a dict
schedule_bby_recipient_id_page_dict = schedule_bby_recipient_id_page_instance.to_dict()
# create an instance of ScheduleBByRecipientIDPage from a dict
schedule_bby_recipient_id_page_from_dict = ScheduleBByRecipientIDPage.from_dict(schedule_bby_recipient_id_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


