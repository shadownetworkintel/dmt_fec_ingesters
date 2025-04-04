# CalendarDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_day** | **bool** |  | [optional] 
**calendar_category_id** | **int** |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
**category** | **str** |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **object** |  | [optional] [readonly] 
**event_id** | **int** | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 
**location** | **str** |  Can be state address or room.  | [optional] 
**start_date** | **object** |  | [optional] [readonly] 
**state** | **List[str]** | The state field only applies to election dates and reporting deadlines, reporting periods and all other dates do not have the array of states to filter on | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  A url for that event  | [optional] 

## Example

```python
from openapi_client.models.calendar_date import CalendarDate

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarDate from a JSON string
calendar_date_instance = CalendarDate.from_json(json)
# print the JSON string representation of the object
print(CalendarDate.to_json())

# convert the object into a dict
calendar_date_dict = calendar_date_instance.to_dict()
# create an instance of CalendarDate from a dict
calendar_date_from_dict = CalendarDate.from_dict(calendar_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


