# ScheduleBEfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_indicator** | **str** |  | [optional] 
**back_reference_schedule_name** | **str** |  | [optional] 
**back_reference_transaction_id** | **str** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**beneficiary_committee_name** | **str** |  | [optional] 
**candidate_office** | **str** |  | [optional] 
**candidate_office_district** | **str** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**csv_url** | **str** |  | [optional] 
**disbursement_amount** | **float** |  | [optional] 
**disbursement_date** | **date** |  | [optional] 
**disbursement_description** | **str** |  | [optional] 
**disbursement_type** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** |  | 
**filing** | [**EFilings**](EFilings.md) |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**is_notice** | **bool** |  | [optional] 
**line_number** | **str** |  | [optional] 
**load_timestamp** | **datetime** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**recipient_city** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_prefix** | **str** |  | [optional] 
**recipient_state** | **str** |  | [optional] 
**recipient_suffix** | **str** |  | [optional] 
**recipient_zip** | **str** |  | [optional] 
**related_line_number** | **int** |  | 
**report_type** | **str** |  | [optional] 
**semi_annual_bundled_refund** | **int** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_b_efile import ScheduleBEfile

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBEfile from a JSON string
schedule_b_efile_instance = ScheduleBEfile.from_json(json)
# print the JSON string representation of the object
print(ScheduleBEfile.to_json())

# convert the object into a dict
schedule_b_efile_dict = schedule_b_efile_instance.to_dict()
# create an instance of ScheduleBEfile from a dict
schedule_b_efile_from_dict = ScheduleBEfile.from_dict(schedule_b_efile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


