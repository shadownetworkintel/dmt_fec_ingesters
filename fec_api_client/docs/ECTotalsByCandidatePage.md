# ECTotalsByCandidatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**OffsetInfo**](OffsetInfo.md) |  | [optional] 
**results** | [**List[ECTotalsByCandidate]**](ECTotalsByCandidate.md) |  | [optional] 

## Example

```python
from openapi_client.models.ec_totals_by_candidate_page import ECTotalsByCandidatePage

# TODO update the JSON string below
json = "{}"
# create an instance of ECTotalsByCandidatePage from a JSON string
ec_totals_by_candidate_page_instance = ECTotalsByCandidatePage.from_json(json)
# print the JSON string representation of the object
print(ECTotalsByCandidatePage.to_json())

# convert the object into a dict
ec_totals_by_candidate_page_dict = ec_totals_by_candidate_page_instance.to_dict()
# create an instance of ECTotalsByCandidatePage from a dict
ec_totals_by_candidate_page_from_dict = ECTotalsByCandidatePage.from_dict(ec_totals_by_candidate_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


