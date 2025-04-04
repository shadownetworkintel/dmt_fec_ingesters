# openapi_client.NationalPartyAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_national_party_schedule_a_get**](NationalPartyAccountsApi.md#v1_national_party_schedule_a_get) | **GET** /v1/national_party/schedule_a/ | 
[**v1_national_party_schedule_b_get**](NationalPartyAccountsApi.md#v1_national_party_schedule_b_get) | **GET** /v1/national_party/schedule_b/ | 
[**v1_national_party_totals_get**](NationalPartyAccountsApi.md#v1_national_party_totals_get) | **GET** /v1/national_party/totals/ | 


# **v1_national_party_schedule_a_get**
> NationalPartyScheduleAPage v1_national_party_schedule_a_get(page=page, per_page=per_page, committee_id=committee_id, contributor_id=contributor_id, two_year_transaction_period=two_year_transaction_period, contributor_name=contributor_name, contributor_city=contributor_city, contributor_state=contributor_state, contributor_zip=contributor_zip, contributor_occupation=contributor_occupation, contributor_employer=contributor_employer, image_number=image_number, min_contribution_receipt_date=min_contribution_receipt_date, max_contribution_receipt_date=max_contribution_receipt_date, is_individual=is_individual, contributor_type=contributor_type, contributor_committee_type=contributor_committee_type, contributor_committee_designation=contributor_committee_designation, min_contribution_receipt_amount=min_contribution_receipt_amount, max_contribution_receipt_amount=max_contribution_receipt_amount, party_account_type=party_account_type, receipt_type=receipt_type, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)


This endpoint includes national party committee account receipts for presidential nominating conventions,
national party headquarters buildings, and election recounts and contests and other legal proceedings accounts.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.national_party_schedule_a_page import NationalPartyScheduleAPage
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
    api_instance = openapi_client.NationalPartyAccountsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    contributor_id = ['contributor_id_example'] # List[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
    two_year_transaction_period = [56] # List[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
    contributor_name = ['contributor_name_example'] # List[str] | Name of contributor (optional)
    contributor_city = ['contributor_city_example'] # List[str] | City of contributor (optional)
    contributor_state = ['contributor_state_example'] # List[str] | State of contributor (optional)
    contributor_zip = ['contributor_zip_example'] # List[str] | Zip code of contributor (optional)
    contributor_occupation = ['contributor_occupation_example'] # List[str] | Occupation of contributor, filers need to make an effort to gather this information (optional)
    contributor_employer = ['contributor_employer_example'] # List[str] | Employer of contributor, filers need to make an effort to gather this information (optional)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    min_contribution_receipt_date = 'min_contribution_receipt_date_example' # str |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_contribution_receipt_date = 'max_contribution_receipt_date_example' # str |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    is_individual = False # bool | Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. (optional) (default to False)
    contributor_type = ['contributor_type_example'] # List[str] |  Filters individual or committee contributions based on line number  (optional)
    contributor_committee_type = ['contributor_committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    contributor_committee_designation = ['contributor_committee_designation_example'] # List[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
    min_contribution_receipt_amount = 3.4 # float |  Minimum receipts amount  (optional)
    max_contribution_receipt_amount = 3.4 # float |  Maximum receipts amount  (optional)
    party_account_type = ['party_account_type_example'] # List[str] | Type of national party account:         - CONVENTION         - HEADQUARTERS         - RECOUNT  (optional)
    receipt_type = ['receipt_type_example'] # List[str] | National party account receipt types:     -30  CONVENTION ACCOUNT RECEIPT - INDIVIDUAL     -30E EARMARKED – CONVENTION     -30F MEMO RECEIPT FROM REGISTERED FILER - JF CONVENTION   ACCOUNT     -30G TRANSFER IN - CONVENTION ACCOUNT     -30J MEMO RECEIPT FROM INDIVIDUAL - JF CONVENTION ACCOUNT     -30K CONVENTION ACCOUNT RECEIPT - REGISTERED FILER     -30T CONVENTION ACCOUNT RECEIPT - TRIBAL     -31  HEADQUARTERS ACCOUNT RECEIPT- INDIVIDUAL     -31E EARMARKED – HEADQUARTERS     -31F MEMO RECEIPT FROM REGISTERED FILER - JF HEADQUARTERS ACCOUNT     -31G TRANSFER IN  - HEADQUARTERS ACCOUNT     -31J MEMO RECEIPT FROM INDIVIDUAL - JF HEADQUARTERS ACCOUNT     -31K HEADQUARTERS ACCOUNT RECEIPT - REGISTERED FILER     -31T HEADQUARTERS ACCOUNT RECEIPT - TRIBAL     -32  RECOUNT ACCOUNT RECEIPT- INDIVIDUAL     -32E EARMARKED – RECOUNT     -32F MEMO RECEIPT FROM REGISTERED FILER - JF RECOUNT ACCOUNT     -32G TRANSFER IN  - RECOUNT ACCOUNT     -32J MEMO RECEIPT FROM INDIVIDUAL -  JF RECOUNT ACCOUNT     -32K RECOUNT ACCOUNT RECEIPT- REGISTERED FILER     -32T RECOUNT ACCOUNT RECEIPT - TRIBAL  (optional)
    sort = '-contribution_receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-contribution_receipt_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_national_party_schedule_a_get(page=page, per_page=per_page, committee_id=committee_id, contributor_id=contributor_id, two_year_transaction_period=two_year_transaction_period, contributor_name=contributor_name, contributor_city=contributor_city, contributor_state=contributor_state, contributor_zip=contributor_zip, contributor_occupation=contributor_occupation, contributor_employer=contributor_employer, image_number=image_number, min_contribution_receipt_date=min_contribution_receipt_date, max_contribution_receipt_date=max_contribution_receipt_date, is_individual=is_individual, contributor_type=contributor_type, contributor_committee_type=contributor_committee_type, contributor_committee_designation=contributor_committee_designation, min_contribution_receipt_amount=min_contribution_receipt_amount, max_contribution_receipt_amount=max_contribution_receipt_amount, party_account_type=party_account_type, receipt_type=receipt_type, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)
        print("The response of NationalPartyAccountsApi->v1_national_party_schedule_a_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NationalPartyAccountsApi->v1_national_party_schedule_a_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **contributor_id** | [**List[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **two_year_transaction_period** | [**List[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **contributor_name** | [**List[str]**](str.md)| Name of contributor | [optional] 
 **contributor_city** | [**List[str]**](str.md)| City of contributor | [optional] 
 **contributor_state** | [**List[str]**](str.md)| State of contributor | [optional] 
 **contributor_zip** | [**List[str]**](str.md)| Zip code of contributor | [optional] 
 **contributor_occupation** | [**List[str]**](str.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] 
 **contributor_employer** | [**List[str]**](str.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] 
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **min_contribution_receipt_date** | **str**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_contribution_receipt_date** | **str**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **is_individual** | **bool**| Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. | [optional] [default to False]
 **contributor_type** | [**List[str]**](str.md)|  Filters individual or committee contributions based on line number  | [optional] 
 **contributor_committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **contributor_committee_designation** | [**List[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **min_contribution_receipt_amount** | **float**|  Minimum receipts amount  | [optional] 
 **max_contribution_receipt_amount** | **float**|  Maximum receipts amount  | [optional] 
 **party_account_type** | [**List[str]**](str.md)| Type of national party account:         - CONVENTION         - HEADQUARTERS         - RECOUNT  | [optional] 
 **receipt_type** | [**List[str]**](str.md)| National party account receipt types:     -30  CONVENTION ACCOUNT RECEIPT - INDIVIDUAL     -30E EARMARKED – CONVENTION     -30F MEMO RECEIPT FROM REGISTERED FILER - JF CONVENTION   ACCOUNT     -30G TRANSFER IN - CONVENTION ACCOUNT     -30J MEMO RECEIPT FROM INDIVIDUAL - JF CONVENTION ACCOUNT     -30K CONVENTION ACCOUNT RECEIPT - REGISTERED FILER     -30T CONVENTION ACCOUNT RECEIPT - TRIBAL     -31  HEADQUARTERS ACCOUNT RECEIPT- INDIVIDUAL     -31E EARMARKED – HEADQUARTERS     -31F MEMO RECEIPT FROM REGISTERED FILER - JF HEADQUARTERS ACCOUNT     -31G TRANSFER IN  - HEADQUARTERS ACCOUNT     -31J MEMO RECEIPT FROM INDIVIDUAL - JF HEADQUARTERS ACCOUNT     -31K HEADQUARTERS ACCOUNT RECEIPT - REGISTERED FILER     -31T HEADQUARTERS ACCOUNT RECEIPT - TRIBAL     -32  RECOUNT ACCOUNT RECEIPT- INDIVIDUAL     -32E EARMARKED – RECOUNT     -32F MEMO RECEIPT FROM REGISTERED FILER - JF RECOUNT ACCOUNT     -32G TRANSFER IN  - RECOUNT ACCOUNT     -32J MEMO RECEIPT FROM INDIVIDUAL -  JF RECOUNT ACCOUNT     -32K RECOUNT ACCOUNT RECEIPT- REGISTERED FILER     -32T RECOUNT ACCOUNT RECEIPT - TRIBAL  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-contribution_receipt_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**NationalPartyScheduleAPage**](NationalPartyScheduleAPage.md)

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

# **v1_national_party_schedule_b_get**
> NationalPartyScheduleBPage v1_national_party_schedule_b_get(page=page, per_page=per_page, committee_id=committee_id, disbursement_type=disbursement_type, disbursement_description=disbursement_description, disbursement_purpose_category=disbursement_purpose_category, image_number=image_number, line_number=line_number, min_disbursement_amount=min_disbursement_amount, max_disbursement_amount=max_disbursement_amount, min_disbursement_date=min_disbursement_date, max_disbursement_date=max_disbursement_date, recipient_city=recipient_city, recipient_committee_id=recipient_committee_id, recipient_name=recipient_name, recipient_state=recipient_state, recipient_zip=recipient_zip, recipient_committee_designation=recipient_committee_designation, recipient_committee_type=recipient_committee_type, two_year_transaction_period=two_year_transaction_period, party_account_type=party_account_type, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)


This endpoint includes national party committee account disbursements for presidential nominating conventions,
national party headquarters buildings, and election recounts and contests and other legal proceedings accounts


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.national_party_schedule_b_page import NationalPartyScheduleBPage
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
    api_instance = openapi_client.NationalPartyAccountsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    disbursement_type = ['disbursement_type_example'] # List[str] | National party account disbursement types:     -40  CONVENTION ACCOUNT DISBURSEMENT     -40T CONVENTION ACCOUNT REFUND - TRIBAL     -40Y CONVENTION ACCOUNT REFUND - INDIVIDUAL     -40Z CONVENTION ACCOUNT REFUND - REGISTERED FILER     -41  HEADQUARTERS ACCOUNT DISBURSEMENT     -41T HEADQUARTERS  ACCOUNT REFUND - TRIBAL     -41Y HEADQUARTERS  ACCOUNT REFUND - INDIVIDUAL     -41Z HEADQUARTERS  ACCOUNT REFUND - REGISTERED FILER     -42  RECOUNT ACCOUNT DISBURSEMENT     -42T RECOUNT ACCOUNT REFUND  - TRIBAL     -42Y RECOUNT ACCOUNT REFUND - INDIVIDUAL     -42Z RECOUNT ACCOUNT REFUND - REGISTERED FILER  (optional)
    disbursement_description = ['disbursement_description_example'] # List[str] | Description of disbursement (optional)
    disbursement_purpose_category = ['disbursement_purpose_category_example'] # List[str] | Disbursement purpose category (optional)
    image_number = ['image_number_example'] # List[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
    line_number = 'line_number_example' # str | Filter for form and line number using the following format: `<form_number-line_number>`. For example F3X-21b or F3X-29 would filter down to all entries from form `F3X` and line number `21b` or form `F3X` and line number `29`.  (optional)
    min_disbursement_amount = 3.4 # float |  Minimum disbursement amount  (optional)
    max_disbursement_amount = 3.4 # float |  Maximum disbursement amount  (optional)
    min_disbursement_date = 'min_disbursement_date_example' # str |  Selects all disbursements received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    max_disbursement_date = 'max_disbursement_date_example' # str |  Selects all disbursements received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
    recipient_city = ['recipient_city_example'] # List[str] | City of recipient (optional)
    recipient_committee_id = ['recipient_committee_id_example'] # List[str] | The FEC identifier should be represented here if the contributor is registered with the FEC. (optional)
    recipient_name = ['recipient_name_example'] # List[str] | Name of the entity receiving the disbursement (optional)
    recipient_state = ['recipient_state_example'] # List[str] | State of recipient (optional)
    recipient_zip = ['recipient_zip_example'] # List[str] |  Zipcode of recipient  (optional)
    recipient_committee_designation = ['recipient_committee_designation_example'] # List[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
    recipient_committee_type = ['recipient_committee_type_example'] # List[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
    two_year_transaction_period = [56] # List[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
    party_account_type = ['party_account_type_example'] # List[str] | Type of national party account:         - CONVENTION         - HEADQUARTERS         - RECOUNT  (optional)
    sort = '-disbursement_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-disbursement_date')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_national_party_schedule_b_get(page=page, per_page=per_page, committee_id=committee_id, disbursement_type=disbursement_type, disbursement_description=disbursement_description, disbursement_purpose_category=disbursement_purpose_category, image_number=image_number, line_number=line_number, min_disbursement_amount=min_disbursement_amount, max_disbursement_amount=max_disbursement_amount, min_disbursement_date=min_disbursement_date, max_disbursement_date=max_disbursement_date, recipient_city=recipient_city, recipient_committee_id=recipient_committee_id, recipient_name=recipient_name, recipient_state=recipient_state, recipient_zip=recipient_zip, recipient_committee_designation=recipient_committee_designation, recipient_committee_type=recipient_committee_type, two_year_transaction_period=two_year_transaction_period, party_account_type=party_account_type, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)
        print("The response of NationalPartyAccountsApi->v1_national_party_schedule_b_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NationalPartyAccountsApi->v1_national_party_schedule_b_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **disbursement_type** | [**List[str]**](str.md)| National party account disbursement types:     -40  CONVENTION ACCOUNT DISBURSEMENT     -40T CONVENTION ACCOUNT REFUND - TRIBAL     -40Y CONVENTION ACCOUNT REFUND - INDIVIDUAL     -40Z CONVENTION ACCOUNT REFUND - REGISTERED FILER     -41  HEADQUARTERS ACCOUNT DISBURSEMENT     -41T HEADQUARTERS  ACCOUNT REFUND - TRIBAL     -41Y HEADQUARTERS  ACCOUNT REFUND - INDIVIDUAL     -41Z HEADQUARTERS  ACCOUNT REFUND - REGISTERED FILER     -42  RECOUNT ACCOUNT DISBURSEMENT     -42T RECOUNT ACCOUNT REFUND  - TRIBAL     -42Y RECOUNT ACCOUNT REFUND - INDIVIDUAL     -42Z RECOUNT ACCOUNT REFUND - REGISTERED FILER  | [optional] 
 **disbursement_description** | [**List[str]**](str.md)| Description of disbursement | [optional] 
 **disbursement_purpose_category** | [**List[str]**](str.md)| Disbursement purpose category | [optional] 
 **image_number** | [**List[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;&lt;form_number-line_number&gt;&#x60;. For example F3X-21b or F3X-29 would filter down to all entries from form &#x60;F3X&#x60; and line number &#x60;21b&#x60; or form &#x60;F3X&#x60; and line number &#x60;29&#x60;.  | [optional] 
 **min_disbursement_amount** | **float**|  Minimum disbursement amount  | [optional] 
 **max_disbursement_amount** | **float**|  Maximum disbursement amount  | [optional] 
 **min_disbursement_date** | **str**|  Selects all disbursements received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_disbursement_date** | **str**|  Selects all disbursements received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **recipient_city** | [**List[str]**](str.md)| City of recipient | [optional] 
 **recipient_committee_id** | [**List[str]**](str.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **recipient_name** | [**List[str]**](str.md)| Name of the entity receiving the disbursement | [optional] 
 **recipient_state** | [**List[str]**](str.md)| State of recipient | [optional] 
 **recipient_zip** | [**List[str]**](str.md)|  Zipcode of recipient  | [optional] 
 **recipient_committee_designation** | [**List[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **recipient_committee_type** | [**List[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **two_year_transaction_period** | [**List[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **party_account_type** | [**List[str]**](str.md)| Type of national party account:         - CONVENTION         - HEADQUARTERS         - RECOUNT  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-disbursement_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**NationalPartyScheduleBPage**](NationalPartyScheduleBPage.md)

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

# **v1_national_party_totals_get**
> NationalPartyTotalsPage v1_national_party_totals_get(page=page, per_page=per_page, committee_id=committee_id, two_year_transaction_period=two_year_transaction_period, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)


This endpoint includes national party committee account total receipts and total disbursements for 

presidential nominating conventions, national party headquarters buildings, and election recounts 

and contests and other legal proceedings accounts for a given two year cycle.


### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.national_party_totals_page import NationalPartyTotalsPage
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
    api_instance = openapi_client.NationalPartyAccountsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
    committee_id = ['committee_id_example'] # List[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  (optional)
    two_year_transaction_period = [56] # List[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)
    sort = '-two_year_transaction_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_transaction_period')
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
    sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (optional) (default to 'DEMO_KEY')

    try:
        api_response = api_instance.v1_national_party_totals_get(page=page, per_page=per_page, committee_id=committee_id, two_year_transaction_period=two_year_transaction_period, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, api_key=api_key)
        print("The response of NationalPartyAccountsApi->v1_national_party_totals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NationalPartyAccountsApi->v1_national_party_totals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **committee_id** | [**List[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general a committee id begins with the letter C which is followed by eight digits.  | [optional] 
 **two_year_transaction_period** | [**List[int]**](int.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_transaction_period&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [optional] [default to &#39;DEMO_KEY&#39;]

### Return type

[**NationalPartyTotalsPage**](NationalPartyTotalsPage.md)

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

