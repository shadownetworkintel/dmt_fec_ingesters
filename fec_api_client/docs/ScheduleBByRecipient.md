# ScheduleBByRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**committee_total_disbursements** | **float** |  | [optional] 
**count** | **int** |  Number of records making up the total.  | [optional] 
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
**memo_count** | **int** |  Number of records making up the total.  | [optional] 
**memo_total** | **float** |  | [optional] 
**recipient_disbursement_percent** | **float** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_bby_recipient import ScheduleBByRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBByRecipient from a JSON string
schedule_bby_recipient_instance = ScheduleBByRecipient.from_json(json)
# print the JSON string representation of the object
print(ScheduleBByRecipient.to_json())

# convert the object into a dict
schedule_bby_recipient_dict = schedule_bby_recipient_instance.to_dict()
# create an instance of ScheduleBByRecipient from a dict
schedule_bby_recipient_from_dict = ScheduleBByRecipient.from_dict(schedule_bby_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


