# ScheduleBEfilePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ScheduleBEfile]**](ScheduleBEfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_b_efile_page import ScheduleBEfilePage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBEfilePage from a JSON string
schedule_b_efile_page_instance = ScheduleBEfilePage.from_json(json)
# print the JSON string representation of the object
print(ScheduleBEfilePage.to_json())

# convert the object into a dict
schedule_b_efile_page_dict = schedule_b_efile_page_instance.to_dict()
# create an instance of ScheduleBEfilePage from a dict
schedule_b_efile_page_from_dict = ScheduleBEfilePage.from_dict(schedule_b_efile_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


