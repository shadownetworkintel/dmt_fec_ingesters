# openapi_client.LegalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_legal_search_get**](LegalApi.md#v1_legal_search_get) | **GET** /v1/legal/search/ | 


# **v1_legal_search_get**
> V1LegalSearchGetDefaultResponse v1_legal_search_get(q=q, from_hit=from_hit, hits_returned=hits_returned, type=type, ao_no=ao_no, ao_name=ao_name, ao_min_issue_date=ao_min_issue_date, ao_max_issue_date=ao_max_issue_date, ao_min_request_date=ao_min_request_date, ao_max_request_date=ao_max_request_date, ao_min_document_date=ao_min_document_date, ao_max_document_date=ao_max_document_date, ao_doc_category_id=ao_doc_category_id, ao_is_pending=ao_is_pending, ao_status=ao_status, ao_requestor=ao_requestor, ao_requestor_type=ao_requestor_type, ao_regulatory_citation=ao_regulatory_citation, ao_statutory_citation=ao_statutory_citation, ao_citation_require_all=ao_citation_require_all, ao_commenter=ao_commenter, ao_representative=ao_representative, case_no=case_no, case_respondents=case_respondents, case_election_cycles=case_election_cycles, case_min_open_date=case_min_open_date, primary_subject_id=primary_subject_id, secondary_subject_id=secondary_subject_id, case_max_open_date=case_max_open_date, case_min_close_date=case_min_close_date, case_max_close_date=case_max_close_date, case_min_document_date=case_min_document_date, case_max_document_date=case_max_document_date, case_regulatory_citation=case_regulatory_citation, case_statutory_citation=case_statutory_citation, case_citation_require_all=case_citation_require_all, q_exclude=q_exclude, case_doc_category_id=case_doc_category_id, mur_type=mur_type, mur_disposition_category_id=mur_disposition_category_id, af_name=af_name, af_committee_id=af_committee_id, af_report_year=af_report_year, af_min_rtb_date=af_min_rtb_date, af_max_rtb_date=af_max_rtb_date, af_rtb_fine_amount=af_rtb_fine_amount, af_min_fd_date=af_min_fd_date, af_max_fd_date=af_max_fd_date, af_fd_fine_amount=af_fd_fine_amount, sort=sort, case_min_penalty_amount=case_min_penalty_amount, case_max_penalty_amount=case_max_penalty_amount, q_proximity=q_proximity, max_gaps=max_gaps, proximity_filter=proximity_filter, proximity_filter_term=proximity_filter_term, filename=filename, api_key=api_key)


Search legal documents by document type, or across all document types using keywords, parameter values and ranges.
This endpoint uses elasticsearch-dsl pagination.For pagination, use both `from_hit` and `hits_returned` parameters. `from_hit` defines the offset from the first result you want to fetch. `hits_returned` allows you to configure the maximum results to be returned.
By default `from_hit` = 0 and `hits_returned` = 20, endpoint will return the first 20 documents (i.e. 0 to 19).
if set `from_hit` = 20 and `hits_returned` = 20, endpoint will return documents range from 21 to 40 (i.e. 20 to 39).
The maximum value of `hits_returned` is 200.



### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.v1_legal_search_get_default_response import V1LegalSearchGetDefaultResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration.api_key['ApiKeyHeaderAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeaderAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration.api_key['ApiKeyQueryAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQueryAuth'] = 'Bearer'

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LegalApi(api_client)
    q = 'q_example' # str |  Text to search legal documents for  (optional)
    from_hit = 56 # int |  Get results starting from this index  (optional)
    hits_returned = 56 # int |  Number of results to return (max 10)  (optional)
    type = 'type_example' # str |  Choose a legal document type  (optional)
    ao_no = ['ao_no_example'] # List[str] |  Force advisory opinion number  (optional)
    ao_name = ['ao_name_example'] # List[str] |  Force advisory opinion name  (optional)
    ao_min_issue_date = 'ao_min_issue_date_example' # str |  Earliest issue date of advisory opinion  (optional)
    ao_max_issue_date = 'ao_max_issue_date_example' # str |  Latest issue date of advisory opinion  (optional)
    ao_min_request_date = 'ao_min_request_date_example' # str |  Earliest request date of advisory opinion  (optional)
    ao_max_request_date = 'ao_max_request_date_example' # str |  Latest request date of advisory opinion  (optional)
    ao_min_document_date = 'ao_min_document_date_example' # str |  Selects all advisory opinion documents dated on or after this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\"  (optional)
    ao_max_document_date = 'ao_max_document_date_example' # str |  Selects all advisory opinion documents dated on or before this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\"  (optional)
    ao_doc_category_id = ['ao_doc_category_id_example'] # List[str] |  Category of the document F - Final Opinion V - Votes D - Draft Documents R - AO Request, Supplemental Material, and Extensions of Time W - Withdrawal of Request C - Comments and Ex parte Communications S - Commissioner Statements  (optional)
    ao_is_pending = True # bool |  AO is pending  (optional)
    ao_status = 'ao_status_example' # str |  Status of AO (pending, withdrawn, or final)  (optional)
    ao_requestor = 'ao_requestor_example' # str |  The requestor of the advisory opinion  (optional)
    ao_requestor_type = ['ao_requestor_type_example'] # List[str] |  Code of the advisory opinion requestor type. Select one or more codes to filter by advisory opinion requestor type:         - 1 - Federal candidate/candidate committee/officeholder         - 2 - Publicly funded candidates/committees         - 3 - Party committee, national         - 4 - Party committee, state or local         - 5 - Nonconnected political committee         - 6 - Separate segregated fun          - 7 - Labor Organization         - 8 - Trade Association         - 9 - Membership Organization, Cooperative, Corporation W/O Capital Stocks         - 10 - Corporation (including LLCs electing corporate status)         - 11 - Partnership (including LLCs electing partnership status)         - 12 - Governmental entity          - 13 - Research/Public Interest/Educational Institution         - 14 - Law Firm         - 15 - Individual         - 16 - Other  (optional)
    ao_regulatory_citation = ['ao_regulatory_citation_example'] # List[str] |  Regulatory citations  (optional)
    ao_statutory_citation = ['ao_statutory_citation_example'] # List[str] |  Statutory citations  (optional)
    ao_citation_require_all = True # bool |  Require all citations to be in document (default behavior is any)  (optional)
    ao_commenter = 'ao_commenter_example' # str |  Name of commenter  (optional)
    ao_representative = 'ao_representative_example' # str |  Name of representative  (optional)
    case_no = ['case_no_example'] # List[str] |  Enforcement matter case number  (optional)
    case_respondents = 'case_respondents_example' # str |  Cases respondents  (optional)
    case_election_cycles = 56 # int |  Cases election cycles  (optional)
    case_min_open_date = 'case_min_open_date_example' # str |  The earliest date opened of case  (optional)
    primary_subject_id = ['primary_subject_id_example'] # List[str] |  Primary Subject Description:     - 1 - Allocation     - 2 - Committees     - 3 - Contributions     - 4 - Disclaimer     - 5 - Disbursements     - 6 - Electioneering     - 7 - Expenditures     - 8 - Express Advocacy     - 9 - Foreign Nationals     - 10 - Fraudulent misrepresentation     - 11 - Issue Advocacy     - 12 - Knowing and Willful     - 13 - Loans     - 14 - Non-federal     - 15 - Other     - 16 - Personal use     - 17 - Presidential     - 18 - Reporting     - 19 - Soft Money     - 20 - Solicitation  (optional)
    secondary_subject_id = ['secondary_subject_id_example'] # List[str] |  Secondary Subject Description:     - 1 - Candidate     - 2 - Multi-candidate     - 3 - Non-party     - 4 - PAC     - 5 - Party     - 6 - Political     - 7 - Presidential     - 8 - Corporations     - 9 - Excessive     - 10 - Exemptions     - 11 - In the name of another     - 12 - Labor unions     - 13 - Limitations     - 14 - National bank     - 15 - Prohibited     - 16 - Coordinated     - 17 - Limits     - 18 - Prohibitions  (optional)
    case_max_open_date = 'case_max_open_date_example' # str |  The latest date opened of case  (optional)
    case_min_close_date = 'case_min_close_date_example' # str |  The earliest date closed of case  (optional)
    case_max_close_date = 'case_max_close_date_example' # str |  The latest date closed of case  (optional)
    case_min_document_date = 'case_min_document_date_example' # str |  Selects all case documents dated on or after this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\"  (optional)
    case_max_document_date = 'case_max_document_date_example' # str |  Selects all case documents dated on or before this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\"  (optional)
    case_regulatory_citation = ['case_regulatory_citation_example'] # List[str] |  Regulatory citations  (optional)
    case_statutory_citation = ['case_statutory_citation_example'] # List[str] |  Statutory citations  (optional)
    case_citation_require_all = True # bool |  Require all citations to be in document (default behavior is any)  (optional)
    q_exclude = 'q_exclude_example' # str |  Exclude documents containing this term  (optional)
    case_doc_category_id = ['case_doc_category_id_example'] # List[str] |  Select one or more case document category id to filter by corresponding case document category:         - 1 - Conciliation and Settlement Agreements         - 2 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 3 - General Counsel Reports, Briefs, Notifications and Responses         - 4 - Certifications         - 5 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 6 - Statement of Reasons          - 1001 - ADR Settlement Agreements         - 1002 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 1003 - ADR Memoranda, Notifications and Responses         - 1004 - Certifications         - 1005 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 1006 - Statement of Reasons          - 2001 - Administrative Fine Case  (optional)
    mur_type = 'mur_type_example' # str |  Type of MUR : current or archived  (optional)
    mur_disposition_category_id = ['mur_disposition_category_id_example'] # List[str] |  Select one or more MUR disposition category id to filter by corresponding MUR disposition category:         - 1 - Conciliation-PPC         - 2 - Conciliation-PC         - 3 - Dismiss and Remind         - 4 - Dismissed         - 5 - Dismissed-Low Rated         - 6 - Dismissed-Other         - 7 - Dismissed-Stale         - 8 - Dismiss pursuant to prosecutorial discretion         - 9 - Dismiss pursuant to prosecutorial discretion, and caution         - 10 - Enforcement - Disposition - Dismissed Dismiss - Dismiss and Caution         - 11 - No PCTB         - 12 - No RTB         - 13 - PCTB Finding         - 14 - PC/NFA         - 15 - RTB Finding         - 16 - RTB/NFA         - 17 - Take no action         - 18 - Take No Further Action  (optional)
    af_name = ['af_name_example'] # List[str] |  Admin fine committee name  (optional)
    af_committee_id = 'af_committee_id_example' # str |  Admin fine committee ID  (optional)
    af_report_year = 'af_report_year_example' # str |  Admin fine report year  (optional)
    af_min_rtb_date = 'af_min_rtb_date_example' # str |  The earliest Reason to Believe date  (optional)
    af_max_rtb_date = 'af_max_rtb_date_example' # str |  The latest Reason to Believe date  (optional)
    af_rtb_fine_amount = 56 # int |  Reason to Believe fine amount  (optional)
    af_min_fd_date = 'af_min_fd_date_example' # str |  The earliest Final Determination date  (optional)
    af_max_fd_date = 'af_max_fd_date_example' # str |  The latest Final Determination date  (optional)
    af_fd_fine_amount = 56 # int |     Final Determination fine amount  (optional)
    sort = 'sort_example' # str |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no`  (optional)
    case_min_penalty_amount = 'case_min_penalty_amount_example' # str |  Show cases with a penalty greater than this amount  (optional)
    case_max_penalty_amount = 'case_max_penalty_amount_example' # str |  Show cases with a penalty less than this amount   (optional)
    q_proximity = ['q_proximity_example'] # List[str] |  This search identifies documents where the specified phrases appear near each other. The field supports both a single phrase or multiple phrases. For a single phrase, the maximum gap is applied between the words in the phrase. For multiple phrases, the maximum gap is applied between the phrases themselves.  (optional)
    max_gaps = 56 # int |  The maximum number of positions allowed between terms specified in `q_proximity`  (optional)
    proximity_filter = 'proximity_filter_example' # str |  Adds additional filters to the proximity search that provides options to specify positional constraints  (optional)
    proximity_filter_term = 'proximity_filter_term_example' # str |  Specifies the term to which the `proximity_filter` option applies to and defines what must appear in relation to the `q_proximity` phrase  (optional)
    filename = 'filename_example' # str |  Search documents by file name  (optional)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_legal_search_get(q=q, from_hit=from_hit, hits_returned=hits_returned, type=type, ao_no=ao_no, ao_name=ao_name, ao_min_issue_date=ao_min_issue_date, ao_max_issue_date=ao_max_issue_date, ao_min_request_date=ao_min_request_date, ao_max_request_date=ao_max_request_date, ao_min_document_date=ao_min_document_date, ao_max_document_date=ao_max_document_date, ao_doc_category_id=ao_doc_category_id, ao_is_pending=ao_is_pending, ao_status=ao_status, ao_requestor=ao_requestor, ao_requestor_type=ao_requestor_type, ao_regulatory_citation=ao_regulatory_citation, ao_statutory_citation=ao_statutory_citation, ao_citation_require_all=ao_citation_require_all, ao_commenter=ao_commenter, ao_representative=ao_representative, case_no=case_no, case_respondents=case_respondents, case_election_cycles=case_election_cycles, case_min_open_date=case_min_open_date, primary_subject_id=primary_subject_id, secondary_subject_id=secondary_subject_id, case_max_open_date=case_max_open_date, case_min_close_date=case_min_close_date, case_max_close_date=case_max_close_date, case_min_document_date=case_min_document_date, case_max_document_date=case_max_document_date, case_regulatory_citation=case_regulatory_citation, case_statutory_citation=case_statutory_citation, case_citation_require_all=case_citation_require_all, q_exclude=q_exclude, case_doc_category_id=case_doc_category_id, mur_type=mur_type, mur_disposition_category_id=mur_disposition_category_id, af_name=af_name, af_committee_id=af_committee_id, af_report_year=af_report_year, af_min_rtb_date=af_min_rtb_date, af_max_rtb_date=af_max_rtb_date, af_rtb_fine_amount=af_rtb_fine_amount, af_min_fd_date=af_min_fd_date, af_max_fd_date=af_max_fd_date, af_fd_fine_amount=af_fd_fine_amount, sort=sort, case_min_penalty_amount=case_min_penalty_amount, case_max_penalty_amount=case_max_penalty_amount, q_proximity=q_proximity, max_gaps=max_gaps, proximity_filter=proximity_filter, proximity_filter_term=proximity_filter_term, filename=filename, api_key=api_key)
        print("The response of LegalApi->v1_legal_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegalApi->v1_legal_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  Text to search legal documents for  | [optional] 
 **from_hit** | **int**|  Get results starting from this index  | [optional] 
 **hits_returned** | **int**|  Number of results to return (max 10)  | [optional] 
 **type** | **str**|  Choose a legal document type  | [optional] 
 **ao_no** | [**List[str]**](str.md)|  Force advisory opinion number  | [optional] 
 **ao_name** | [**List[str]**](str.md)|  Force advisory opinion name  | [optional] 
 **ao_min_issue_date** | **str**|  Earliest issue date of advisory opinion  | [optional] 
 **ao_max_issue_date** | **str**|  Latest issue date of advisory opinion  | [optional] 
 **ao_min_request_date** | **str**|  Earliest request date of advisory opinion  | [optional] 
 **ao_max_request_date** | **str**|  Latest request date of advisory opinion  | [optional] 
 **ao_min_document_date** | **str**|  Selects all advisory opinion documents dated on or after this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\&quot;  | [optional] 
 **ao_max_document_date** | **str**|  Selects all advisory opinion documents dated on or before this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\&quot;  | [optional] 
 **ao_doc_category_id** | [**List[str]**](str.md)|  Category of the document F - Final Opinion V - Votes D - Draft Documents R - AO Request, Supplemental Material, and Extensions of Time W - Withdrawal of Request C - Comments and Ex parte Communications S - Commissioner Statements  | [optional] 
 **ao_is_pending** | **bool**|  AO is pending  | [optional] 
 **ao_status** | **str**|  Status of AO (pending, withdrawn, or final)  | [optional] 
 **ao_requestor** | **str**|  The requestor of the advisory opinion  | [optional] 
 **ao_requestor_type** | [**List[str]**](str.md)|  Code of the advisory opinion requestor type. Select one or more codes to filter by advisory opinion requestor type:         - 1 - Federal candidate/candidate committee/officeholder         - 2 - Publicly funded candidates/committees         - 3 - Party committee, national         - 4 - Party committee, state or local         - 5 - Nonconnected political committee         - 6 - Separate segregated fun          - 7 - Labor Organization         - 8 - Trade Association         - 9 - Membership Organization, Cooperative, Corporation W/O Capital Stocks         - 10 - Corporation (including LLCs electing corporate status)         - 11 - Partnership (including LLCs electing partnership status)         - 12 - Governmental entity          - 13 - Research/Public Interest/Educational Institution         - 14 - Law Firm         - 15 - Individual         - 16 - Other  | [optional] 
 **ao_regulatory_citation** | [**List[str]**](str.md)|  Regulatory citations  | [optional] 
 **ao_statutory_citation** | [**List[str]**](str.md)|  Statutory citations  | [optional] 
 **ao_citation_require_all** | **bool**|  Require all citations to be in document (default behavior is any)  | [optional] 
 **ao_commenter** | **str**|  Name of commenter  | [optional] 
 **ao_representative** | **str**|  Name of representative  | [optional] 
 **case_no** | [**List[str]**](str.md)|  Enforcement matter case number  | [optional] 
 **case_respondents** | **str**|  Cases respondents  | [optional] 
 **case_election_cycles** | **int**|  Cases election cycles  | [optional] 
 **case_min_open_date** | **str**|  The earliest date opened of case  | [optional] 
 **primary_subject_id** | [**List[str]**](str.md)|  Primary Subject Description:     - 1 - Allocation     - 2 - Committees     - 3 - Contributions     - 4 - Disclaimer     - 5 - Disbursements     - 6 - Electioneering     - 7 - Expenditures     - 8 - Express Advocacy     - 9 - Foreign Nationals     - 10 - Fraudulent misrepresentation     - 11 - Issue Advocacy     - 12 - Knowing and Willful     - 13 - Loans     - 14 - Non-federal     - 15 - Other     - 16 - Personal use     - 17 - Presidential     - 18 - Reporting     - 19 - Soft Money     - 20 - Solicitation  | [optional] 
 **secondary_subject_id** | [**List[str]**](str.md)|  Secondary Subject Description:     - 1 - Candidate     - 2 - Multi-candidate     - 3 - Non-party     - 4 - PAC     - 5 - Party     - 6 - Political     - 7 - Presidential     - 8 - Corporations     - 9 - Excessive     - 10 - Exemptions     - 11 - In the name of another     - 12 - Labor unions     - 13 - Limitations     - 14 - National bank     - 15 - Prohibited     - 16 - Coordinated     - 17 - Limits     - 18 - Prohibitions  | [optional] 
 **case_max_open_date** | **str**|  The latest date opened of case  | [optional] 
 **case_min_close_date** | **str**|  The earliest date closed of case  | [optional] 
 **case_max_close_date** | **str**|  The latest date closed of case  | [optional] 
 **case_min_document_date** | **str**|  Selects all case documents dated on or after this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\&quot;  | [optional] 
 **case_max_document_date** | **str**|  Selects all case documents dated on or before this date. Date must be formatted as MM/DD/YYYY or YYYY-MM-DD.\&quot;  | [optional] 
 **case_regulatory_citation** | [**List[str]**](str.md)|  Regulatory citations  | [optional] 
 **case_statutory_citation** | [**List[str]**](str.md)|  Statutory citations  | [optional] 
 **case_citation_require_all** | **bool**|  Require all citations to be in document (default behavior is any)  | [optional] 
 **q_exclude** | **str**|  Exclude documents containing this term  | [optional] 
 **case_doc_category_id** | [**List[str]**](str.md)|  Select one or more case document category id to filter by corresponding case document category:         - 1 - Conciliation and Settlement Agreements         - 2 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 3 - General Counsel Reports, Briefs, Notifications and Responses         - 4 - Certifications         - 5 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 6 - Statement of Reasons          - 1001 - ADR Settlement Agreements         - 1002 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 1003 - ADR Memoranda, Notifications and Responses         - 1004 - Certifications         - 1005 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 1006 - Statement of Reasons          - 2001 - Administrative Fine Case  | [optional] 
 **mur_type** | **str**|  Type of MUR : current or archived  | [optional] 
 **mur_disposition_category_id** | [**List[str]**](str.md)|  Select one or more MUR disposition category id to filter by corresponding MUR disposition category:         - 1 - Conciliation-PPC         - 2 - Conciliation-PC         - 3 - Dismiss and Remind         - 4 - Dismissed         - 5 - Dismissed-Low Rated         - 6 - Dismissed-Other         - 7 - Dismissed-Stale         - 8 - Dismiss pursuant to prosecutorial discretion         - 9 - Dismiss pursuant to prosecutorial discretion, and caution         - 10 - Enforcement - Disposition - Dismissed Dismiss - Dismiss and Caution         - 11 - No PCTB         - 12 - No RTB         - 13 - PCTB Finding         - 14 - PC/NFA         - 15 - RTB Finding         - 16 - RTB/NFA         - 17 - Take no action         - 18 - Take No Further Action  | [optional] 
 **af_name** | [**List[str]**](str.md)|  Admin fine committee name  | [optional] 
 **af_committee_id** | **str**|  Admin fine committee ID  | [optional] 
 **af_report_year** | **str**|  Admin fine report year  | [optional] 
 **af_min_rtb_date** | **str**|  The earliest Reason to Believe date  | [optional] 
 **af_max_rtb_date** | **str**|  The latest Reason to Believe date  | [optional] 
 **af_rtb_fine_amount** | **int**|  Reason to Believe fine amount  | [optional] 
 **af_min_fd_date** | **str**|  The earliest Final Determination date  | [optional] 
 **af_max_fd_date** | **str**|  The latest Final Determination date  | [optional] 
 **af_fd_fine_amount** | **int**|     Final Determination fine amount  | [optional] 
 **sort** | **str**|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **case_min_penalty_amount** | **str**|  Show cases with a penalty greater than this amount  | [optional] 
 **case_max_penalty_amount** | **str**|  Show cases with a penalty less than this amount   | [optional] 
 **q_proximity** | [**List[str]**](str.md)|  This search identifies documents where the specified phrases appear near each other. The field supports both a single phrase or multiple phrases. For a single phrase, the maximum gap is applied between the words in the phrase. For multiple phrases, the maximum gap is applied between the phrases themselves.  | [optional] 
 **max_gaps** | **int**|  The maximum number of positions allowed between terms specified in &#x60;q_proximity&#x60;  | [optional] 
 **proximity_filter** | **str**|  Adds additional filters to the proximity search that provides options to specify positional constraints  | [optional] 
 **proximity_filter_term** | **str**|  Specifies the term to which the &#x60;proximity_filter&#x60; option applies to and defines what must appear in relation to the &#x60;q_proximity&#x60; phrase  | [optional] 
 **filename** | **str**|  Search documents by file name  | [optional] 
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**V1LegalSearchGetDefaultResponse**](V1LegalSearchGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Legal search results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

