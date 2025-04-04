# openapi_client.DisbursementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_schedules_schedule_b_efile_get**](DisbursementsApi.md#v1_schedules_schedule_b_efile_get) | **GET** /v1/schedules/schedule_b/efile/ | 
[**v1_schedules_schedule_b_get**](DisbursementsApi.md#v1_schedules_schedule_b_get) | **GET** /v1/schedules/schedule_b/ | 
[**v1_schedules_schedule_b_sub_id_get**](DisbursementsApi.md#v1_schedules_schedule_b_sub_id_get) | **GET** /v1/schedules/schedule_b/{sub_id}/ | 
[**v1_schedules_schedule_bby_purpose_get**](DisbursementsApi.md#v1_schedules_schedule_bby_purpose_get) | **GET** /v1/schedules/schedule_b/by_purpose/ | 
[**v1_schedules_schedule_bby_recipient_get**](DisbursementsApi.md#v1_schedules_schedule_bby_recipient_get) | **GET** /v1/schedules/schedule_b/by_recipient/ | 
[**v1_schedules_schedule_bby_recipient_id_get**](DisbursementsApi.md#v1_schedules_schedule_bby_recipient_id_get) | **GET** /v1/schedules/schedule_b/by_recipient_id/ | 
[**v1_schedules_schedule_h4_efile_get**](DisbursementsApi.md#v1_schedules_schedule_h4_efile_get) | **GET** /v1/schedules/schedule_h4/efile/ | 
[**v1_schedules_schedule_h4_get**](DisbursementsApi.md#v1_schedules_schedule_h4_get) | **GET** /v1/schedules/schedule_h4/ | 


# **v1_schedules_schedule_b_efile_get**
> ScheduleBEfilePage v1_schedules_schedule_b_efile_get(page=page, per_page=per_page, committee_id=committee_id, disbursement_description=disbursement_description, image_number=image_number, recipient_city=recipient_city, recipient_state=recipient_state, max_date=max_date, min_date=min_date, min_amount=min_amount, max_amount=max_amount, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don't contain the processed and coded data that you can find on other endpoints.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_b_efile_page import ScheduleBEfilePage
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    disbursement_description = ['disbursement_description_example'] # List[str] | Description of disbursement (optional)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    recipient_city = ['recipient_city_example'] # List[str] | City of recipient (optional)
    recipient_state = ['recipient_state_example'] # List[str] | State of recipient (optional)
    max_date = 'null' # str | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional) (default to 'null')
    min_date = 'null' # str | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page. (optional) (default to 'null')
    min_amount = 3.4 # float | Filter for all amounts less than a value. (optional)
    max_amount = 3.4 # float | Filter for all amounts less than a value. (optional)
    sort = '-disbursement_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-disbursement_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_b_efile_get(page=page, per_page=per_page, committee_id=committee_id, disbursement_description=disbursement_description, image_number=image_number, recipient_city=recipient_city, recipient_state=recipient_state, max_date=max_date, min_date=min_date, min_amount=min_amount, max_amount=max_amount, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_b_efile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_b_efile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **disbursement_description** | [**List[str]**](str.md)| Description of disbursement | [optional] 
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **recipient_city** | [**List[str]**](str.md)| City of recipient | [optional] 
 **recipient_state** | [**List[str]**](str.md)| State of recipient | [optional] 
 **max_date** | **str**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to &#39;null&#39;]
 **min_date** | **str**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to &#39;null&#39;]
 **min_amount** | **float**| Filter for all amounts less than a value. | [optional] 
 **max_amount** | **float**| Filter for all amounts less than a value. | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-disbursement_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleBEfilePage**](ScheduleBEfilePage.md)

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

# **v1_schedules_schedule_b_get**
> ScheduleBPage v1_schedules_schedule_b_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, committee_id=committee_id, disbursement_description=disbursement_description, disbursement_purpose_category=disbursement_purpose_category, last_disbursement_amount=last_disbursement_amount, last_disbursement_date=last_disbursement_date, line_number=line_number, recipient_city=recipient_city, recipient_committee_id=recipient_committee_id, recipient_name=recipient_name, recipient_state=recipient_state, spender_committee_designation=spender_committee_designation, spender_committee_org_type=spender_committee_org_type, spender_committee_type=spender_committee_type, two_year_transaction_period=two_year_transaction_period, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)


Schedule B filings describe itemized disbursements. This data
explains how committees and other filers spend their money. These figures are
reported as part of forms F3, F3X and F3P.

The data are divided in two-year periods, called `two_year_transaction_period`, which
is derived from the `report_year` submitted of the corresponding form. If no value is supplied, the results will
default to the most recent two-year period that is named after the ending,
even-numbered year.

Due to the large quantity of Schedule B filings, this endpoint is not paginated by
page number. Instead, you can request the next page of results by adding the values in
the `last_indexes` object from `pagination` to the URL of your last request. For
example, when sorting by `disbursement_date`, you might receive a page of
results with the following pagination information:

```
pagination: {
    pages: 965191,
    per_page: 20,
    count: 19303814,
    is_count_exact: False,
    last_indexes: {
        last_index: "230906248",
        last_disbursement_date: "2014-07-04"
    }
}
```

To fetch the next page of sorted results, append `last_index=230906248` and
`last_disbursement_date=2014-07-04` to the URL.  We strongly advise paging through
these results by using the sort indices (defaults to sort by disbursement date, e.g.
`last_disbursement_date`), otherwise some resources may be unintentionally filtered out.
This resource uses keyset pagination to improve query performance
and these indices are required to properly page through this large dataset.

Note: because the Schedule B data includes many records, counts for
large result sets are approximate; you will want to page through the records until no records are returned.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_b_page import ScheduleBPage
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_image_number = 'min_image_number_example' # str | Minium image number of the page where the schedule item is reported (optional)
    max_image_number = 'max_image_number_example' # str | Maxium image number of the page where the schedule item is reported (optional)
    min_amount = 3.4 # float | Filter for all amounts greater than a value. (optional)
    max_amount = 3.4 # float | Filter for all amounts less than a value. (optional)
    min_date = 'min_date_example' # str | Minimum date (optional)
    max_date = 'max_date_example' # str | Maximum date (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    disbursement_description = ['disbursement_description_example'] # List[str] | Description of disbursement (optional)
    disbursement_purpose_category = ['disbursement_purpose_category_example'] # List[str] | Disbursement purpose category (optional)
    last_disbursement_amount = 3.4 # float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    last_disbursement_date = 'null' # str | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. (optional) (default to 'null')
    line_number = 'line_number_example' # str |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
    recipient_city = ['recipient_city_example'] # List[str] | City of recipient (optional)
    recipient_committee_id = ['recipient_committee_id_example'] # List[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
    recipient_name = ['recipient_name_example'] # List[str] | Name of the entity receiving the disbursement (optional)
    recipient_state = ['recipient_state_example'] # List[str] | State of recipient (optional)
    spender_committee_designation = ['spender_committee_designation_example'] # List[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
    spender_committee_org_type = ['spender_committee_org_type_example'] # List[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
    spender_committee_type = ['spender_committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    two_year_transaction_period = [56] # List[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    last_index = 56 # int | Index of last result from previous page (optional)
    sort = '-disbursement_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-disbursement_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_b_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, committee_id=committee_id, disbursement_description=disbursement_description, disbursement_purpose_category=disbursement_purpose_category, last_disbursement_amount=last_disbursement_amount, last_disbursement_date=last_disbursement_date, line_number=line_number, recipient_city=recipient_city, recipient_committee_id=recipient_committee_id, recipient_name=recipient_name, recipient_state=recipient_state, spender_committee_designation=spender_committee_designation, spender_committee_org_type=spender_committee_org_type, spender_committee_type=spender_committee_type, two_year_transaction_period=two_year_transaction_period, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_b_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_b_get: %s\n" % e)
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
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **disbursement_description** | [**List[str]**](str.md)| Description of disbursement | [optional] 
 **disbursement_purpose_category** | [**List[str]**](str.md)| Disbursement purpose category | [optional] 
 **last_disbursement_amount** | **float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **last_disbursement_date** | **str**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to &#39;null&#39;]
 **line_number** | **str**|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **recipient_city** | [**List[str]**](str.md)| City of recipient | [optional] 
 **recipient_committee_id** | [**List[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **recipient_name** | [**List[str]**](str.md)| Name of the entity receiving the disbursement | [optional] 
 **recipient_state** | [**List[str]**](str.md)| State of recipient | [optional] 
 **spender_committee_designation** | [**List[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **spender_committee_org_type** | [**List[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **spender_committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **two_year_transaction_period** | [**List[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-disbursement_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

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

# **v1_schedules_schedule_b_sub_id_get**
> ScheduleBPage v1_schedules_schedule_b_sub_id_get(sub_id, image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, committee_id=committee_id, disbursement_description=disbursement_description, disbursement_purpose_category=disbursement_purpose_category, last_disbursement_amount=last_disbursement_amount, last_disbursement_date=last_disbursement_date, line_number=line_number, recipient_city=recipient_city, recipient_committee_id=recipient_committee_id, recipient_name=recipient_name, recipient_state=recipient_state, spender_committee_designation=spender_committee_designation, spender_committee_org_type=spender_committee_org_type, spender_committee_type=spender_committee_type, two_year_transaction_period=two_year_transaction_period, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)


Schedule B filings describe itemized disbursements. This data
explains how committees and other filers spend their money. These figures are
reported as part of forms F3, F3X and F3P.

The data are divided in two-year periods, called `two_year_transaction_period`, which
is derived from the `report_year` submitted of the corresponding form. If no value is supplied, the results will
default to the most recent two-year period that is named after the ending,
even-numbered year.

Due to the large quantity of Schedule B filings, this endpoint is not paginated by
page number. Instead, you can request the next page of results by adding the values in
the `last_indexes` object from `pagination` to the URL of your last request. For
example, when sorting by `disbursement_date`, you might receive a page of
results with the following pagination information:

```
pagination: {
    pages: 965191,
    per_page: 20,
    count: 19303814,
    is_count_exact: False,
    last_indexes: {
        last_index: "230906248",
        last_disbursement_date: "2014-07-04"
    }
}
```

To fetch the next page of sorted results, append `last_index=230906248` and
`last_disbursement_date=2014-07-04` to the URL.  We strongly advise paging through
these results by using the sort indices (defaults to sort by disbursement date, e.g.
`last_disbursement_date`), otherwise some resources may be unintentionally filtered out.
This resource uses keyset pagination to improve query performance
and these indices are required to properly page through this large dataset.

Note: because the Schedule B data includes many records, counts for
large result sets are approximate; you will want to page through the records until no records are returned.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_b_page import ScheduleBPage
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    sub_id = 'sub_id_example' # str | 
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_image_number = 'min_image_number_example' # str | Minium image number of the page where the schedule item is reported (optional)
    max_image_number = 'max_image_number_example' # str | Maxium image number of the page where the schedule item is reported (optional)
    min_amount = 3.4 # float | Filter for all amounts greater than a value. (optional)
    max_amount = 3.4 # float | Filter for all amounts less than a value. (optional)
    min_date = 'min_date_example' # str | Minimum date (optional)
    max_date = 'max_date_example' # str | Maximum date (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    disbursement_description = ['disbursement_description_example'] # List[str] | Description of disbursement (optional)
    disbursement_purpose_category = ['disbursement_purpose_category_example'] # List[str] | Disbursement purpose category (optional)
    last_disbursement_amount = 3.4 # float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    last_disbursement_date = 'null' # str | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. (optional) (default to 'null')
    line_number = 'line_number_example' # str |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
    recipient_city = ['recipient_city_example'] # List[str] | City of recipient (optional)
    recipient_committee_id = ['recipient_committee_id_example'] # List[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
    recipient_name = ['recipient_name_example'] # List[str] | Name of the entity receiving the disbursement (optional)
    recipient_state = ['recipient_state_example'] # List[str] | State of recipient (optional)
    spender_committee_designation = ['spender_committee_designation_example'] # List[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
    spender_committee_org_type = ['spender_committee_org_type_example'] # List[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
    spender_committee_type = ['spender_committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    two_year_transaction_period = [56] # List[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    last_index = 56 # int | Index of last result from previous page (optional)
    sort = '-disbursement_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-disbursement_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_b_sub_id_get(sub_id, image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, committee_id=committee_id, disbursement_description=disbursement_description, disbursement_purpose_category=disbursement_purpose_category, last_disbursement_amount=last_disbursement_amount, last_disbursement_date=last_disbursement_date, line_number=line_number, recipient_city=recipient_city, recipient_committee_id=recipient_committee_id, recipient_name=recipient_name, recipient_state=recipient_state, spender_committee_designation=spender_committee_designation, spender_committee_org_type=spender_committee_org_type, spender_committee_type=spender_committee_type, two_year_transaction_period=two_year_transaction_period, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_b_sub_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_b_sub_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**|  | 
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **min_image_number** | **str**| Minium image number of the page where the schedule item is reported | [optional] 
 **max_image_number** | **str**| Maxium image number of the page where the schedule item is reported | [optional] 
 **min_amount** | **float**| Filter for all amounts greater than a value. | [optional] 
 **max_amount** | **float**| Filter for all amounts less than a value. | [optional] 
 **min_date** | **str**| Minimum date | [optional] 
 **max_date** | **str**| Maximum date | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **disbursement_description** | [**List[str]**](str.md)| Description of disbursement | [optional] 
 **disbursement_purpose_category** | [**List[str]**](str.md)| Disbursement purpose category | [optional] 
 **last_disbursement_amount** | **float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **last_disbursement_date** | **str**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to &#39;null&#39;]
 **line_number** | **str**|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **recipient_city** | [**List[str]**](str.md)| City of recipient | [optional] 
 **recipient_committee_id** | [**List[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **recipient_name** | [**List[str]**](str.md)| Name of the entity receiving the disbursement | [optional] 
 **recipient_state** | [**List[str]**](str.md)| State of recipient | [optional] 
 **spender_committee_designation** | [**List[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **spender_committee_org_type** | [**List[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **spender_committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **two_year_transaction_period** | [**List[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-disbursement_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

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

# **v1_schedules_schedule_bby_purpose_get**
> ScheduleBByPurposePage v1_schedules_schedule_bby_purpose_get(page=page, per_page=per_page, cycle=cycle, purpose=purpose, committee_id=committee_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule B disbursements aggregated by disbursement purpose category. To avoid double counting,
memoed items are not included.
Purpose is a combination of transaction codes, category codes and disbursement description.
Inspect the `disbursement_purpose` sql function within the migrations for more details.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_bby_purpose_page import ScheduleBByPurposePage
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    purpose = ['purpose_example'] # List[str] | Disbursement purpose category (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_bby_purpose_get(page=page, per_page=per_page, cycle=cycle, purpose=purpose, committee_id=committee_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_bby_purpose_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_bby_purpose_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **purpose** | [**List[str]**](str.md)| Disbursement purpose category | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleBByPurposePage**](ScheduleBByPurposePage.md)

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

# **v1_schedules_schedule_bby_recipient_get**
> ScheduleBByRecipientPage v1_schedules_schedule_bby_recipient_get(page=page, per_page=per_page, cycle=cycle, recipient_name=recipient_name, committee_id=committee_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule B disbursements aggregated by recipient name. To avoid double counting,
memoed items are not included.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_bby_recipient_page import ScheduleBByRecipientPage
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    recipient_name = ['recipient_name_example'] # List[str] | Name of the entity receiving the disbursement (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_bby_recipient_get(page=page, per_page=per_page, cycle=cycle, recipient_name=recipient_name, committee_id=committee_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_bby_recipient_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_bby_recipient_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **recipient_name** | [**List[str]**](str.md)| Name of the entity receiving the disbursement | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleBByRecipientPage**](ScheduleBByRecipientPage.md)

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

# **v1_schedules_schedule_bby_recipient_id_get**
> ScheduleBByRecipientIDPage v1_schedules_schedule_bby_recipient_id_get(page=page, per_page=per_page, cycle=cycle, recipient_id=recipient_id, committee_id=committee_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Schedule B disbursements aggregated by recipient committee ID, if applicable.
To avoid double counting, memoed items are not included.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_bby_recipient_id_page import ScheduleBByRecipientIDPage
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    recipient_id = ['recipient_id_example'] # List[str] | The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_bby_recipient_id_get(page=page, per_page=per_page, cycle=cycle, recipient_id=recipient_id, committee_id=committee_id, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_bby_recipient_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_bby_recipient_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **recipient_id** | [**List[str]**](str.md)| The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleBByRecipientIDPage**](ScheduleBByRecipientIDPage.md)

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

# **v1_schedules_schedule_h4_efile_get**
> ScheduleH4EfilePage v1_schedules_schedule_h4_efile_get(page=page, per_page=per_page, image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, payee_city=payee_city, payee_zip=payee_zip, payee_state=payee_state, committee_id=committee_id, last_disbursement_purpose=last_disbursement_purpose, last_event_purpose_date=last_event_purpose_date, min_date=min_date, max_date=max_date, last_disbursement_amount=last_disbursement_amount, min_amount=min_amount, max_amount=max_amount, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)


Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don't contain the processed and coded data that you can find on other endpoints.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_h4_efile_page import ScheduleH4EfilePage
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_image_number = 'min_image_number_example' # str | Minium image number of the page where the schedule item is reported (optional)
    max_image_number = 'max_image_number_example' # str | Maxium image number of the page where the schedule item is reported (optional)
    payee_city = ['payee_city_example'] # List[str] | City of the entity that received the payment (optional)
    payee_zip = ['payee_zip_example'] # List[str] | Zip of the entity that received the payment (optional)
    payee_state = ['payee_state_example'] # List[str] | State of the entity that received the payment (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    last_disbursement_purpose = ['last_disbursement_purpose_example'] # List[str] | When sorting by `disbursement_purpose`, this is populated with the `disbursement_purpose`of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    last_event_purpose_date = 'null' # str | When sorting by `event_purpose_date`, this is populated with the `event_purpose_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. (optional) (default to 'null')
    min_date = 'null' # str | Minimum event_purpose_date (optional) (default to 'null')
    max_date = 'null' # str | Maximum event_purpose_date (optional) (default to 'null')
    last_disbursement_amount = 3.4 # float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    min_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    sort = '-event_purpose_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-event_purpose_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_h4_efile_get(page=page, per_page=per_page, image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, payee_city=payee_city, payee_zip=payee_zip, payee_state=payee_state, committee_id=committee_id, last_disbursement_purpose=last_disbursement_purpose, last_event_purpose_date=last_event_purpose_date, min_date=min_date, max_date=max_date, last_disbursement_amount=last_disbursement_amount, min_amount=min_amount, max_amount=max_amount, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_h4_efile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_h4_efile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **min_image_number** | **str**| Minium image number of the page where the schedule item is reported | [optional] 
 **max_image_number** | **str**| Maxium image number of the page where the schedule item is reported | [optional] 
 **payee_city** | [**List[str]**](str.md)| City of the entity that received the payment | [optional] 
 **payee_zip** | [**List[str]**](str.md)| Zip of the entity that received the payment | [optional] 
 **payee_state** | [**List[str]**](str.md)| State of the entity that received the payment | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **last_disbursement_purpose** | [**List[str]**](str.md)| When sorting by &#x60;disbursement_purpose&#x60;, this is populated with the &#x60;disbursement_purpose&#x60;of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **last_event_purpose_date** | **str**| When sorting by &#x60;event_purpose_date&#x60;, this is populated with the &#x60;event_purpose_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to &#39;null&#39;]
 **min_date** | **str**| Minimum event_purpose_date | [optional] [default to &#39;null&#39;]
 **max_date** | **str**| Maximum event_purpose_date | [optional] [default to &#39;null&#39;]
 **last_disbursement_amount** | **float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **min_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-event_purpose_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleH4EfilePage**](ScheduleH4EfilePage.md)

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

# **v1_schedules_schedule_h4_get**
> ScheduleH4Page v1_schedules_schedule_h4_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, report_year=report_year, report_type=report_type, activity_or_event=activity_or_event, q_payee_name=q_payee_name, payee_city=payee_city, payee_zip=payee_zip, payee_state=payee_state, q_disbursement_purpose=q_disbursement_purpose, cycle=cycle, committee_id=committee_id, last_payee_name=last_payee_name, last_disbursement_purpose=last_disbursement_purpose, last_event_purpose_date=last_event_purpose_date, last_spender_committee_name=last_spender_committee_name, last_disbursement_amount=last_disbursement_amount, administrative_voter_drive_activity_indicator=administrative_voter_drive_activity_indicator, fundraising_activity_indicator=fundraising_activity_indicator, exempt_activity_indicator=exempt_activity_indicator, direct_candidate_support_activity_indicator=direct_candidate_support_activity_indicator, administrative_activity_indicator=administrative_activity_indicator, general_voter_drive_activity_indicator=general_voter_drive_activity_indicator, public_comm_indicator=public_comm_indicator, spender_committee_name=spender_committee_name, spender_committee_type=spender_committee_type, spender_committee_designation=spender_committee_designation, form_line_number=form_line_number, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)


Schedule H4 filings describe disbursements for allocated federal/nonfederal activity. This data
demonstrates how separate segregated funds, party committees and nonconnected committees that are active
in both federal and nonfederal elections, and have established separate federal and nonfederal accounts,
allocate their activity. These figures are reported on Form 3X.

The data are divided in two-year periods, called `two_year_transaction_period`, which are derived from the
`report_year` submitted on Form 3X. If no value is supplied, the results will default to the most recent
two-year period.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.schedule_h4_page import ScheduleH4Page
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
    api_instance = openapi_client.DisbursementsApi(api_client)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_image_number = 'min_image_number_example' # str | Minium image number of the page where the schedule item is reported (optional)
    max_image_number = 'max_image_number_example' # str | Maxium image number of the page where the schedule item is reported (optional)
    min_amount = 3.4 # float |  Filter for all amounts greater than a value.  (optional)
    max_amount = 3.4 # float |  Filter for all amounts less than a value.  (optional)
    min_date = 'null' # str | Minimum event_purpose_date (optional) (default to 'null')
    max_date = 'null' # str | Maximum event_purpose_date (optional) (default to 'null')
    report_year = [56] # List[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
    report_type = ['report_type_example'] # List[str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)
    activity_or_event = ['activity_or_event_example'] # List[str] |  (optional)
    q_payee_name = ['q_payee_name_example'] # List[str] |  Name of the entity that received the payment.  (optional)
    payee_city = ['payee_city_example'] # List[str] | City of the entity that received the payment (optional)
    payee_zip = ['payee_zip_example'] # List[str] | Zip of the entity that received the payment (optional)
    payee_state = ['payee_state_example'] # List[str] | State of the entity that received the payment (optional)
    q_disbursement_purpose = ['q_disbursement_purpose_example'] # List[str] | Purpose of the allocated disbursement (optional)
    cycle = [56] # List[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    last_payee_name = ['last_payee_name_example'] # List[str] | When sorting by `payee_name`, this is populated with the `payee_name` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    last_disbursement_purpose = ['last_disbursement_purpose_example'] # List[str] | When sorting by `disbursement_purpose`, this is populated with the `disbursement_purpose`of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    last_event_purpose_date = 'null' # str | When sorting by `event_purpose_date`, this is populated with the `event_purpose_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. (optional) (default to 'null')
    last_spender_committee_name = ['last_spender_committee_name_example'] # List[str] | When sorting by `spender_committee_name`, this is populated with the `spender_committee_name` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    last_disbursement_amount = 3.4 # float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page. (optional)
    administrative_voter_drive_activity_indicator = ['administrative_voter_drive_activity_indicator_example'] # List[str] | Activity or event: Admin/Voter Drive checkbox (optional)
    fundraising_activity_indicator = ['fundraising_activity_indicator_example'] # List[str] | Activity or event: Fundraising checkbox (optional)
    exempt_activity_indicator = ['exempt_activity_indicator_example'] # List[str] | Activity or event: Exempt checkbox (optional)
    direct_candidate_support_activity_indicator = ['direct_candidate_support_activity_indicator_example'] # List[str] | Activity or event: Direct Candidate checkbox (optional)
    administrative_activity_indicator = ['administrative_activity_indicator_example'] # List[str] | Activity or event: Administrative checkbox (optional)
    general_voter_drive_activity_indicator = ['general_voter_drive_activity_indicator_example'] # List[str] | Activity or event: Voter Drive checkbox (optional)
    public_comm_indicator = ['public_comm_indicator_example'] # List[str] | Activity or event: Public Comm (ref to party only) by PAC checkbox (optional)
    spender_committee_name = ['spender_committee_name_example'] # List[str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)
    spender_committee_type = ['spender_committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    spender_committee_designation = ['spender_committee_designation_example'] # List[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
    form_line_number = ['form_line_number_example'] # List[str] |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    last_index = 56 # int | Index of last result from previous page (optional)
    sort = '-event_purpose_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-event_purpose_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_schedules_schedule_h4_get(image_number=image_number, min_image_number=min_image_number, max_image_number=max_image_number, min_amount=min_amount, max_amount=max_amount, min_date=min_date, max_date=max_date, report_year=report_year, report_type=report_type, activity_or_event=activity_or_event, q_payee_name=q_payee_name, payee_city=payee_city, payee_zip=payee_zip, payee_state=payee_state, q_disbursement_purpose=q_disbursement_purpose, cycle=cycle, committee_id=committee_id, last_payee_name=last_payee_name, last_disbursement_purpose=last_disbursement_purpose, last_event_purpose_date=last_event_purpose_date, last_spender_committee_name=last_spender_committee_name, last_disbursement_amount=last_disbursement_amount, administrative_voter_drive_activity_indicator=administrative_voter_drive_activity_indicator, fundraising_activity_indicator=fundraising_activity_indicator, exempt_activity_indicator=exempt_activity_indicator, direct_candidate_support_activity_indicator=direct_candidate_support_activity_indicator, administrative_activity_indicator=administrative_activity_indicator, general_voter_drive_activity_indicator=general_voter_drive_activity_indicator, public_comm_indicator=public_comm_indicator, spender_committee_name=spender_committee_name, spender_committee_type=spender_committee_type, spender_committee_designation=spender_committee_designation, form_line_number=form_line_number, per_page=per_page, last_index=last_index, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)
        print("The response of DisbursementsApi->v1_schedules_schedule_h4_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementsApi->v1_schedules_schedule_h4_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **min_image_number** | **str**| Minium image number of the page where the schedule item is reported | [optional] 
 **max_image_number** | **str**| Maxium image number of the page where the schedule item is reported | [optional] 
 **min_amount** | **float**|  Filter for all amounts greater than a value.  | [optional] 
 **max_amount** | **float**|  Filter for all amounts less than a value.  | [optional] 
 **min_date** | **str**| Minimum event_purpose_date | [optional] [default to &#39;null&#39;]
 **max_date** | **str**| Maximum event_purpose_date | [optional] [default to &#39;null&#39;]
 **report_year** | [**List[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **report_type** | [**List[str]**](str.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 24  24 Hour Notification (F6, F9)     - 24  24 Hour Report of Independent Expenditures (F5, F24/F3X)     - 48  48 Hour Report of Independent Expenditures (F5, F24/F3X)     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **activity_or_event** | [**List[str]**](str.md)|  | [optional] 
 **q_payee_name** | [**List[str]**](str.md)|  Name of the entity that received the payment.  | [optional] 
 **payee_city** | [**List[str]**](str.md)| City of the entity that received the payment | [optional] 
 **payee_zip** | [**List[str]**](str.md)| Zip of the entity that received the payment | [optional] 
 **payee_state** | [**List[str]**](str.md)| State of the entity that received the payment | [optional] 
 **q_disbursement_purpose** | [**List[str]**](str.md)| Purpose of the allocated disbursement | [optional] 
 **cycle** | [**List[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **last_payee_name** | [**List[str]**](str.md)| When sorting by &#x60;payee_name&#x60;, this is populated with the &#x60;payee_name&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **last_disbursement_purpose** | [**List[str]**](str.md)| When sorting by &#x60;disbursement_purpose&#x60;, this is populated with the &#x60;disbursement_purpose&#x60;of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **last_event_purpose_date** | **str**| When sorting by &#x60;event_purpose_date&#x60;, this is populated with the &#x60;event_purpose_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] [default to &#39;null&#39;]
 **last_spender_committee_name** | [**List[str]**](str.md)| When sorting by &#x60;spender_committee_name&#x60;, this is populated with the &#x60;spender_committee_name&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **last_disbursement_amount** | **float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **administrative_voter_drive_activity_indicator** | [**List[str]**](str.md)| Activity or event: Admin/Voter Drive checkbox | [optional] 
 **fundraising_activity_indicator** | [**List[str]**](str.md)| Activity or event: Fundraising checkbox | [optional] 
 **exempt_activity_indicator** | [**List[str]**](str.md)| Activity or event: Exempt checkbox | [optional] 
 **direct_candidate_support_activity_indicator** | [**List[str]**](str.md)| Activity or event: Direct Candidate checkbox | [optional] 
 **administrative_activity_indicator** | [**List[str]**](str.md)| Activity or event: Administrative checkbox | [optional] 
 **general_voter_drive_activity_indicator** | [**List[str]**](str.md)| Activity or event: Voter Drive checkbox | [optional] 
 **public_comm_indicator** | [**List[str]**](str.md)| Activity or event: Public Comm (ref to party only) by PAC checkbox | [optional] 
 **spender_committee_name** | [**List[str]**](str.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
 **spender_committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **spender_committee_designation** | [**List[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **form_line_number** | [**List[str]**](str.md)|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-event_purpose_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**ScheduleH4Page**](ScheduleH4Page.md)

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

