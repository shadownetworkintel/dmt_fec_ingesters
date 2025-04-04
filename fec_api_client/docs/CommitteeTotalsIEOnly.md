# CommitteeTotalsIEOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**committee_state** | **str** |  State of the committee&#39;s address as filed on the Form 1  | [optional] 
**contributions_ie_and_party_expenditures_made_percent** | **float** |  | [optional] 
**coverage_end_date** | **datetime** | Ending date of the reporting period | [optional] 
**coverage_start_date** | **datetime** | Beginning date of the reporting period | [optional] 
**cycle** | **int** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**filing_frequency** | **str** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
**filing_frequency_full** | **str** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
**first_file_date** | **date** | The day the FEC received the committee&#39;s first filing. This is usually a Form 1 committee registration. | [optional] 
**individual_contributions_percent** | **float** |  | [optional] 
**last_beginning_image_number** | **str** |  | [optional] 
**last_cash_on_hand_end_period** | **float** |  | [optional] 
**operating_expenditures_percent** | **float** |  | [optional] 
**party_and_other_committee_contributions_percent** | **float** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**report_form** | **str** |  | [optional] 
**total_independent_contributions** | **float** |  | [optional] 
**total_independent_expenditures** | **float** |  | [optional] 
**transaction_coverage_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.committee_totals_ie_only import CommitteeTotalsIEOnly

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeTotalsIEOnly from a JSON string
committee_totals_ie_only_instance = CommitteeTotalsIEOnly.from_json(json)
# print the JSON string representation of the object
print(CommitteeTotalsIEOnly.to_json())

# convert the object into a dict
committee_totals_ie_only_dict = committee_totals_ie_only_instance.to_dict()
# create an instance of CommitteeTotalsIEOnly from a dict
committee_totals_ie_only_from_dict = CommitteeTotalsIEOnly.from_dict(committee_totals_ie_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


