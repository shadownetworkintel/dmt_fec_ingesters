# openapi_client.FinancialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_committee_committee_id_reports_get**](FinancialApi.md#v1_committee_committee_id_reports_get) | **GET** /v1/committee/{committee_id}/reports/ | 
[**v1_committee_committee_id_totals_get**](FinancialApi.md#v1_committee_committee_id_totals_get) | **GET** /v1/committee/{committee_id}/totals/ | 
[**v1_elections_get**](FinancialApi.md#v1_elections_get) | **GET** /v1/elections/ | 
[**v1_elections_search_get**](FinancialApi.md#v1_elections_search_get) | **GET** /v1/elections/search/ | 
[**v1_elections_summary_get**](FinancialApi.md#v1_elections_summary_get) | **GET** /v1/elections/summary/ | 
[**v1_reports_entity_type_get**](FinancialApi.md#v1_reports_entity_type_get) | **GET** /v1/reports/{entity_type}/ | 
[**v1_totals_by_entity_get**](FinancialApi.md#v1_totals_by_entity_get) | **GET** /v1/totals/by_entity/ | 
[**v1_totals_entity_type_get**](FinancialApi.md#v1_totals_entity_type_get) | **GET** /v1/totals/{entity_type}/ | 
[**v1_totals_inaugural_committees_by_contributor_get**](FinancialApi.md#v1_totals_inaugural_committees_by_contributor_get) | **GET** /v1/totals/inaugural_committees/by_contributor/ | 


# **v1_committee_committee_id_reports_get**
> CommitteeReportsPage v1_committee_committee_id_reports_get(committee_id, page=page, per_page=per_page, year=year, cycle=cycle, beginning_image_number=beginning_image_number, report_type=report_type, is_amended=is_amended, min_disbursements_amount=min_disbursements_amount, max_disbursements_amount=max_disbursements_amount, min_receipts_amount=min_receipts_amount, max_receipts_amount=max_receipts_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, min_debts_owed_amount=min_debts_owed_amount, max_debts_owed_expenditures=max_debts_owed_expenditures, min_independent_expenditures=min_independent_expenditures, max_independent_expenditures=max_independent_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_total_contributions=min_total_contributions, max_total_contributions=max_total_contributions, type=type, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Each report represents the summary information from Form 3, Form 3X and Form 3P.
These reports have key statistics that illuminate the financial status of a given committee.
Things like cash on hand, debts owed by committee, total receipts, and total disbursements
are especially helpful for understanding a committee's financial dealings.

By default, this endpoint includes both amended and final versions of each report. To restrict
to only the final versions of each report, use `is_amended=false`; to retrieve only reports that
have been amended, use `is_amended=true`.

Several different reporting structures exist, depending on the type of organization that
submits financial information. To see an example of these reporting requirements,
look at the summary and detailed summary pages of Form 3, Form 3X, and Form 3P.

DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly
label these fields while conveying clear meaning to ensure accessibility for all users.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.committee_reports_page import CommitteeReportsPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits. 
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    year = [56] # List[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    beginning_image_number = ['beginning_image_number_example'] # List[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
    report_type = ['report_type_example'] # List[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
    is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
    min_disbursements_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_disbursements_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_receipts_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_receipts_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_cash_on_hand_end_period_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_cash_on_hand_end_period_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_debts_owed_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_debts_owed_expenditures = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_independent_expenditures = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_independent_expenditures = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_party_coordinated_expenditures = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_party_coordinated_expenditures = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_total_contributions = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_total_contributions = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    type = ['type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    sort = ['sort_example'] # List[str] | Provide a field to sort by. Use `-` for descending order.  (optional)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_committee_committee_id_reports_get(committee_id, page=page, per_page=per_page, year=year, cycle=cycle, beginning_image_number=beginning_image_number, report_type=report_type, is_amended=is_amended, min_disbursements_amount=min_disbursements_amount, max_disbursements_amount=max_disbursements_amount, min_receipts_amount=min_receipts_amount, max_receipts_amount=max_receipts_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, min_debts_owed_amount=min_debts_owed_amount, max_debts_owed_expenditures=max_debts_owed_expenditures, min_independent_expenditures=min_independent_expenditures, max_independent_expenditures=max_independent_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_total_contributions=min_total_contributions, max_total_contributions=max_total_contributions, type=type, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_committee_committee_id_reports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_committee_committee_id_reports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **year** | [**List[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **beginning_image_number** | [**List[str]**](str.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 
 **report_type** | [**List[str]**](str.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional] 
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **min_disbursements_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_disbursements_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_receipts_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_receipts_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_cash_on_hand_end_period_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_cash_on_hand_end_period_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_debts_owed_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_debts_owed_expenditures** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_independent_expenditures** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_independent_expenditures** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_party_coordinated_expenditures** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_party_coordinated_expenditures** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_total_contributions** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_total_contributions** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **sort** | [**List[str]**](str.md)| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

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

# **v1_committee_committee_id_totals_get**
> CommitteeTotalsPage v1_committee_committee_id_totals_get(committee_id, page=page, per_page=per_page, cycle=cycle, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports,
which are aggregated by two-year period. We refer to two-year periods as a `cycle`.

The cycle is named after the even-numbered year and includes the year before it. To obtain
totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle
is the next year — for example, in 2015, the current cycle is 2016.

For presidential and Senate candidates, multiple two-year cycles exist between elections.



### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.committee_totals_page import CommitteeTotalsPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits. 
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_committee_committee_id_totals_get(committee_id, page=page, per_page=per_page, cycle=cycle, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_committee_committee_id_totals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_committee_committee_id_totals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

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

# **v1_elections_get**
> ElectionPage v1_elections_get(cycle, office, page=page, per_page=per_page, state=state, district=district, election_full=election_full, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Look at the top-level financial information for all candidates running for the same
office.

Choose a 2-year cycle, and `house`, `senate` or `presidential`.

If you are looking for a Senate seat, you will need to select the state using a two-letter
abbreviation.

House races require state and a two-digit district number.

Since this endpoint reflects financial information, it will only have candidates once they file
financial reporting forms. Query the `/candidates` endpoint to retrieve an-up-to-date list of all the
candidates that filed to run for a particular seat.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.election_page import ElectionPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    office = 'office_example' # str | Federal office candidate runs for: H, S or P
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
    district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
    election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
    sort = '-total_receipts' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-total_receipts')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_elections_get(cycle, office, page=page, per_page=per_page, state=state, district=district, election_full=election_full, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_elections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_elections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **office** | **str**| Federal office candidate runs for: H, S or P | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **state** | **str**| US state or territory where a candidate runs for office | [optional] 
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-total_receipts&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ElectionPage**](ElectionPage.md)

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

# **v1_elections_search_get**
> ElectionsListPage v1_elections_search_get(page=page, per_page=per_page, state=state, district=district, cycle=cycle, zip=zip, office=office, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


List elections by cycle, office, state, and district.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.elections_list_page import ElectionsListPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    state = ['state_example'] # List[str] | US state or territory where a candidate runs for office (optional)
    district = ['district_example'] # List[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
    cycle = [56] # List[int] |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
    zip = [56] # List[int] | Zip code (optional)
    office = ['office_example'] # List[str] |  (optional)
    sort = ['sort_example'] # List[str] | Provide a field to sort by. Use `-` for descending order.  (optional)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_elections_search_get(page=page, per_page=per_page, state=state, district=district, cycle=cycle, zip=zip, office=office, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_elections_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_elections_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **state** | [**List[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **district** | [**List[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **cycle** | [**List[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **zip** | [**List[int]**](int.md)| Zip code | [optional] 
 **office** | [**List[str]**](str.md)|  | [optional] 
 **sort** | [**List[str]**](str.md)| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ElectionsListPage**](ElectionsListPage.md)

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

# **v1_elections_summary_get**
> ElectionSummary v1_elections_summary_get(cycle, office, state=state, district=district, election_full=election_full, api_key=api_key)


List elections by cycle, office, state, and district.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.election_summary import ElectionSummary
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
    api_instance = openapi_client.FinancialApi(api_client)
    cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    office = 'office_example' # str | Federal office candidate runs for: H, S or P
    state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
    district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
    election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_elections_summary_get(cycle, office, state=state, district=district, election_full=election_full, api_key=api_key)
        print("The response of FinancialApi->v1_elections_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_elections_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **office** | **str**| Federal office candidate runs for: H, S or P | 
 **state** | **str**| US state or territory where a candidate runs for office | [optional] 
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ElectionSummary**](ElectionSummary.md)

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

# **v1_reports_entity_type_get**
> CommitteeReportsPage v1_reports_entity_type_get(entity_type, page=page, per_page=per_page, year=year, cycle=cycle, beginning_image_number=beginning_image_number, report_type=report_type, is_amended=is_amended, most_recent=most_recent, filer_type=filer_type, min_disbursements_amount=min_disbursements_amount, max_disbursements_amount=max_disbursements_amount, min_receipts_amount=min_receipts_amount, max_receipts_amount=max_receipts_amount, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, min_debts_owed_amount=min_debts_owed_amount, max_debts_owed_expenditures=max_debts_owed_expenditures, min_independent_expenditures=min_independent_expenditures, max_independent_expenditures=max_independent_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_total_contributions=min_total_contributions, max_total_contributions=max_total_contributions, committee_type=committee_type, candidate_id=candidate_id, committee_id=committee_id, amendment_indicator=amendment_indicator, q_filer=q_filer, q_spender=q_spender, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Each report represents the summary information from Form 3, Form 3X and Form 3P.
These reports have key statistics that illuminate the financial status of a given committee.
Things like cash on hand, debts owed by committee, total receipts, and total disbursements
are especially helpful for understanding a committee's financial dealings.

By default, this endpoint includes both amended and final versions of each report. To restrict
to only the final versions of each report, use `is_amended=false`; to retrieve only reports that
have been amended, use `is_amended=true`.

Several different reporting structures exist, depending on the type of organization that
submits financial information. To see an example of these reporting requirements,
look at the summary and detailed summary pages of Form 3, Form 3X, and Form 3P.

DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly
label these fields while conveying clear meaning to ensure accessibility for all users.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.committee_reports_page import CommitteeReportsPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    entity_type = 'entity_type_example' # str | Committee groupings based on FEC filing form.                 Choose one of: `presidential`, `pac-party`, `house-senate`, or `ie-only`
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    year = [56] # List[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    beginning_image_number = ['beginning_image_number_example'] # List[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
    report_type = ['report_type_example'] # List[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
    is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
    most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
    filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
    min_disbursements_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_disbursements_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_receipts_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_receipts_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    max_receipt_date = 'max_receipt_date_example' # str |  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    min_receipt_date = 'min_receipt_date_example' # str |  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    min_cash_on_hand_end_period_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_cash_on_hand_end_period_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_debts_owed_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_debts_owed_expenditures = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_independent_expenditures = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_independent_expenditures = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_party_coordinated_expenditures = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_party_coordinated_expenditures = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_total_contributions = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_total_contributions = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    committee_type = ['committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    candidate_id = ['candidate_id_example'] # List[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence.  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    amendment_indicator = ['amendment_indicator_example'] # List[str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
    q_filer = ['q_filer_example'] # List[str] |  Keyword search for filer name or ID  (optional)
    q_spender = ['q_spender_example'] # List[str] |  Keyword search for spender name or ID  (optional)
    sort = ['sort_example'] # List[str] | Provide a field to sort by. Use `-` for descending order.  (optional)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_reports_entity_type_get(entity_type, page=page, per_page=per_page, year=year, cycle=cycle, beginning_image_number=beginning_image_number, report_type=report_type, is_amended=is_amended, most_recent=most_recent, filer_type=filer_type, min_disbursements_amount=min_disbursements_amount, max_disbursements_amount=max_disbursements_amount, min_receipts_amount=min_receipts_amount, max_receipts_amount=max_receipts_amount, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, min_debts_owed_amount=min_debts_owed_amount, max_debts_owed_expenditures=max_debts_owed_expenditures, min_independent_expenditures=min_independent_expenditures, max_independent_expenditures=max_independent_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_total_contributions=min_total_contributions, max_total_contributions=max_total_contributions, committee_type=committee_type, candidate_id=candidate_id, committee_id=committee_id, amendment_indicator=amendment_indicator, q_filer=q_filer, q_spender=q_spender, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_reports_entity_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_reports_entity_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Committee groupings based on FEC filing form.                 Choose one of: &#x60;presidential&#x60;, &#x60;pac-party&#x60;, &#x60;house-senate&#x60;, or &#x60;ie-only&#x60; | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **year** | [**List[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **beginning_image_number** | [**List[str]**](str.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 
 **report_type** | [**List[str]**](str.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional] 
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **most_recent** | **bool**|  Report is either new or is the most-recently filed amendment  | [optional] 
 **filer_type** | **str**| The method used to file with the FEC, either electronic or on paper. | [optional] 
 **min_disbursements_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_disbursements_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_receipts_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_receipts_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **max_receipt_date** | **str**|  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_receipt_date** | **str**|  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_cash_on_hand_end_period_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_cash_on_hand_end_period_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_debts_owed_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_debts_owed_expenditures** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_independent_expenditures** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_independent_expenditures** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_party_coordinated_expenditures** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_party_coordinated_expenditures** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_total_contributions** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_total_contributions** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **candidate_id** | [**List[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **amendment_indicator** | [**List[str]**](str.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
 **q_filer** | [**List[str]**](str.md)|  Keyword search for filer name or ID  | [optional] 
 **q_spender** | [**List[str]**](str.md)|  Keyword search for spender name or ID  | [optional] 
 **sort** | [**List[str]**](str.md)| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

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

# **v1_totals_by_entity_get**
> EntityReceiptDisbursementTotalsPage v1_totals_by_entity_get(cycle, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Provides cumulative receipt totals by entity type, over a two year cycle. Totals are adjusted to avoid double counting.

This is [the sql](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V41__large_aggregates.sql) that creates these calculations.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.entity_receipt_disbursement_totals_page import EntityReceiptDisbursementTotalsPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    cycle = 56 # int |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    sort = 'end_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'end_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_totals_by_entity_get(cycle, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_totals_by_entity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_totals_by_entity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;end_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**EntityReceiptDisbursementTotalsPage**](EntityReceiptDisbursementTotalsPage.md)

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

# **v1_totals_entity_type_get**
> CommitteeTotalsPage v1_totals_entity_type_get(entity_type, page=page, per_page=per_page, cycle=cycle, committee_designation=committee_designation, committee_id=committee_id, committee_type=committee_type, committee_state=committee_state, filing_frequency=filing_frequency, treasurer_name=treasurer_name, min_disbursements=min_disbursements, max_disbursements=max_disbursements, min_receipts=min_receipts, max_receipts=max_receipts, min_last_cash_on_hand_end_period=min_last_cash_on_hand_end_period, max_last_cash_on_hand_end_period=max_last_cash_on_hand_end_period, min_last_debts_owed_by_committee=min_last_debts_owed_by_committee, max_last_debts_owed_by_committee=max_last_debts_owed_by_committee, sponsor_candidate_id=sponsor_candidate_id, organization_type=organization_type, min_first_f1_date=min_first_f1_date, max_first_f1_date=max_first_f1_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports,
which are aggregated by two-year period. We refer to two-year periods as a `cycle`.

The cycle is named after the even-numbered year and includes the year before it. To obtain
totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle
is the next year — for example, in 2015, the current cycle is 2016.

For presidential and Senate candidates, multiple two-year cycles exist between elections.



### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.committee_totals_page import CommitteeTotalsPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    entity_type = 'entity_type_example' # str | Committee groupings based on FEC filing form.                 Choose one of: `presidential`, `pac`, `party`, `pac-party`,                 `house-senate`, or `ie-only`
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    committee_designation = ['committee_designation_example'] # List[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    committee_type = ['committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    committee_state = ['committee_state_example'] # List[str] | US state or territory (optional)
    filing_frequency = ['filing_frequency_example'] # List[str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
    treasurer_name = ['treasurer_name_example'] # List[str] | Name of the Committee's treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. (optional)
    min_disbursements = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_disbursements = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_receipts = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_receipts = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_last_cash_on_hand_end_period = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_last_cash_on_hand_end_period = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_last_debts_owed_by_committee = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_last_debts_owed_by_committee = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    sponsor_candidate_id = ['sponsor_candidate_id_example'] # List[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. This is a filter for Leadership PAC sponsor.  (optional)
    organization_type = ['organization_type_example'] # List[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
    min_first_f1_date = 'min_first_f1_date_example' # str | Filter for committees whose first Form 1 was received on or after this date. (optional)
    max_first_f1_date = 'max_first_f1_date_example' # str | Filter for committees whose first Form 1 was received on or before this date. (optional)
    sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_totals_entity_type_get(entity_type, page=page, per_page=per_page, cycle=cycle, committee_designation=committee_designation, committee_id=committee_id, committee_type=committee_type, committee_state=committee_state, filing_frequency=filing_frequency, treasurer_name=treasurer_name, min_disbursements=min_disbursements, max_disbursements=max_disbursements, min_receipts=min_receipts, max_receipts=max_receipts, min_last_cash_on_hand_end_period=min_last_cash_on_hand_end_period, max_last_cash_on_hand_end_period=max_last_cash_on_hand_end_period, min_last_debts_owed_by_committee=min_last_debts_owed_by_committee, max_last_debts_owed_by_committee=max_last_debts_owed_by_committee, sponsor_candidate_id=sponsor_candidate_id, organization_type=organization_type, min_first_f1_date=min_first_f1_date, max_first_f1_date=max_first_f1_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_totals_entity_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_totals_entity_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Committee groupings based on FEC filing form.                 Choose one of: &#x60;presidential&#x60;, &#x60;pac&#x60;, &#x60;party&#x60;, &#x60;pac-party&#x60;,                 &#x60;house-senate&#x60;, or &#x60;ie-only&#x60; | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **committee_designation** | [**List[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **committee_state** | [**List[str]**](str.md)| US state or territory | [optional] 
 **filing_frequency** | [**List[str]**](str.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **treasurer_name** | [**List[str]**](str.md)| Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
 **min_disbursements** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_disbursements** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_receipts** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_receipts** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_last_cash_on_hand_end_period** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_last_cash_on_hand_end_period** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_last_debts_owed_by_committee** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_last_debts_owed_by_committee** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **sponsor_candidate_id** | [**List[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. This is a filter for Leadership PAC sponsor.  | [optional] 
 **organization_type** | [**List[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **min_first_f1_date** | **str**| Filter for committees whose first Form 1 was received on or after this date. | [optional] 
 **max_first_f1_date** | **str**| Filter for committees whose first Form 1 was received on or before this date. | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

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

# **v1_totals_inaugural_committees_by_contributor_get**
> InauguralDonationsPage v1_totals_inaugural_committees_by_contributor_get(page=page, per_page=per_page, committee_id=committee_id, contributor_name=contributor_name, cycle=cycle, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


This endpoint provides information about an inaugural committee's Form 13 report of donations accepted.
The data is aggregated by the contributor and the two-year period. We refer to two-year periods as a `cycle`.



### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.inaugural_donations_page import InauguralDonationsPage
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
    api_instance = openapi_client.FinancialApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    contributor_name = ['contributor_name_example'] # List[str] | Name of contributor (optional)
    cycle = [56] # List[int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
    sort = ['sort_example'] # List[str] | Provide a field to sort by. Use `-` for descending order.  (optional)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_totals_inaugural_committees_by_contributor_get(page=page, per_page=per_page, committee_id=committee_id, contributor_name=contributor_name, cycle=cycle, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FinancialApi->v1_totals_inaugural_committees_by_contributor_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialApi->v1_totals_inaugural_committees_by_contributor_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **contributor_name** | [**List[str]**](str.md)| Name of contributor | [optional] 
 **cycle** | [**List[int]**](int.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sort** | [**List[str]**](str.md)| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**InauguralDonationsPage**](InauguralDonationsPage.md)

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

