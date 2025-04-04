# ScheduleH4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_or_event** | **str** |  | [optional] 
**administrative_activity_indicator** | **str** |  | [optional] 
**administrative_voter_drive_activity_indicator** | **str** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**direct_candidate_support_activity_indicator** | **str** |  | [optional] 
**disbursement_amount** | **float** |  | [optional] 
**disbursement_purpose** | **str** |  | [optional] 
**event_amount_year_to_date** | **float** |  | [optional] 
**event_purpose_date** | **date** |  | [optional] 
**exempt_activity_indicator** | **str** |  | [optional] 
**federal_share** | **float** |  | [optional] 
**file_number** | **int** |  | [optional] 
**filing_form** | **str** |  | [optional] 
**form_line_number** | **str** |  | [optional] 
**fundraising_activity_indicator** | **str** |  | [optional] 
**general_voter_drive_activity_indicator** | **str** |  | [optional] 
**image_number** | **str** |  | [optional] 
**line_number** | **str** |  | [optional] 
**link_id** | **int** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**nonfederal_share** | **float** |  | [optional] 
**original_sub_id** | **str** |  | [optional] 
**payee_city** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**payee_state** | **str** |  | [optional] 
**payee_street_1** | **str** |  | [optional] 
**payee_street_2** | **str** |  | [optional] 
**payee_zip** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**public_comm_indicator** | **str** |  | [optional] 
**report_type** | **str** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
**report_year** | **float** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_full** | **str** |  | [optional] 
**spender_committee_designation** | **str** |  | [optional] 
**spender_committee_name** | **str** |  | [optional] 
**spender_committee_type** | **str** |  | [optional] 
**sub_id** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_h4 import ScheduleH4

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleH4 from a JSON string
schedule_h4_instance = ScheduleH4.from_json(json)
# print the JSON string representation of the object
print(ScheduleH4.to_json())

# convert the object into a dict
schedule_h4_dict = schedule_h4_instance.to_dict()
# create an instance of ScheduleH4 from a dict
schedule_h4_from_dict = ScheduleH4.from_dict(schedule_h4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


