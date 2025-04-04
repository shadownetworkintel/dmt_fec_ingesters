# TestForm1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliated_candidate_id** | **str** |  | [optional] 
**affiliated_committee_city** | **str** |  | [optional] 
**affiliated_committee_id** | **str** |  | [optional] 
**affiliated_committee_name** | **str** |  Affiliated committee or connected organization  | [optional] 
**affiliated_committee_state** | **str** |  | [optional] 
**affiliated_committee_str1** | **str** |  | [optional] 
**affiliated_committee_str2** | **str** |  | [optional] 
**affiliated_committee_zip** | **str** |  | [optional] 
**affiliated_relationship_code** | **str** |  | [optional] 
**candidate_district** | **str** |  House district of the office sought, if applicable.  | [optional] 
**candidate_first_name** | **str** | First name of candidate running for office | [optional] 
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**candidate_last_name** | **str** |  Candidate last name  | [optional] 
**candidate_middle_name** | **str** | Middle name of candidate running for office | [optional] 
**candidate_name** | **str** |  | [optional] 
**candidate_office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**candidate_party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**city** | **str** |  | [optional] 
**committee_city** | **str** |  City of committee as reported on the Form 1  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**committee_state** | **str** |  State of the committee&#39;s address as filed on the Form 1  | [optional] 
**committee_str1** | **str** |  Street address of committee as reported on the Form 1  | [optional] 
**committee_str2** | **str** |  Second line of street address of committee as reported on the Form 1  | [optional] 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**committee_zip** | **str** |  Zip code of committee as reported on the Form 1  | [optional] 
**election_state** | **str** |  State or territory of the office sought.  | [optional] 
**email** | **str** |  Email as reported on the Form 1  | [optional] 
**file_number** | **int** | Filing ID number | [optional] 
**image_number** | **str** |  | [optional] 
**load_timestamp** | **str** |  | [optional] 
**organization_type** | **str** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**pdf_url** | **str** |  | [optional] 
**state** | **str** | US state or territory where a candidate runs for office | [optional] 
**street_1** | **str** |  | [optional] 
**street_2** | **str** |  | [optional] 
**treasurer_city** | **str** |  City of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_first_name** | **str** |  Name 1 of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_last_name** | **str** |  | [optional] 
**treasurer_middle_name** | **str** |  Middle name of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_state** | **str** |  State of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_str1** | **str** |  Street of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_str2** | **str** |  Second line of the street of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_zip** | **str** |  Zip code of committee treasurer as reported on the Form 1  | [optional] 
**zip** | **str** | Zip code | [optional] 

## Example

```python
from openapi_client.models.test_form1 import TestForm1

# TODO update the JSON string below
json = "{}"
# create an instance of TestForm1 from a JSON string
test_form1_instance = TestForm1.from_json(json)
# print the JSON string representation of the object
print(TestForm1.to_json())

# convert the object into a dict
test_form1_dict = test_form1_instance.to_dict()
# create an instance of TestForm1 from a dict
test_form1_from_dict = TestForm1.from_dict(test_form1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


