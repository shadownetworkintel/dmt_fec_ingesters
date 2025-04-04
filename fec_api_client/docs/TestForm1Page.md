# TestForm1Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[TestForm1]**](TestForm1.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_form1_page import TestForm1Page

# TODO update the JSON string below
json = "{}"
# create an instance of TestForm1Page from a JSON string
test_form1_page_instance = TestForm1Page.from_json(json)
# print the JSON string representation of the object
print(TestForm1Page.to_json())

# convert the object into a dict
test_form1_page_dict = test_form1_page_instance.to_dict()
# create an instance of TestForm1Page from a dict
test_form1_page_from_dict = TestForm1Page.from_dict(test_form1_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


