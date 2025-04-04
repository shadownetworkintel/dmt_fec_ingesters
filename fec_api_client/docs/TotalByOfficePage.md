# TotalByOfficePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[TotalByOffice]**](TotalByOffice.md) |  | [optional] 

## Example

```python
from openapi_client.models.total_by_office_page import TotalByOfficePage

# TODO update the JSON string below
json = "{}"
# create an instance of TotalByOfficePage from a JSON string
total_by_office_page_instance = TotalByOfficePage.from_json(json)
# print the JSON string representation of the object
print(TotalByOfficePage.to_json())

# convert the object into a dict
total_by_office_page_dict = total_by_office_page_instance.to_dict()
# create an instance of TotalByOfficePage from a dict
total_by_office_page_from_dict = TotalByOfficePage.from_dict(total_by_office_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


