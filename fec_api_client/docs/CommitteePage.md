# CommitteePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[Committee]**](Committee.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_page import CommitteePage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteePage from a JSON string
committee_page_instance = CommitteePage.from_json(json)
# print the JSON string representation of the object
print(CommitteePage.to_json())

# convert the object into a dict
committee_page_dict = committee_page_instance.to_dict()
# create an instance of CommitteePage from a dict
committee_page_from_dict = CommitteePage.from_dict(committee_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


