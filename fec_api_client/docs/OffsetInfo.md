# OffsetInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**is_count_exact** | **bool** |  | [optional] 
**page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.offset_info import OffsetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OffsetInfo from a JSON string
offset_info_instance = OffsetInfo.from_json(json)
# print the JSON string representation of the object
print(OffsetInfo.to_json())

# convert the object into a dict
offset_info_dict = offset_info_instance.to_dict()
# create an instance of OffsetInfo from a dict
offset_info_from_dict = OffsetInfo.from_dict(offset_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


