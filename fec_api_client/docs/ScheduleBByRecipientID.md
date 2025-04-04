# ScheduleBByRecipientID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**committee_name** | **str** |  | [optional] 
**count** | **int** |  Number of records making up the total.  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
**memo_count** | **int** |  Number of records making up the total.  | [optional] 
**memo_total** | **float** |  | [optional] 
**recipient_id** | **str** | The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. | 
**recipient_name** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_bby_recipient_id import ScheduleBByRecipientID

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBByRecipientID from a JSON string
schedule_bby_recipient_id_instance = ScheduleBByRecipientID.from_json(json)
# print the JSON string representation of the object
print(ScheduleBByRecipientID.to_json())

# convert the object into a dict
schedule_bby_recipient_id_dict = schedule_bby_recipient_id_instance.to_dict()
# create an instance of ScheduleBByRecipientID from a dict
schedule_bby_recipient_id_from_dict = ScheduleBByRecipientID.from_dict(schedule_bby_recipient_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


