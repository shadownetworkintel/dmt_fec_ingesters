# Electioneering


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_indicator** | **str** |  | [optional] 
**beginning_image_number** | **str** |  | [optional] 
**calculated_candidate_share** | **float** |  | [optional] 
**candidate_district** | **str** |  | [optional] 
**candidate_id** | **str** |  | [optional] 
**candidate_name** | **str** |  | [optional] 
**candidate_office** | **str** |  | [optional] 
**candidate_state** | **str** |  | [optional] 
**committee_id** | **str** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**communication_date** | **date** |  It is the airing, broadcast, cablecast or other dissemination of the communication.  | [optional] 
**disbursement_amount** | **float** |  | [optional] 
**disbursement_date** | **date** |  Disbursement date includes actual disbursements and execution of contracts creating an obligation to make disbursements (SB date of disbursement).  | [optional] 
**election_type** | **str** |  | [optional] 
**file_number** | **int** |  | [optional] 
**link_id** | **int** |  | [optional] 
**number_of_candidates** | **float** |  | [optional] 
**payee_name** | **str** |  Name of the entity that received the payment.  | [optional] 
**payee_state** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**public_distribution_date** | **date** |  The pubic distribution date is the date that triggers disclosure of the electioneering communication (date reported on page 1 of Form 9).  | [optional] 
**purpose_description** | **str** |  | [optional] 
**receipt_date** | **date** |  | [optional] 
**report_year** | **int** |  | [optional] 
**sb_image_num** | **str** |  | [optional] 
**sb_link_id** | **str** |  | [optional] 
**sub_id** | **int** |  The identifier for each electioneering record.  | [optional] 

## Example

```python
from openapi_client.models.electioneering import Electioneering

# TODO update the JSON string below
json = "{}"
# create an instance of Electioneering from a JSON string
electioneering_instance = Electioneering.from_json(json)
# print the JSON string representation of the object
print(Electioneering.to_json())

# convert the object into a dict
electioneering_dict = electioneering_instance.to_dict()
# create an instance of Electioneering from a dict
electioneering_from_dict = Electioneering.from_dict(electioneering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


