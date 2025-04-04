# ElectionDatesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ElectionDates]**](ElectionDates.md) |  | [optional] 

## Example

```python
from openapi_client.models.election_dates_page import ElectionDatesPage

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionDatesPage from a JSON string
election_dates_page_instance = ElectionDatesPage.from_json(json)
# print the JSON string representation of the object
print(ElectionDatesPage.to_json())

# convert the object into a dict
election_dates_page_dict = election_dates_page_instance.to_dict()
# create an instance of ElectionDatesPage from a dict
election_dates_page_from_dict = ElectionDatesPage.from_dict(election_dates_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


