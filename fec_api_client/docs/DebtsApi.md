# openapi_client.DebtsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_schedules_schedule_d_get**](DebtsApi.md#v1_schedules_schedule_d_get) | **GET** /v1/schedules/schedule_d/ | 
[**v1_schedules_schedule_d_sub_id_get**](DebtsApi.md#v1_schedules_schedule_d_sub_id_get) | **GET** /v1/schedules/schedule_d/{sub_id}/ | 


# **v1_schedules_schedule_d_get**
> ScheduleDPage v1_schedules_schedule_d_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_payment_period=min_payment_period, max_payment_period=max_payment_period, min_amount_incurred=min_amount_incurred, max_amount_incurred=max_amount_incurred, min_amount_outstanding_beginning=min_amount_outstanding_beginning, max_amount_outstanding_beginning=max_amount_outstanding_beginning, min_amount_outstanding_close=min_amount_outstanding_close, max_amount_outstanding_close=max_amount_outstanding_close, creditor_debtor_name=creditor_debtor_name, nature_of_debt=nature_of_debt, committee_id=committee_id, min_coverage_end_date=min_coverage_end_date, max_coverage_end_date=max_coverage_end_date, min_coverage_start_date=min_coverage_start_date, max_coverage_start_date=max_coverage_start_date, report_year=report_year, report_type=report_type, form_line_number=form_line_number, committee_type=committee_type, filing_form=filing_form, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule D, it shows debts and obligations owed to or by the committee that are
required to be disclosed.




### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_d_page import ScheduleDPage
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
    api_instance = openapi_client.DebtsApi(api_client)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_image_number = 'min_image_number_example' # str | Minium image number of the page where the schedule item is reported (optional)
    max_image_number = 'max_image_number_example' # str | Maxium image number of the page where the schedule item is reported (optional)
    min_payment_period = 3.4 # float |  (optional)
    max_payment_period = 3.4 # float |  (optional)
    min_amount_incurred = 3.4 # float |  (optional)
    max_amount_incurred = 3.4 # float |  (optional)
    min_amount_outstanding_beginning = 3.4 # float |  (optional)
    max_amount_outstanding_beginning = 3.4 # float |  (optional)
    min_amount_outstanding_close = 3.4 # float |  (optional)
    max_amount_outstanding_close = 3.4 # float |  (optional)
    creditor_debtor_name = ['creditor_debtor_name_example'] # List[str] |  (optional)
    nature_of_debt = 'nature_of_debt_example' # str |  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    min_coverage_end_date = 'null' # str |  Ending date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional) (default to 'null')
    max_coverage_end_date = 'null' # str |  Ending date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional) (default to 'null')
    min_coverage_start_date = 'null' # str |  Starting date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional) (default to 'null')
    max_coverage_start_date = 'null' # str |  Starting date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional) (default to 'null')
    report_year = [56] # List[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
    report_type = ['report_type_example'] # List[str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)
    form_line_number = ['form_line_number_example'] # List[str] |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
    committee_type = ['committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    filing_form = ['filing_form_example'] # List[str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    sort = '-coverage_end_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-coverage_end_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_d_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_payment_period=min_payment_period, max_payment_period=max_payment_period, min_amount_incurred=min_amount_incurred, max_amount_incurred=max_amount_incurred, min_amount_outstanding_beginning=min_amount_outstanding_beginning, max_amount_outstanding_beginning=max_amount_outstanding_beginning, min_amount_outstanding_close=min_amount_outstanding_close, max_amount_outstanding_close=max_amount_outstanding_close, creditor_debtor_name=creditor_debtor_name, nature_of_debt=nature_of_debt, committee_id=committee_id, min_coverage_end_date=min_coverage_end_date, max_coverage_end_date=max_coverage_end_date, min_coverage_start_date=min_coverage_start_date, max_coverage_start_date=max_coverage_start_date, report_year=report_year, report_type=report_type, form_line_number=form_line_number, committee_type=committee_type, filing_form=filing_form, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DebtsApi->v1_schedules_schedule_d_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebtsApi->v1_schedules_schedule_d_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **min_image_number** | **str**| Minium image number of the page where the schedule item is reported | [optional] 
 **max_image_number** | **str**| Maxium image number of the page where the schedule item is reported | [optional] 
 **min_payment_period** | **float**|  | [optional] 
 **max_payment_period** | **float**|  | [optional] 
 **min_amount_incurred** | **float**|  | [optional] 
 **max_amount_incurred** | **float**|  | [optional] 
 **min_amount_outstanding_beginning** | **float**|  | [optional] 
 **max_amount_outstanding_beginning** | **float**|  | [optional] 
 **min_amount_outstanding_close** | **float**|  | [optional] 
 **max_amount_outstanding_close** | **float**|  | [optional] 
 **creditor_debtor_name** | [**List[str]**](str.md)|  | [optional] 
 **nature_of_debt** | **str**|  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **min_coverage_end_date** | **str**|  Ending date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] [default to &#39;null&#39;]
 **max_coverage_end_date** | **str**|  Ending date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] [default to &#39;null&#39;]
 **min_coverage_start_date** | **str**|  Starting date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] [default to &#39;null&#39;]
 **max_coverage_start_date** | **str**|  Starting date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] [default to &#39;null&#39;]
 **report_year** | [**List[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **report_type** | [**List[str]**](str.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **form_line_number** | [**List[str]**](str.md)|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **filing_form** | [**List[str]**](str.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F24  24/48 Hour Report of Independent Expenditures     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-coverage_end_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleDPage**](ScheduleDPage.md)

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

# **v1_schedules_schedule_d_sub_id_get**
> ScheduleDPage v1_schedules_schedule_d_sub_id_get(sub_id, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule D, it shows debts and obligations owed to or by the committee that are
required to be disclosed.




### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_d_page import ScheduleDPage
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
    api_instance = openapi_client.DebtsApi(api_client)
    sub_id = 'sub_id_example' # str | 
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    sort = '-coverage_end_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-coverage_end_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_d_sub_id_get(sub_id, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DebtsApi->v1_schedules_schedule_d_sub_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebtsApi->v1_schedules_schedule_d_sub_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**|  | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-coverage_end_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleDPage**](ScheduleDPage.md)

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

