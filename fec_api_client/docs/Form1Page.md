# Form1Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[Form1]**](Form1.md) |  | [optional] 

## Example

```python
from openapi_client.models.form1_page import Form1Page

# TODO update the JSON string below
json = "{}"
# create an instance of Form1Page from a JSON string
form1_page_instance = Form1Page.from_json(json)
# print the JSON string representation of the object
print(Form1Page.to_json())

# convert the object into a dict
form1_page_dict = form1_page_instance.to_dict()
# create an instance of Form1Page from a dict
form1_page_from_dict = Form1Page.from_dict(form1_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


