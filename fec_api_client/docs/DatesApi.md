# openapi_client.DatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_calendar_dates_export_get**](DatesApi.md#v1_calendar_dates_export_get) | **GET** /v1/calendar-dates/export/ | 
[**v1_calendar_dates_get**](DatesApi.md#v1_calendar_dates_get) | **GET** /v1/calendar-dates/ | 
[**v1_election_dates_get**](DatesApi.md#v1_election_dates_get) | **GET** /v1/election-dates/ | 
[**v1_reporting_dates_get**](DatesApi.md#v1_reporting_dates_get) | **GET** /v1/reporting-dates/ | 


# **v1_calendar_dates_export_get**
> CalendarDatePage v1_calendar_dates_export_get(renderer=renderer, page=page, per_page=per_page, calendar_category_id=calendar_category_id, description=description, summary=summary, min_start_date=min_start_date, min_end_date=min_end_date, max_start_date=max_start_date, max_end_date=max_end_date, event_id=event_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Returns CSV or ICS for downloading directly into calendar applications like Google, Outlook or other applications.

Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other
events into one calendar.

State filtering now applies to elections, reports and reporting periods.

Presidential pre-primary report due dates are not shown on even years.
Filers generally opt to file monthly rather than submit over 50 pre-primary election
reports. All reporting deadlines are available at /reporting-dates/ for reference.

This is [the sql function](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V40__omnibus_dates.sql)
that creates the calendar.



### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.calendar_date_page import CalendarDatePage
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
    api_instance = openapi_client.DatesApi(api_client)
    renderer = ics # str |  (optional) (default to ics)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    calendar_category_id = [56] # List[int] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  (optional)
    description = ['description_example'] # List[str] | Brief description of event (optional)
    summary = ['summary_example'] # List[str] | Longer description of event (optional)
    min_start_date = 'min_start_date_example' # str |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    min_end_date = 'min_end_date_example' # str |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_start_date = 'max_start_date_example' # str |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_end_date = 'max_end_date_example' # str |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    event_id = 56 # int | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. (optional)
    sort = '-start_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-start_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_calendar_dates_export_get(renderer=renderer, page=page, per_page=per_page, calendar_category_id=calendar_category_id, description=description, summary=summary, min_start_date=min_start_date, min_end_date=min_end_date, max_start_date=max_start_date, max_end_date=max_end_date, event_id=event_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DatesApi->v1_calendar_dates_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatesApi->v1_calendar_dates_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **renderer** | **str**|  | [optional] [default to ics]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **calendar_category_id** | [**List[int]**](int.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
 **description** | [**List[str]**](str.md)| Brief description of event | [optional] 
 **summary** | [**List[str]**](str.md)| Longer description of event | [optional] 
 **min_start_date** | **str**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_end_date** | **str**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_start_date** | **str**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_end_date** | **str**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **event_id** | **int**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-start_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

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

# **v1_calendar_dates_get**
> CalendarDatePage v1_calendar_dates_get(page=page, per_page=per_page, calendar_category_id=calendar_category_id, description=description, summary=summary, min_start_date=min_start_date, min_end_date=min_end_date, max_start_date=max_start_date, max_end_date=max_end_date, event_id=event_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other
events into one calendar.

State and report type filtering is no longer available.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.calendar_date_page import CalendarDatePage
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
    api_instance = openapi_client.DatesApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    calendar_category_id = [56] # List[int] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  (optional)
    description = ['description_example'] # List[str] | Brief description of event (optional)
    summary = ['summary_example'] # List[str] | Longer description of event (optional)
    min_start_date = 'min_start_date_example' # str |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    min_end_date = 'min_end_date_example' # str |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_start_date = 'max_start_date_example' # str |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_end_date = 'max_end_date_example' # str |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    event_id = 56 # int | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. (optional)
    sort = '-start_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-start_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_calendar_dates_get(page=page, per_page=per_page, calendar_category_id=calendar_category_id, description=description, summary=summary, min_start_date=min_start_date, min_end_date=min_end_date, max_start_date=max_start_date, max_end_date=max_end_date, event_id=event_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DatesApi->v1_calendar_dates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatesApi->v1_calendar_dates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **calendar_category_id** | [**List[int]**](int.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
 **description** | [**List[str]**](str.md)| Brief description of event | [optional] 
 **summary** | [**List[str]**](str.md)| Longer description of event | [optional] 
 **min_start_date** | **str**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_end_date** | **str**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_start_date** | **str**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_end_date** | **str**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **event_id** | **int**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-start_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

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

# **v1_election_dates_get**
> ElectionDatesPage v1_election_dates_get(page=page, per_page=per_page, election_state=election_state, election_district=election_district, election_party=election_party, office_sought=office_sought, min_election_date=min_election_date, max_election_date=max_election_date, election_type_id=election_type_id, min_create_date=min_create_date, max_create_date=max_create_date, min_update_date=min_update_date, max_update_date=max_update_date, election_year=election_year, min_primary_general_date=min_primary_general_date, max_primary_general_date=max_primary_general_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


FEC election dates since 1995.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.election_dates_page import ElectionDatesPage
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
    api_instance = openapi_client.DatesApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    election_state = ['election_state_example'] # List[str] |  State or territory of the office sought.  (optional)
    election_district = ['election_district_example'] # List[str] |  House district of the office sought, if applicable.  (optional)
    election_party = ['election_party_example'] # List[str] |  Party, if applicable.  (optional)
    office_sought = ['office_sought_example'] # List[str] |  House, Senate or presidential office.  (optional)
    min_election_date = 'min_election_date_example' # str |  The minimum date of election.  (optional)
    max_election_date = 'max_election_date_example' # str |  The maximum date of election.  (optional)
    election_type_id = ['election_type_id_example'] # List[str] |  Election type id  (optional)
    min_create_date = 'min_create_date_example' # str |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_create_date = 'max_create_date_example' # str |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    min_update_date = 'min_update_date_example' # str |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_update_date = 'max_update_date_example' # str |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    election_year = ['election_year_example'] # List[str] | Year of election (optional)
    min_primary_general_date = 'min_primary_general_date_example' # str |  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_primary_general_date = 'max_primary_general_date_example' # str |  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    sort = '-election_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-election_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_election_dates_get(page=page, per_page=per_page, election_state=election_state, election_district=election_district, election_party=election_party, office_sought=office_sought, min_election_date=min_election_date, max_election_date=max_election_date, election_type_id=election_type_id, min_create_date=min_create_date, max_create_date=max_create_date, min_update_date=min_update_date, max_update_date=max_update_date, election_year=election_year, min_primary_general_date=min_primary_general_date, max_primary_general_date=max_primary_general_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DatesApi->v1_election_dates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatesApi->v1_election_dates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **election_state** | [**List[str]**](str.md)|  State or territory of the office sought.  | [optional] 
 **election_district** | [**List[str]**](str.md)|  House district of the office sought, if applicable.  | [optional] 
 **election_party** | [**List[str]**](str.md)|  Party, if applicable.  | [optional] 
 **office_sought** | [**List[str]**](str.md)|  House, Senate or presidential office.  | [optional] 
 **min_election_date** | **str**|  The minimum date of election.  | [optional] 
 **max_election_date** | **str**|  The maximum date of election.  | [optional] 
 **election_type_id** | [**List[str]**](str.md)|  Election type id  | [optional] 
 **min_create_date** | **str**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_create_date** | **str**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_update_date** | **str**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_update_date** | **str**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **election_year** | [**List[str]**](str.md)| Year of election | [optional] 
 **min_primary_general_date** | **str**|  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_primary_general_date** | **str**|  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-election_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ElectionDatesPage**](ElectionDatesPage.md)

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

# **v1_reporting_dates_get**
> ReportingDatesPage v1_reporting_dates_get(page=page, per_page=per_page, min_due_date=min_due_date, max_due_date=max_due_date, report_year=report_year, report_type=report_type, min_create_date=min_create_date, max_create_date=max_create_date, min_update_date=min_update_date, max_update_date=max_update_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


FEC election dates since 1995.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.reporting_dates_page import ReportingDatesPage
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
    api_instance = openapi_client.DatesApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    min_due_date = 'min_due_date_example' # str |  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_due_date = 'max_due_date_example' # str |  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    report_year = [56] # List[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
    report_type = ['report_type_example'] # List[str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)
    min_create_date = 'min_create_date_example' # str |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_create_date = 'max_create_date_example' # str |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    min_update_date = 'min_update_date_example' # str |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_update_date = 'max_update_date_example' # str |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    sort = '-due_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-due_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_reporting_dates_get(page=page, per_page=per_page, min_due_date=min_due_date, max_due_date=max_due_date, report_year=report_year, report_type=report_type, min_create_date=min_create_date, max_create_date=max_create_date, min_update_date=min_update_date, max_update_date=max_update_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DatesApi->v1_reporting_dates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatesApi->v1_reporting_dates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **min_due_date** | **str**|  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_due_date** | **str**|  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **report_year** | [**List[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **report_type** | [**List[str]**](str.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **min_create_date** | **str**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_create_date** | **str**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **min_update_date** | **str**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_update_date** | **str**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-due_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ReportingDatesPage**](ReportingDatesPage.md)

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

