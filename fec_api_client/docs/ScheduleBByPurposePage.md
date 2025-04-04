# ScheduleBByPurposePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleBByPurpose]**](ScheduleBByPurpose.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_bby_purpose_page import ScheduleBByPurposePage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBByPurposePage from a JSON string
schedule_bby_purpose_page_instance = ScheduleBByPurposePage.from_json(json)
# print the JSON string representation of the object
print(ScheduleBByPurposePage.to_json())

# convert the object into a dict
schedule_bby_purpose_page_dict = schedule_bby_purpose_page_instance.to_dict()
# create an instance of ScheduleBByPurposePage from a dict
schedule_bby_purpose_page_from_dict = ScheduleBByPurposePage.from_dict(schedule_bby_purpose_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


