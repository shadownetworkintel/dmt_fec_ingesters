# Form2Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[Form2]**](Form2.md) |  | [optional] 

## Example

```python
from openapi_client.models.form2_page import Form2Page

# TODO update the JSON string below
json = "{}"
# create an instance of Form2Page from a JSON string
form2_page_instance = Form2Page.from_json(json)
# print the JSON string representation of the object
print(Form2Page.to_json())

# convert the object into a dict
form2_page_dict = form2_page_instance.to_dict()
# create an instance of Form2Page from a dict
form2_page_from_dict = Form2Page.from_dict(form2_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


