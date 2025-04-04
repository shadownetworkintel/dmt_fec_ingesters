# Form2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_city** | **str** |  | [optional] 
**address_state** | **str** |  | [optional] 
**address_str1** | **str** |  | [optional] 
**address_str2** | **str** |  | [optional] 
**address_zip** | **str** |  | [optional] 
**candidate_district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**candidate_first_name** | **str** |  | [optional] 
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**candidate_last_name** | **str** |  | [optional] 
**candidate_middle_name** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**candidate_office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**candidate_party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**committee_address_city** | **str** |  | [optional] 
**committee_address_str1** | **str** |  | [optional] 
**committee_address_str2** | **str** |  | [optional] 
**committee_address_zip** | **str** |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** |  | [optional] 
**election_state** | **str** |  State or territory of the office sought.  | [optional] 
**election_year** | **str** |  | [optional] 
**file_number** | **int** | Filing ID number | [optional] 
**image_number** | **str** |  | [optional] 
**load_timestamp** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.form2 import Form2

# TODO update the JSON string below
json = "{}"
# create an instance of Form2 from a JSON string
form2_instance = Form2.from_json(json)
# print the JSON string representation of the object
print(Form2.to_json())

# convert the object into a dict
form2_dict = form2_instance.to_dict()
# create an instance of Form2 from a dict
form2_from_dict = Form2.from_dict(form2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


