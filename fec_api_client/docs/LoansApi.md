# openapi_client.LoansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_schedules_schedule_c_get**](LoansApi.md#v1_schedules_schedule_c_get) | **GET** /v1/schedules/schedule_c/ | 
[**v1_schedules_schedule_c_sub_id_get**](LoansApi.md#v1_schedules_schedule_c_sub_id_get) | **GET** /v1/schedules/schedule_c/{sub_id}/ | 


# **v1_schedules_schedule_c_get**
> ScheduleCPage v1_schedules_schedule_c_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, committee_id=committee_id, candidate_name=candidate_name, loan_source_name=loan_source_name, min_payment_to_date=min_payment_to_date, max_payment_to_date=max_payment_to_date, min_incurred_date=min_incurred_date, max_incurred_date=max_incurred_date, form_line_number=form_line_number, page=page, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule C shows all loans, endorsements and loan guarantees a committee
receives or makes.

The committee continues to report the loan until it is repaid.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_c_page import ScheduleCPage
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
    api_instance = openapi_client.LoansApi(api_client)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_image_number = 'min_image_number_example' # str | Minium image number of the page where the schedule item is reported (optional)
    max_image_number = 'max_image_number_example' # str | Maxium image number of the page where the schedule item is reported (optional)
    min_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    candidate_name = ['candidate_name_example'] # List[str] | Name of candidate running for office (optional)
    loan_source_name = ['loan_source_name_example'] # List[str] | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate (optional)
    min_payment_to_date = 56 # int |  Minimum payment to date  (optional)
    max_payment_to_date = 56 # int |  Maximum payment to date  (optional)
    min_incurred_date = 'null' # str |  Minimum incurred date  (optional) (default to 'null')
    max_incurred_date = 'null' # str |  Maximum incurred date  (optional) (default to 'null')
    form_line_number = ['form_line_number_example'] # List[str] |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    last_index = 56 # int | Index of last result from previous page (optional)
    sort = '-incurred_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-incurred_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = True # bool | Toggle that sorts null values last (optional) (default to True)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_c_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, committee_id=committee_id, candidate_name=candidate_name, loan_source_name=loan_source_name, min_payment_to_date=min_payment_to_date, max_payment_to_date=max_payment_to_date, min_incurred_date=min_incurred_date, max_incurred_date=max_incurred_date, form_line_number=form_line_number, page=page, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of LoansApi->v1_schedules_schedule_c_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->v1_schedules_schedule_c_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **min_image_number** | **str**| Minium image number of the page where the schedule item is reported | [optional] 
 **max_image_number** | **str**| Maxium image number of the page where the schedule item is reported | [optional] 
 **min_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **candidate_name** | [**List[str]**](str.md)| Name of candidate running for office | [optional] 
 **loan_source_name** | [**List[str]**](str.md)| Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate | [optional] 
 **min_payment_to_date** | **int**|  Minimum payment to date  | [optional] 
 **max_payment_to_date** | **int**|  Maximum payment to date  | [optional] 
 **min_incurred_date** | **str**|  Minimum incurred date  | [optional] [default to &#39;null&#39;]
 **max_incurred_date** | **str**|  Maximum incurred date  | [optional] [default to &#39;null&#39;]
 **form_line_number** | [**List[str]**](str.md)|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-incurred_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to True]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleCPage**](ScheduleCPage.md)

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

# **v1_schedules_schedule_c_sub_id_get**
> ScheduleCPage v1_schedules_schedule_c_sub_id_get(sub_id, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule C shows all loans, endorsements and loan guarantees a committee
receives or makes.

The committee continues to report the loan until it is repaid.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_c_page import ScheduleCPage
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
    api_instance = openapi_client.LoansApi(api_client)
    sub_id = 'sub_id_example' # str | 
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_c_sub_id_get(sub_id, page=page, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of LoansApi->v1_schedules_schedule_c_sub_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->v1_schedules_schedule_c_sub_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**|  | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleCPage**](ScheduleCPage.md)

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

