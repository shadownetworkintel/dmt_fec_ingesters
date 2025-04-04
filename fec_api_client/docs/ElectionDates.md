# ElectionDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_election** | **bool** |  | [optional] 
**create_date** | **datetime** | Date the record was created | [optional] 
**election_date** | **date** | Date of election | [optional] 
**election_district** | **str** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**election_notes** | **str** |  | [optional] 
**election_party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**election_state** | **str** | US state or territory where a candidate runs for office | [optional] 
**election_type_full** | **str** |  | [optional] 
**election_type_id** | **str** | Election type  Convention, Primary, General, Special, Runoff etc.  | [optional] 
**election_year** | **int** | Year of election | [optional] 
**office_sought** | **str** | Federal office candidate runs for: H, S or P | [optional] 
**primary_general_date** | **date** |  | [optional] 
**update_date** | **datetime** | Date the record was updated | [optional] 

## Example

```python
from openapi_client.models.election_dates import ElectionDates

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionDates from a JSON string
election_dates_instance = ElectionDates.from_json(json)
# print the JSON string representation of the object
print(ElectionDates.to_json())

# convert the object into a dict
election_dates_dict = election_dates_instance.to_dict()
# create an instance of ElectionDates from a dict
election_dates_from_dict = ElectionDates.from_dict(election_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


