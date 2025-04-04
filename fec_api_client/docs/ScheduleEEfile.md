# ScheduleEEfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_indicator** | **str** |  | [optional] 
**back_reference_schedule_name** | **str** |  | [optional] 
**back_reference_transaction_id** | **str** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**candidate_first_name** | **str** |  | [optional] 
**candidate_id** | **str** |  | [optional] 
**candidate_middle_name** | **str** |  | [optional] 
**candidate_name** | **str** | Name of candidate running for office | [optional] 
**candidate_office** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**candidate_office_district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**candidate_office_state** | **str** | US state or territory | [optional] 
**candidate_party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**candidate_prefix** | **str** |  | [optional] 
**candidate_suffix** | **str** |  | [optional] 
**category_code** | **str** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**csv_url** | **str** |  | [optional] 
**dissemination_date** | **date** |  Date when a PAC distrubutes or disseminates an independent expenditure and pays for it in the same reporting period  | [optional] 
**entity_type** | **str** |  | [optional] 
**expenditure_amount** | **int** |  | [optional] 
**expenditure_date** | **date** |  | [optional] 
**expenditure_description** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** |  | 
**filer_first_name** | **str** |  | [optional] 
**filer_last_name** | **str** |  | [optional] 
**filer_middle_name** | **str** |  | [optional] 
**filer_prefix** | **str** |  | [optional] 
**filer_suffix** | **str** |  | [optional] 
**filing** | [**EFilings**](EFilings.md) |  | [optional] 
**filing_form** | **str** |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**is_notice** | **bool** |  | [optional] 
**line_number** | **str** |  | [optional] 
**load_timestamp** | **datetime** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**most_recent** | **bool** |  Report is either new or is the most-recently filed amendment  | [optional] 
**notary_sign_date** | **date** |  | [optional] 
**office_total_ytd** | **float** |  | [optional] 
**payee_city** | **str** |  | [optional] 
**payee_first_name** | **str** |  | [optional] 
**payee_last_name** | **str** |  | [optional] 
**payee_middle_name** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**payee_prefix** | **str** |  | [optional] 
**payee_state** | **str** |  | [optional] 
**payee_street_1** | **str** |  | [optional] 
**payee_street_2** | **str** |  | [optional] 
**payee_suffix** | **str** |  | [optional] 
**payee_zip** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**related_line_number** | **int** |  | 
**report_type** | **str** |  | [optional] 
**support_oppose_indicator** | **str** | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_e_efile import ScheduleEEfile

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEEfile from a JSON string
schedule_e_efile_instance = ScheduleEEfile.from_json(json)
# print the JSON string representation of the object
print(ScheduleEEfile.to_json())

# convert the object into a dict
schedule_e_efile_dict = schedule_e_efile_instance.to_dict()
# create an instance of ScheduleEEfile from a dict
schedule_e_efile_from_dict = ScheduleEEfile.from_dict(schedule_e_efile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


