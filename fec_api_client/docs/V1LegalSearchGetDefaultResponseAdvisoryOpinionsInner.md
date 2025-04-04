# V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ao_citations** | [**List[V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner]**](V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.md) |  | [optional] 
**aos_cited_by** | [**List[V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner]**](V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.md) |  | [optional] 
**commenter_names** | **List[str]** |  | [optional] 
**document_highlights** | **object** |  | [optional] 
**documents** | [**List[V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerDocumentsInner]**](V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerDocumentsInner.md) |  | [optional] 
**entities** | [**List[V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerEntitiesInner]**](V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerEntitiesInner.md) |  | [optional] 
**highlights** | **List[str]** |  | [optional] 
**is_pending** | **bool** |  | [optional] 
**issue_date** | **date** |  | [optional] 
**name** | **str** |  | [optional] 
**no** | **str** |  | [optional] 
**regulatory_citations** | [**List[V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerRegulatoryCitationsInner]**](V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerRegulatoryCitationsInner.md) |  | [optional] 
**representative_names** | **List[str]** |  | [optional] 
**request_date** | **date** |  | [optional] 
**requestor_names** | **List[str]** |  | [optional] 
**requestor_types** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**statutory_citations** | [**List[V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerStatutoryCitationsInner]**](V1LegalSearchGetDefaultResponseAdvisoryOpinionsInnerStatutoryCitationsInner.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_legal_search_get_default_response_advisory_opinions_inner import V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner from a JSON string
v1_legal_search_get_default_response_advisory_opinions_inner_instance = V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner.from_json(json)
# print the JSON string representation of the object
print(V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner.to_json())

# convert the object into a dict
v1_legal_search_get_default_response_advisory_opinions_inner_dict = v1_legal_search_get_default_response_advisory_opinions_inner_instance.to_dict()
# create an instance of V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner from a dict
v1_legal_search_get_default_response_advisory_opinions_inner_from_dict = V1LegalSearchGetDefaultResponseAdvisoryOpinionsInner.from_dict(v1_legal_search_get_default_response_advisory_opinions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


