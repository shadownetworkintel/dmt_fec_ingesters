# PresidentialCoveragePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[PresidentialCoverage]**](PresidentialCoverage.md) |  | [optional] 

## Example

```python
from openapi_client.models.presidential_coverage_page import PresidentialCoveragePage

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialCoveragePage from a JSON string
presidential_coverage_page_instance = PresidentialCoveragePage.from_json(json)
# print the JSON string representation of the object
print(PresidentialCoveragePage.to_json())

# convert the object into a dict
presidential_coverage_page_dict = presidential_coverage_page_instance.to_dict()
# create an instance of PresidentialCoveragePage from a dict
presidential_coverage_page_from_dict = PresidentialCoveragePage.from_dict(presidential_coverage_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


