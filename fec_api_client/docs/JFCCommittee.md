# JFCCommittee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**joint_committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
**joint_committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 

## Example

```python
from openapi_client.models.jfc_committee import JFCCommittee

# TODO update the JSON string below
json = "{}"
# create an instance of JFCCommittee from a JSON string
jfc_committee_instance = JFCCommittee.from_json(json)
# print the JSON string representation of the object
print(JFCCommittee.to_json())

# convert the object into a dict
jfc_committee_dict = jfc_committee_instance.to_dict()
# create an instance of JFCCommittee from a dict
jfc_committee_from_dict = JFCCommittee.from_dict(jfc_committee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


