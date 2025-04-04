# ScheduleH4Efile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_or_event** | **str** |  | [optional] 
**administrative_voter_drive_activity_indicator** | **str** |  | [optional] 
**amendment_indicator** | **str** |  | [optional] 
**back_reference_schedule_name** | **str** |  | [optional] 
**back_reference_transaction_id** | **str** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**csv_url** | **str** |  | [optional] 
**direct_candidate_support_activity_indicator** | **str** |  | [optional] 
**disbursement_amount** | **float** |  | [optional] 
**disbursement_purpose** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**event_amount_year_to_date** | **float** |  | [optional] 
**event_purpose_date** | **date** |  | [optional] 
**exempt_activity_indicator** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**fed_share** | **float** |  | [optional] 
**file_number** | **int** |  | 
**filing** | [**EFilings**](EFilings.md) |  | [optional] 
**fundraising_activity_indicator** | **str** |  | [optional] 
**general_voter_drive_activity_indicator** | **str** |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**is_notice** | **bool** |  | [optional] 
**load_timestamp** | **datetime** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**nonfed_share** | **float** |  | [optional] 
**payee_city** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**payee_state** | **str** |  | [optional] 
**payee_zip** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**public_comm_indicator** | **str** |  | [optional] 
**related_line_number** | **int** |  | 
**report_type** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_h4_efile import ScheduleH4Efile

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleH4Efile from a JSON string
schedule_h4_efile_instance = ScheduleH4Efile.from_json(json)
# print the JSON string representation of the object
print(ScheduleH4Efile.to_json())

# convert the object into a dict
schedule_h4_efile_dict = schedule_h4_efile_instance.to_dict()
# create an instance of ScheduleH4Efile from a dict
schedule_h4_efile_from_dict = ScheduleH4Efile.from_dict(schedule_h4_efile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


