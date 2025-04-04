# RadAnalyst


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyst_id** | **float** |  | [optional] 
**analyst_short_id** | **float** |  | [optional] 
**assignment_update_date** | **date** | Date of most recent RAD analyst assignment change | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**email** | **str** | Email of RAD analyst | [optional] 
**first_name** | **str** | Fist name of RAD analyst | [optional] 
**last_name** | **str** | Last name of RAD analyst | [optional] 
**rad_branch** | **str** | Branch of RAD analyst | [optional] 
**telephone_ext** | **float** |  | [optional] 
**title** | **str** | Title of RAD analyst | [optional] 

## Example

```python
from openapi_client.models.rad_analyst import RadAnalyst

# TODO update the JSON string below
json = "{}"
# create an instance of RadAnalyst from a JSON string
rad_analyst_instance = RadAnalyst.from_json(json)
# print the JSON string representation of the object
print(RadAnalyst.to_json())

# convert the object into a dict
rad_analyst_dict = rad_analyst_instance.to_dict()
# create an instance of RadAnalyst from a dict
rad_analyst_from_dict = RadAnalyst.from_dict(rad_analyst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


