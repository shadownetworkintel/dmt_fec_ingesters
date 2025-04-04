# RadAnalystPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[RadAnalyst]**](RadAnalyst.md) |  | [optional] 

## Example

```python
from openapi_client.models.rad_analyst_page import RadAnalystPage

# TODO update the JSON string below
json = "{}"
# create an instance of RadAnalystPage from a JSON string
rad_analyst_page_instance = RadAnalystPage.from_json(json)
# print the JSON string representation of the object
print(RadAnalystPage.to_json())

# convert the object into a dict
rad_analyst_page_dict = rad_analyst_page_instance.to_dict()
# create an instance of RadAnalystPage from a dict
rad_analyst_page_from_dict = RadAnalystPage.from_dict(rad_analyst_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


