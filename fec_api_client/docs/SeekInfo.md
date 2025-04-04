# SeekInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**is_count_exact** | **bool** |  | [optional] 
**last_indexes** | **object** |  | [optional] 
**pages** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.seek_info import SeekInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SeekInfo from a JSON string
seek_info_instance = SeekInfo.from_json(json)
# print the JSON string representation of the object
print(SeekInfo.to_json())

# convert the object into a dict
seek_info_dict = seek_info_instance.to_dict()
# create an instance of SeekInfo from a dict
seek_info_from_dict = SeekInfo.from_dict(seek_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


