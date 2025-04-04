# CommitteeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliated_committee_name** | **str** |  Affiliated committee or connected organization  | [optional] 
**candidate_ids** | **List[str]** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**city** | **str** |  City of committee as reported on the Form 1  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**committee_type_full** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**custodian_city** | **str** |  City of committee custodian as reported on the Form 1  | [optional] 
**custodian_name_1** | **str** |  Name 1 of committee custodian as reported on the Form 1  | [optional] 
**custodian_name_2** | **str** |  Name 2 of committee custodian as reported on the Form 1  | [optional] 
**custodian_name_full** | **str** |  Full name of committee custodian as reported on the Form 1  | [optional] 
**custodian_name_middle** | **str** |  Middle name of committee custodian as reported on the Form 1  | [optional] 
**custodian_name_prefix** | **str** |  Name prefix of committee custodian as reported on the Form 1  | [optional] 
**custodian_name_suffix** | **str** |  Suffix name of the committee custodian as reported on the Form 1  | [optional] 
**custodian_name_title** | **str** |  Name title of the committee custodian as reported on the Form 1  | [optional] 
**custodian_phone** | **str** |  Phone number of committee custodian as reported on the Form 1  | [optional] 
**custodian_state** | **str** |  State of committee custodian as reported on the Form 1  | [optional] 
**custodian_street_1** | **str** |  Street address of the committee custodian as reported on the Form 1  | [optional] 
**custodian_street_2** | **str** |  Second line of the street address of the committee custodian as reported on the Form 1  | [optional] 
**custodian_zip** | **str** |  Zip code of the committee custodian as reported on the Form 1  | [optional] 
**cycles** | **List[int]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**designation** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**designation_full** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**email** | **str** |  Email as reported on the Form 1  | [optional] 
**fax** | **str** |  Fax as reported on the Form 1  | [optional] 
**filing_frequency** | **str** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
**first_f1_date** | **date** | The day the FEC received the committee&#39;s first Form 1 | [optional] 
**first_file_date** | **date** | The day the FEC received the committee&#39;s first filing. This is usually a Form 1 committee registration. | [optional] 
**form_type** | **str** | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
**jfc_committee** | [**List[JFCCommittee]**](JFCCommittee.md) |  | [optional] 
**last_f1_date** | **date** | The day the FEC received the committee&#39;s most recent Form 1 | [optional] 
**last_file_date** | **date** | The day the FEC received the committee&#39;s most recent filing | [optional] 
**leadership_pac** | **str** |  Indicates if the committee is a leadership PAC  | [optional] 
**lobbyist_registrant_pac** | **str** |  Indicates if the committee is a lobbyist registrant PAC  | [optional] 
**name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**organization_type** | **str** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**organization_type_full** | **str** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**party_full** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**party_type** | **str** |  Code for the type of party the committee is, only if applicable  | [optional] 
**party_type_full** | **str** |  Description of the type of party the committee is, only if applicable  | [optional] 
**sponsor_candidate_ids** | **List[str]** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. This is a filter for Leadership PAC sponsor.  | [optional] 
**state** | **str** |  State of the committee&#39;s address as filed on the Form 1  | [optional] 
**state_full** | **str** |  State of committee as reported on the Form 1  | [optional] 
**street_1** | **str** |  Street address of committee as reported on the Form 1  | [optional] 
**street_2** | **str** |  Second line of street address of committee as reported on the Form 1  | [optional] 
**treasurer_city** | **str** |  City of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_name** | **str** | Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
**treasurer_name_1** | **str** |  Name 1 of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_name_2** | **str** |  Name 2 of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_name_middle** | **str** |  Middle name of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_name_prefix** | **str** |  Name Prefix of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_name_suffix** | **str** |  Name suffix of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_name_title** | **str** |  Name title of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_phone** | **str** |  Phone of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_state** | **str** |  State of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_street_1** | **str** |  Street of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_street_2** | **str** |  Second line of the street of committee treasurer as reported on the Form 1  | [optional] 
**treasurer_zip** | **str** |  Zip code of committee treasurer as reported on the Form 1  | [optional] 
**website** | **str** |  Website url as reported on the Form 1  | [optional] 
**zip** | **str** |  Zip code of committee as reported on the Form 1  | [optional] 

## Example

```python
from openapi_client.models.committee_detail import CommitteeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeDetail from a JSON string
committee_detail_instance = CommitteeDetail.from_json(json)
# print the JSON string representation of the object
print(CommitteeDetail.to_json())

# convert the object into a dict
committee_detail_dict = committee_detail_instance.to_dict()
# create an instance of CommitteeDetail from a dict
committee_detail_from_dict = CommitteeDetail.from_dict(committee_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


