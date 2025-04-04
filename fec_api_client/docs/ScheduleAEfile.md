# ScheduleAEfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_indicator** | **str** |  | [optional] 
**back_reference_schedule_name** | **str** |  | [optional] 
**back_reference_transaction_id** | **str** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**conduit_committee_city** | **str** |  | [optional] 
**conduit_committee_id** | **str** |  | [optional] 
**conduit_committee_name** | **str** |  | [optional] 
**conduit_committee_state** | **str** |  | [optional] 
**conduit_committee_street1** | **str** |  | [optional] 
**conduit_committee_street2** | **str** |  | [optional] 
**conduit_committee_zip** | **str** |  | [optional] 
**contribution_receipt_amount** | **float** |  | [optional] 
**contribution_receipt_date** | **date** |  | [optional] 
**contributor_aggregate_ytd** | **float** |  | [optional] 
**contributor_city** | **str** | City of contributor | [optional] 
**contributor_employer** | **str** | Employer of contributor, filers need to make an effort to gather this information | [optional] 
**contributor_first_name** | **str** |  | [optional] 
**contributor_last_name** | **str** |  | [optional] 
**contributor_middle_name** | **str** |  | [optional] 
**contributor_name** | **str** |  | [optional] 
**contributor_occupation** | **str** | Occupation of contributor, filers need to make an effort to gather this information | [optional] 
**contributor_prefix** | **str** |  | [optional] 
**contributor_state** | **str** | State of contributor | [optional] 
**contributor_suffix** | **str** |  | [optional] 
**contributor_zip** | **str** | Zip code of contributor | [optional] 
**csv_url** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**fec_election_type_desc** | **str** |  | [optional] 
**fec_url** | **str** |  | [optional] 
**file_number** | **int** |  | 
**filing** | [**EFilings**](EFilings.md) |  | [optional] 
**image_number** | **str** |  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
**line_number** | **str** |  | [optional] 
**load_timestamp** | **datetime** |  | [optional] 
**memo_code** | **str** |  | [optional] 
**memo_text** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**pgo** | **str** |  | [optional] 
**related_line_number** | **int** |  | 
**report_type** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_a_efile import ScheduleAEfile

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAEfile from a JSON string
schedule_a_efile_instance = ScheduleAEfile.from_json(json)
# print the JSON string representation of the object
print(ScheduleAEfile.to_json())

# convert the object into a dict
schedule_a_efile_dict = schedule_a_efile_instance.to_dict()
# create an instance of ScheduleAEfile from a dict
schedule_a_efile_from_dict = ScheduleAEfile.from_dict(schedule_a_efile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


