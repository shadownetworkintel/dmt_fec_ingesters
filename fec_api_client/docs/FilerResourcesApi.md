# openapi_client.FilerResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_rad_analyst_get**](FilerResourcesApi.md#v1_rad_analyst_get) | **GET** /v1/rad-analyst/ | 
[**v1_state_election_office_get**](FilerResourcesApi.md#v1_state_election_office_get) | **GET** /v1/state-election-office/ | 


# **v1_rad_analyst_get**
> RadAnalystPage v1_rad_analyst_get(page=page, per_page=per_page, committee_id=committee_id, analyst_id=analyst_id, analyst_short_id=analyst_short_id, telephone_ext=telephone_ext, name=name, email=email, title=title, min_assignment_update_date=min_assignment_update_date, max_assignment_update_date=max_assignment_update_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Use this endpoint to look up the RAD Analyst for a committee.

The mission of the Reports Analysis Division (RAD) is to ensure that
campaigns and political committees file timely and accurate reports that fully disclose
their financial activities.  RAD is responsible for reviewing statements and financial
reports filed by political committees participating in federal elections, providing
assistance and guidance to the committees to properly file their reports, and for taking
appropriate action to ensure compliance with the Federal Election Campaign Act (FECA).


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.rad_analyst_page import RadAnalystPage
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
    api_instance = openapi_client.FilerResourcesApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    analyst_id = [56] # List[int] | ID of RAD analyst (optional)
    analyst_short_id = [56] # List[int] | Short ID of RAD analyst (optional)
    telephone_ext = [56] # List[int] | Telephone extension of RAD analyst (optional)
    name = ['name_example'] # List[str] | Name of RAD analyst (optional)
    email = ['email_example'] # List[str] | Email of RAD analyst (optional)
    title = ['title_example'] # List[str] | Title of RAD analyst (optional)
    min_assignment_update_date = 'min_assignment_update_date_example' # str | Filter results for assignment updates made after this date (optional)
    max_assignment_update_date = 'max_assignment_update_date_example' # str | Filter results for assignment updates made before this date (optional)
    sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_rad_analyst_get(page=page, per_page=per_page, committee_id=committee_id, analyst_id=analyst_id, analyst_short_id=analyst_short_id, telephone_ext=telephone_ext, name=name, email=email, title=title, min_assignment_update_date=min_assignment_update_date, max_assignment_update_date=max_assignment_update_date, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FilerResourcesApi->v1_rad_analyst_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilerResourcesApi->v1_rad_analyst_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **analyst_id** | [**List[int]**](int.md)| ID of RAD analyst | [optional] 
 **analyst_short_id** | [**List[int]**](int.md)| Short ID of RAD analyst | [optional] 
 **telephone_ext** | [**List[int]**](int.md)| Telephone extension of RAD analyst | [optional] 
 **name** | [**List[str]**](str.md)| Name of RAD analyst | [optional] 
 **email** | [**List[str]**](str.md)| Email of RAD analyst | [optional] 
 **title** | [**List[str]**](str.md)| Title of RAD analyst | [optional] 
 **min_assignment_update_date** | **str**| Filter results for assignment updates made after this date | [optional] 
 **max_assignment_update_date** | **str**| Filter results for assignment updates made before this date | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**RadAnalystPage**](RadAnalystPage.md)

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

# **v1_state_election_office_get**
> StateElectionOfficeInfoPage v1_state_election_office_get(state, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


State laws and procedures govern elections for state or local offices as well as
how candidates appear on election ballots.
Contact the appropriate state election office for more information.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.state_election_office_info_page import StateElectionOfficeInfoPage
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
    api_instance = openapi_client.FilerResourcesApi(api_client)
    state = 'state_example' # str |  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.  
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_state_election_office_get(state, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of FilerResourcesApi->v1_state_election_office_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilerResourcesApi->v1_state_election_office_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.   | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**StateElectionOfficeInfoPage**](StateElectionOfficeInfoPage.md)

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

