# openapi_client.IndependentExpendituresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_schedules_schedule_e_efile_get**](IndependentExpendituresApi.md#v1_schedules_schedule_e_efile_get) | **GET** /v1/schedules/schedule_e/efile/ | 
[**v1_schedules_schedule_e_get**](IndependentExpendituresApi.md#v1_schedules_schedule_e_get) | **GET** /v1/schedules/schedule_e/ | 
[**v1_schedules_schedule_e_totals_by_candidate_get**](IndependentExpendituresApi.md#v1_schedules_schedule_e_totals_by_candidate_get) | **GET** /v1/schedules/schedule_e/totals/by_candidate/ | 
[**v1_schedules_schedule_eby_candidate_get**](IndependentExpendituresApi.md#v1_schedules_schedule_eby_candidate_get) | **GET** /v1/schedules/schedule_e/by_candidate/ | 


# **v1_schedules_schedule_e_efile_get**
> ScheduleEEfilePage v1_schedules_schedule_e_efile_get(page=page, per_page=per_page, candidate_search=candidate_search, committee_id=committee_id, candidate_id=candidate_id, payee_name=payee_name, image_number=image_number, support_oppose_indicator=support_oppose_indicator, min_expenditure_date=min_expenditure_date, max_expenditure_date=max_expenditure_date, min_dissemination_date=min_dissemination_date, max_dissemination_date=max_dissemination_date, min_expenditure_amount=min_expenditure_amount, max_expenditure_amount=max_expenditure_amount, spender_name=spender_name, candidate_party=candidate_party, candidate_office=candidate_office, candidate_office_state=candidate_office_state, candidate_office_district=candidate_office_district, most_recent=most_recent, min_filed_date=min_filed_date, max_filed_date=max_filed_date, filing_form=filing_form, is_notice=is_notice, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don't contain the processed and coded data that you can find on other endpoints.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_e_efile_page import ScheduleEEfilePage
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
    api_instance = openapi_client.IndependentExpendituresApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    candidate_search = ['candidate_search_example'] # List[str] |  Search for candidates by candiate id or candidate first or last name  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    candidate_id = ['candidate_id_example'] # List[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence.  (optional)
    payee_name = ['payee_name_example'] # List[str] |  Name of the entity that received the payment.  (optional)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    support_oppose_indicator = ['support_oppose_indicator_example'] # List[str] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. (optional)
    min_expenditure_date = 'min_expenditure_date_example' # str | Selects all items expended by this committee after this date (optional)
    max_expenditure_date = 'max_expenditure_date_example' # str | Selects all items expended by this committee before this date (optional)
    min_dissemination_date = 'min_dissemination_date_example' # str | Selects all items distributed by this committee after this date (optional)
    max_dissemination_date = 'max_dissemination_date_example' # str | Selects all items distributed by this committee before this date (optional)
    min_expenditure_amount = 56 # int | Selects all items expended by this committee greater than this amount (optional)
    max_expenditure_amount = 56 # int | Selects all items expended by this committee less than this amount (optional)
    spender_name = ['spender_name_example'] # List[str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)
    candidate_party = ['candidate_party_example'] # List[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
    candidate_office = 'candidate_office_example' # str | Federal office candidate runs for: H, S or P (optional)
    candidate_office_state = ['candidate_office_state_example'] # List[str] | US state or territory where a candidate runs for office (optional)
    candidate_office_district = ['candidate_office_district_example'] # List[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
    most_recent = True # bool |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included.  (optional)
    min_filed_date = 'min_filed_date_example' # str | Timestamp of electronic or paper record that FEC received (optional)
    max_filed_date = 'max_filed_date_example' # str | Timestamp of electronic or paper record that FEC received (optional)
    filing_form = ['filing_form_example'] # List[str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
    is_notice = True # bool |  Record filed as 24- or 48-hour notice.  (optional)
    sort = '-expenditure_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-expenditure_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_e_efile_get(page=page, per_page=per_page, candidate_search=candidate_search, committee_id=committee_id, candidate_id=candidate_id, payee_name=payee_name, image_number=image_number, support_oppose_indicator=support_oppose_indicator, min_expenditure_date=min_expenditure_date, max_expenditure_date=max_expenditure_date, min_dissemination_date=min_dissemination_date, max_dissemination_date=max_dissemination_date, min_expenditure_amount=min_expenditure_amount, max_expenditure_amount=max_expenditure_amount, spender_name=spender_name, candidate_party=candidate_party, candidate_office=candidate_office, candidate_office_state=candidate_office_state, candidate_office_district=candidate_office_district, most_recent=most_recent, min_filed_date=min_filed_date, max_filed_date=max_filed_date, filing_form=filing_form, is_notice=is_notice, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of IndependentExpendituresApi->v1_schedules_schedule_e_efile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndependentExpendituresApi->v1_schedules_schedule_e_efile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **candidate_search** | [**List[str]**](str.md)|  Search for candidates by candiate id or candidate first or last name  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **candidate_id** | [**List[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **payee_name** | [**List[str]**](str.md)|  Name of the entity that received the payment.  | [optional] 
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **support_oppose_indicator** | [**List[str]**](str.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] 
 **min_expenditure_date** | **str**| Selects all items expended by this committee after this date | [optional] 
 **max_expenditure_date** | **str**| Selects all items expended by this committee before this date | [optional] 
 **min_dissemination_date** | **str**| Selects all items distributed by this committee after this date | [optional] 
 **max_dissemination_date** | **str**| Selects all items distributed by this committee before this date | [optional] 
 **min_expenditure_amount** | **int**| Selects all items expended by this committee greater than this amount | [optional] 
 **max_expenditure_amount** | **int**| Selects all items expended by this committee less than this amount | [optional] 
 **spender_name** | [**List[str]**](str.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
 **candidate_party** | [**List[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **candidate_office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **candidate_office_state** | [**List[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **candidate_office_district** | [**List[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **most_recent** | **bool**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] 
 **min_filed_date** | **str**| Timestamp of electronic or paper record that FEC received | [optional] 
 **max_filed_date** | **str**| Timestamp of electronic or paper record that FEC received | [optional] 
 **filing_form** | [**List[str]**](str.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **is_notice** | **bool**|  Record filed as 24- or 48-hour notice.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-expenditure_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleEEfilePage**](ScheduleEEfilePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_schedules_schedule_e_get**
> ScheduleEPage v1_schedules_schedule_e_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, candidate_office=candidate_office, candidate_party=candidate_party, candidate_office_state=candidate_office_state, candidate_office_district=candidate_office_district, cycle=cycle, committee_id=committee_id, candidate_id=candidate_id, filing_form=filing_form, last_expenditure_date=last_expenditure_date, last_expenditure_amount=last_expenditure_amount, last_office_total_ytd=last_office_total_ytd, payee_name=payee_name, support_oppose_indicator=support_oppose_indicator, last_support_oppose_indicator=last_support_oppose_indicator, is_notice=is_notice, min_dissemination_date=min_dissemination_date, max_dissemination_date=max_dissemination_date, min_filing_date=min_filing_date, max_filing_date=max_filing_date, most_recent=most_recent, q_spender=q_spender, form_line_number=form_line_number, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule E covers the line item expenditures for independent expenditures. For example, if a super PAC
bought ads on TV to oppose a federal candidate, each ad purchase would be recorded here with
the expenditure amount, name and id of the candidate, and whether the ad supported or opposed the candidate.

An independent expenditure is an expenditure for a communication "expressly advocating the election or
defeat of a clearly identified candidate that is not made in cooperation, consultation, or concert with,
or at the request or suggestion of, a candidate, a candidate’s authorized committee, or their agents, or
a political party or its agents."

Aggregates by candidate do not include 24 and 48 hour reports. This ensures we don't double count expenditures
and the totals are more accurate. You can still find the information from 24 and 48 hour reports in
`/schedule/schedule_e/`.

Due to the large quantity of Schedule E filings, this endpoint is not paginated by
page number. Instead, you can request the next page of results by adding the values in
the `last_indexes` object from `pagination` to the URL of your last request. For
example, when sorting by `expenditure_amount`, you might receive a page of
results with the following pagination information:

```
 "pagination": {
    "count": 152623,
    "is_count_exact": True,
    "last_indexes": {
      "last_index": "3023037",
      "last_expenditure_amount": -17348.5
    },
    "per_page": 20,
    "pages": 7632
  }
}
```

To fetch the next page of sorted results, append `last_index=3023037` and
`last_expenditure_amount=` to the URL.  We strongly advise paging through
these results by using the sort indices (defaults to sort by disbursement date,
e.g. `last_disbursement_date`), otherwise some resources may be unintentionally
filtered out.  This resource uses keyset pagination to improve query performance
and these indices are required to properly page through this large dataset.

Note: because the Schedule E data includes many records, counts for
large result sets are approximate; you will want to page through the records until no records are returned.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_e_page import ScheduleEPage
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
    api_instance = openapi_client.IndependentExpendituresApi(api_client)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_image_number = 'min_image_number_example' # str | Minium image number of the page where the schedule item is reported (optional)
    max_image_number = 'max_image_number_example' # str | Maxium image number of the page where the schedule item is reported (optional)
    min_amount = 3.4 # float | Filter for all amounts greater than a value. (optional)
    max_amount = 3.4 # float | Filter for all amounts less than a value. (optional)
    min_date = 'min_date_example' # str | Minimum date (optional)
    max_date = 'max_date_example' # str | Maximum date (optional)
    candidate_office = ['candidate_office_example'] # List[str] | Federal office candidate runs for: H, S or P (optional)
    candidate_party = ['candidate_party_example'] # List[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
    candidate_office_state = ['candidate_office_state_example'] # List[str] | US state or territory (optional)
    candidate_office_district = ['candidate_office_district_example'] # List[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    candidate_id = ['candidate_id_example'] # List[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence.  (optional)
    filing_form = ['filing_form_example'] # List[str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
    last_expenditure_date = 'null' # str |  When sorting by `expenditure_date`, this is populated with the `expenditure_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.  (optional) (default to 'null')
    last_expenditure_amount = 3.4 # float |  When sorting by `expenditure_amount`, this is populated with the `expenditure_amount` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.  (optional)
    last_office_total_ytd = 3.4 # float |  When sorting by `office_total_ytd`, this is populated with the `office_total_ytd` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.'  (optional)
    payee_name = ['payee_name_example'] # List[str] |  Name of the entity that received the payment.  (optional)
    support_oppose_indicator = ['support_oppose_indicator_example'] # List[str] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. (optional)
    last_support_oppose_indicator = 'null' # str |  When sorting by `support_oppose_indicator`, this is populated with the `support_oppose_indicator` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.'  (optional) (default to 'null')
    is_notice = [True] # List[bool] |  Record filed as 24- or 48-hour notice.  (optional)
    min_dissemination_date = 'min_dissemination_date_example' # str | Selects all items distributed by this committee after this date (optional)
    max_dissemination_date = 'max_dissemination_date_example' # str | Selects all items distributed by this committee before this date (optional)
    min_filing_date = 'min_filing_date_example' # str |  Selects all filings received after this date  (optional)
    max_filing_date = 'max_filing_date_example' # str |  Selects all filings received before this date  (optional)
    most_recent = True # bool |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included.  (optional)
    q_spender = ['q_spender_example'] # List[str] |  Keyword search for spender name or ID  (optional)
    form_line_number = ['form_line_number_example'] # List[str] |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    last_index = 56 # int | Index of last result from previous page (optional)
    sort = '-expenditure_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-expenditure_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_e_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, candidate_office=candidate_office, candidate_party=candidate_party, candidate_office_state=candidate_office_state, candidate_office_district=candidate_office_district, cycle=cycle, committee_id=committee_id, candidate_id=candidate_id, filing_form=filing_form, last_expenditure_date=last_expenditure_date, last_expenditure_amount=last_expenditure_amount, last_office_total_ytd=last_office_total_ytd, payee_name=payee_name, support_oppose_indicator=support_oppose_indicator, last_support_oppose_indicator=last_support_oppose_indicator, is_notice=is_notice, min_dissemination_date=min_dissemination_date, max_dissemination_date=max_dissemination_date, min_filing_date=min_filing_date, max_filing_date=max_filing_date, most_recent=most_recent, q_spender=q_spender, form_line_number=form_line_number, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of IndependentExpendituresApi->v1_schedules_schedule_e_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndependentExpendituresApi->v1_schedules_schedule_e_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **min_image_number** | **str**| Minium image number of the page where the schedule item is reported | [optional] 
 **max_image_number** | **str**| Maxium image number of the page where the schedule item is reported | [optional] 
 **min_amount** | **float**| Filter for all amounts greater than a value. | [optional] 
 **max_amount** | **float**| Filter for all amounts less than a value. | [optional] 
 **min_date** | **str**| Minimum date | [optional] 
 **max_date** | **str**| Maximum date | [optional] 
 **candidate_office** | [**List[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional] 
 **candidate_party** | [**List[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **candidate_office_state** | [**List[str]**](str.md)| US state or territory | [optional] 
 **candidate_office_district** | [**List[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **candidate_id** | [**List[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **filing_form** | [**List[str]**](str.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **last_expenditure_date** | **str**|  When sorting by &#x60;expenditure_date&#x60;, this is populated with the &#x60;expenditure_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] [default to &#39;null&#39;]
 **last_expenditure_amount** | **float**|  When sorting by &#x60;expenditure_amount&#x60;, this is populated with the &#x60;expenditure_amount&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] 
 **last_office_total_ytd** | **float**|  When sorting by &#x60;office_total_ytd&#x60;, this is populated with the &#x60;office_total_ytd&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] 
 **payee_name** | [**List[str]**](str.md)|  Name of the entity that received the payment.  | [optional] 
 **support_oppose_indicator** | [**List[str]**](str.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] 
 **last_support_oppose_indicator** | **str**|  When sorting by &#x60;support_oppose_indicator&#x60;, this is populated with the &#x60;support_oppose_indicator&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] [default to &#39;null&#39;]
 **is_notice** | [**List[bool]**](bool.md)|  Record filed as 24- or 48-hour notice.  | [optional] 
 **min_dissemination_date** | **str**| Selects all items distributed by this committee after this date | [optional] 
 **max_dissemination_date** | **str**| Selects all items distributed by this committee before this date | [optional] 
 **min_filing_date** | **str**|  Selects all filings received after this date  | [optional] 
 **max_filing_date** | **str**|  Selects all filings received before this date  | [optional] 
 **most_recent** | **bool**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] 
 **q_spender** | [**List[str]**](str.md)|  Keyword search for spender name or ID  | [optional] 
 **form_line_number** | [**List[str]**](str.md)|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-expenditure_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleEPage**](ScheduleEPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_schedules_schedule_e_totals_by_candidate_get**
> IETotalsByCandidatePage v1_schedules_schedule_e_totals_by_candidate_get(page=page, per_page=per_page, cycle=cycle, candidate_id=candidate_id, election_full=election_full, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Total independent expenditure on supported or opposed candidates by cycle or candidate election year.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.ie_totals_by_candidate_page import IETotalsByCandidatePage
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
    api_instance = openapi_client.IndependentExpendituresApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    candidate_id = ['candidate_id_example'] # List[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence.  (optional)
    election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
    sort = ['sort_example'] # List[str] | Provide a field to sort by. Use `-` for descending order.  (optional)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_e_totals_by_candidate_get(page=page, per_page=per_page, cycle=cycle, candidate_id=candidate_id, election_full=election_full, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of IndependentExpendituresApi->v1_schedules_schedule_e_totals_by_candidate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndependentExpendituresApi->v1_schedules_schedule_e_totals_by_candidate_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **candidate_id** | [**List[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **sort** | [**List[str]**](str.md)| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**IETotalsByCandidatePage**](IETotalsByCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_schedules_schedule_eby_candidate_get**
> ScheduleEByCandidatePage v1_schedules_schedule_eby_candidate_get(page=page, per_page=per_page, state=state, district=district, cycle=cycle, office=office, election_full=election_full, candidate_id=candidate_id, committee_id=committee_id, support_oppose=support_oppose, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule E receipts aggregated by recipient candidate. To avoid double
counting, memoed items are not included.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_eby_candidate_page import ScheduleEByCandidatePage
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
    api_instance = openapi_client.IndependentExpendituresApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
    district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
    election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
    candidate_id = ['candidate_id_example'] # List[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence.  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    support_oppose = null # str | Support or opposition (optional) (default to null)
    sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_eby_candidate_get(page=page, per_page=per_page, state=state, district=district, cycle=cycle, office=office, election_full=election_full, candidate_id=candidate_id, committee_id=committee_id, support_oppose=support_oppose, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of IndependentExpendituresApi->v1_schedules_schedule_eby_candidate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndependentExpendituresApi->v1_schedules_schedule_eby_candidate_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **state** | **str**| US state or territory where a candidate runs for office | [optional] 
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **candidate_id** | [**List[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **support_oppose** | **str**| Support or opposition | [optional] [default to null]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleEByCandidatePage**](ScheduleEByCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

