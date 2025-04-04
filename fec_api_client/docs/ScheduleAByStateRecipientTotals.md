# ScheduleAByStateRecipientTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**committee_type_full** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**count** | **int** | Number of records making up the total. | [optional] 
**cycle** | **int** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**state** | **str** | US state or territory | [optional] 
**state_full** | **str** | US state or territory | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_aby_state_recipient_totals import ScheduleAByStateRecipientTotals

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleAByStateRecipientTotals from a JSON string
schedule_aby_state_recipient_totals_instance = ScheduleAByStateRecipientTotals.from_json(json)
# print the JSON string representation of the object
print(ScheduleAByStateRecipientTotals.to_json())

# convert the object into a dict
schedule_aby_state_recipient_totals_dict = schedule_aby_state_recipient_totals_instance.to_dict()
# create an instance of ScheduleAByStateRecipientTotals from a dict
schedule_aby_state_recipient_totals_from_dict = ScheduleAByStateRecipientTotals.from_dict(schedule_aby_state_recipient_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


