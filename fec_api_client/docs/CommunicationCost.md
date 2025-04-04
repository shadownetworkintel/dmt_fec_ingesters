# CommunicationCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_code** | **str** |  | [optional] 
**action_code_full** | **str** |  | [optional] 
**candidate_first_name** | **str** |  | [optional] 
**candidate_id** | **str** |  | [optional] 
**candidate_last_name** | **str** |  | [optional] 
**candidate_middle_name** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**candidate_office** | **str** |  | [optional] 
**candidate_office_district** | **str** |  | [optional] 
**candidate_office_full** | **str** |  | [optional] 
**candidate_office_state** | **str** |  | [optional] 
**committee_id** | **str** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**communication_class** | **str** |  | [optional] 
**communication_type** | **str** |  | [optional] 
**communication_type_full** | **str** |  | [optional] 
**cycle** | **int** |  | [optional] 
**file_number** | **int** |  | [optional] 
**form_type_code** | **str** |  | [optional] 
**image_number** | **str** |  | [optional] 
**original_sub_id** | **int** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**primary_general_indicator** | **str** |  | [optional] 
**primary_general_indicator_description** | **str** |  | [optional] 
**purpose** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**report_year** | **int** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_type_full** | **str** |  | [optional] 
**state_full** | **str** |  | [optional] 
**sub_id** | **int** |  | [optional] 
**support_oppose_indicator** | **str** |  | [optional] 
**tran_id** | **str** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**transaction_date** | **date** |  | [optional] 
**transaction_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.communication_cost import CommunicationCost

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCost from a JSON string
communication_cost_instance = CommunicationCost.from_json(json)
# print the JSON string representation of the object
print(CommunicationCost.to_json())

# convert the object into a dict
communication_cost_dict = communication_cost_instance.to_dict()
# create an instance of CommunicationCost from a dict
communication_cost_from_dict = CommunicationCost.from_dict(communication_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


