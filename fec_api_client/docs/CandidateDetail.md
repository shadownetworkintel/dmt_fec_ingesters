# CandidateDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_through** | **int** | Last year a candidate was active. This field is specific to the candidate_id so if the same person runs for another office, there may be a different record for them. | [optional] 
**address_city** | **str** | City of candidate&#39;s address, as reported on their Form 2. | [optional] 
**address_state** | **str** | State of candidate&#39;s address, as reported on their Form 2. | [optional] 
**address_street_1** | **str** | Street of candidate&#39;s address, as reported on their Form 2. | [optional] 
**address_street_2** | **str** | Additional street information of candidate&#39;s address, as reported on their Form 2. | [optional] 
**address_zip** | **str** | Zip code of candidate&#39;s address, as reported on their Form 2. | [optional] 
**candidate_first_name** | **str** | First name of candidate running for office | [optional] 
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**candidate_inactive** | **bool** | True indicates that a candidate is inactive. | [optional] 
**candidate_last_name** | **str** |  Candidate last name  | [optional] 
**candidate_middle_name** | **str** | Middle name of candidate running for office | [optional] 
**candidate_prefix** | **str** | Name prefix of candidate running for office | [optional] 
**candidate_status** | **str** | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
**candidate_suffix** | **str** | Name suffix of candidate running for office | [optional] 
**cycles** | **List[int]** |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
**district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**district_number** | **int** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**election_districts** | **List[str]** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**election_years** | **List[int]** | Years in which a candidate ran for office. | [optional] 
**federal_funds_flag** | **bool** |  | [optional] 
**first_file_date** | **date** | The day the FEC received the candidate&#39;s first filing. This is a F2 candidate registration. | [optional] 
**flags** | **object** |  | [optional] 
**has_raised_funds** | **bool** |  | [optional] 
**incumbent_challenge** | **str** | One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
**incumbent_challenge_full** | **str** | Explains if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
**last_f2_date** | **date** | The day the FEC received the candidate&#39;s most recent Form 2 | [optional] 
**last_file_date** | **date** | The day the FEC received the candidate&#39;s most recent filing | [optional] 
**load_date** | **datetime** | Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently. | [optional] 
**name** | **str** | Name of candidate running for office | [optional] 
**office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**office_full** | **str** | Federal office candidate runs for: House, Senate or presidential | [optional] 
**party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**party_full** | **str** | Party affiliated with a candidate or committee | [optional] 
**state** | **str** | US state or territory where a candidate runs for office | [optional] 

## Example

```python
from openapi_client.models.candidate_detail import CandidateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateDetail from a JSON string
candidate_detail_instance = CandidateDetail.from_json(json)
# print the JSON string representation of the object
print(CandidateDetail.to_json())

# convert the object into a dict
candidate_detail_dict = candidate_detail_instance.to_dict()
# create an instance of CandidateDetail from a dict
candidate_detail_from_dict = CandidateDetail.from_dict(candidate_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


