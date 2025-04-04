# CommitteeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliated_committee_name** | **str** |  Affiliated committee or connected organization  | [optional] 
**candidate_ids** | **List[str]** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**city** | **str** |  City of committee as reported on the Form 1  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**committee_type_full** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**cycle** | **int** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | 
**cycles** | **List[int]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**cycles_has_activity** | **List[int]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1), and the committee has filling activity during the cycle  | [optional] 
**cycles_has_financial** | **List[int]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s), and the committee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;) during this cycle.  | [optional] 
**designation** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**designation_full** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**filing_frequency** | **str** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
**first_f1_date** | **date** | The day the FEC received the committee&#39;s first Form 1 | [optional] 
**first_file_date** | **date** | The day the FEC received the committee&#39;s first filing. This is usually a Form 1 committee registration. | [optional] 
**is_active** | **bool** |  True indicates that a committee is active.  | [optional] 
**jfc_committee** | [**List[JFCCommittee]**](JFCCommittee.md) |  | [optional] 
**last_cycle_has_activity** | **int** |  The latest two year election cycle that the committee has filings  | [optional] 
**last_cycle_has_financial** | **int** |  The latest two year election cycle that the committee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;).  | [optional] 
**last_f1_date** | **date** | The day the FEC received the committee&#39;s most recent Form 1 | [optional] 
**last_file_date** | **date** | The day the FEC received the committee&#39;s most recent filing | [optional] 
**name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**organization_type** | **str** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**organization_type_full** | **str** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**party_full** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**state** | **str** |  State of the committee&#39;s address as filed on the Form 1  | [optional] 
**state_full** | **str** |  State of committee as reported on the Form 1  | [optional] 
**street_1** | **str** |  Street address of committee as reported on the Form 1  | [optional] 
**street_2** | **str** |  Second line of street address of committee as reported on the Form 1  | [optional] 
**treasurer_name** | **str** | Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
**zip** | **str** |  Zip code of committee as reported on the Form 1  | [optional] 

## Example

```python
from openapi_client.models.committee_history import CommitteeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeHistory from a JSON string
committee_history_instance = CommitteeHistory.from_json(json)
# print the JSON string representation of the object
print(CommitteeHistory.to_json())

# convert the object into a dict
committee_history_dict = committee_history_instance.to_dict()
# create an instance of CommitteeHistory from a dict
committee_history_from_dict = CommitteeHistory.from_dict(committee_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


