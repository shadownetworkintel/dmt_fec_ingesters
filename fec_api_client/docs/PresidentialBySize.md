# PresidentialBySize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrats   -P00000003    Republicans  | [optional] 
**contribution_receipt_amount** | **float** |  | [optional] 
**election_year** | **int** | Year of election | [optional] 
**size** | **int** |  The total all contributions in the following ranges: &#x60;&#x60;&#x60;   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + &#x60;&#x60;&#x60; Unitemized contributions are included in the &#x60;0&#x60; category.  | [optional] 
**size_range_id** | **int** |  The total all contributions range id.  | [optional] 

## Example

```python
from openapi_client.models.presidential_by_size import PresidentialBySize

# TODO update the JSON string below
json = "{}"
# create an instance of PresidentialBySize from a JSON string
presidential_by_size_instance = PresidentialBySize.from_json(json)
# print the JSON string representation of the object
print(PresidentialBySize.to_json())

# convert the object into a dict
presidential_by_size_dict = presidential_by_size_instance.to_dict()
# create an instance of PresidentialBySize from a dict
presidential_by_size_from_dict = PresidentialBySize.from_dict(presidential_by_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


