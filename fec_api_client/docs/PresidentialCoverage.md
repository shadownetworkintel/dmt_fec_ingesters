# PresidentialCoverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrats   -P00000003    Republicans  | [optional] 
**coverage_end_date** | **datetime** | Ending date of the reporting period | [optional] 
**election_year** | **int** | Year of election | [optional] 

## Example

```python
from openapi_client.models.presidential_coverage import PresidentialCoverage

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialCoverage from a JSON string
presidential_coverage_instance = PresidentialCoverage.from_json(json)
# print the JSON string representation of the object
print(PresidentialCoverage.to_json())

# convert the object into a dict
presidential_coverage_dict = presidential_coverage_instance.to_dict()
# create an instance of PresidentialCoverage from a dict
presidential_coverage_from_dict = PresidentialCoverage.from_dict(presidential_coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


