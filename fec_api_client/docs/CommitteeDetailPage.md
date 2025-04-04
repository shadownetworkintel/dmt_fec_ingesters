# CommitteeDetailPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[CommitteeDetail]**](CommitteeDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.committee_detail_page import CommitteeDetailPage

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeDetailPage from a JSON string
committee_detail_page_instance = CommitteeDetailPage.from_json(json)
# print the JSON string representation of the object
print(CommitteeDetailPage.to_json())

# convert the object into a dict
committee_detail_page_dict = committee_detail_page_instance.to_dict()
# create an instance of CommitteeDetailPage from a dict
committee_detail_page_from_dict = CommitteeDetailPage.from_dict(committee_detail_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


