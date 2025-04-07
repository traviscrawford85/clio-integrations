# openapi_client.CivilCertificatedRatesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lauk_civil_certificated_rate_index**](CivilCertificatedRatesApi.md#lauk_civil_certificated_rate_index) | **GET** /lauk_civil_certificated_rates.json | List Civil Certificated Rates


# **lauk_civil_certificated_rate_index**
> LaukCivilCertificatedRateList lauk_civil_certificated_rate_index(x_api_version=x_api_version, activity=activity, activity_sub_category=activity_sub_category, attended_several_hearings_for_multiple_clients=attended_several_hearings_for_multiple_clients, category_of_law=category_of_law, change_of_solicitor=change_of_solicitor, court=court, eligible_for_sqm=eligible_for_sqm, fee_scheme=fee_scheme, fields=fields, first_conducting_solicitor=first_conducting_solicitor, key=key, limit=limit, number_of_clients=number_of_clients, page_token=page_token, party=party, post_transfer_clients_represented=post_transfer_clients_represented, rate_type=rate_type, region=region, session_type=session_type, user_type=user_type)

List Civil Certificated Rates

Outlines the parameters, optional and required, used when requesting the data for all LaukCivilCertificatedRates

### Example


```python
import openapi_client
from openapi_client.models.lauk_civil_certificated_rate_list import LaukCivilCertificatedRateList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.clio.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.clio.com/api/v4"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CivilCertificatedRatesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    activity = 'activity_example' # str | Filter by activity. (optional)
    activity_sub_category = 'activity_sub_category_example' # str | Filter by activity sub-category. (optional)
    attended_several_hearings_for_multiple_clients = True # bool | Filter by whether multiple hearings were attended for multiple clients. (optional)
    category_of_law = 'category_of_law_example' # str | Filter by category of law. (optional)
    change_of_solicitor = True # bool | Filter by change of solicitor status. (optional)
    court = 'court_example' # str | Filter by court. (optional)
    eligible_for_sqm = True # bool | Filter by SQM eligibility. (optional)
    fee_scheme = 'fee_scheme_example' # str | Fee scheme (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    first_conducting_solicitor = True # bool | Filter by first conducting solicitor status. (optional)
    key = 'key_example' # str | Filter by key. (optional)
    limit = 56 # int | A limit on the number of LaukCivilCertificatedRate records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    number_of_clients = 'number_of_clients_example' # str | Filter by number of clients. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    party = 'party_example' # str | Filter by party. (optional)
    post_transfer_clients_represented = 'post_transfer_clients_represented_example' # str | Filter by post-transfer clients represented. (optional)
    rate_type = 'rate_type_example' # str | Filter by rate type. (optional)
    region = 'region_example' # str | Filter by region. (optional)
    session_type = 'session_type_example' # str | Filter by session type. (optional)
    user_type = 'user_type_example' # str | Filter by user type. (optional)

    try:
        # List Civil Certificated Rates
        api_response = api_instance.lauk_civil_certificated_rate_index(x_api_version=x_api_version, activity=activity, activity_sub_category=activity_sub_category, attended_several_hearings_for_multiple_clients=attended_several_hearings_for_multiple_clients, category_of_law=category_of_law, change_of_solicitor=change_of_solicitor, court=court, eligible_for_sqm=eligible_for_sqm, fee_scheme=fee_scheme, fields=fields, first_conducting_solicitor=first_conducting_solicitor, key=key, limit=limit, number_of_clients=number_of_clients, page_token=page_token, party=party, post_transfer_clients_represented=post_transfer_clients_represented, rate_type=rate_type, region=region, session_type=session_type, user_type=user_type)
        print("The response of CivilCertificatedRatesApi->lauk_civil_certificated_rate_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CivilCertificatedRatesApi->lauk_civil_certificated_rate_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **activity** | **str**| Filter by activity. | [optional] 
 **activity_sub_category** | **str**| Filter by activity sub-category. | [optional] 
 **attended_several_hearings_for_multiple_clients** | **bool**| Filter by whether multiple hearings were attended for multiple clients. | [optional] 
 **category_of_law** | **str**| Filter by category of law. | [optional] 
 **change_of_solicitor** | **bool**| Filter by change of solicitor status. | [optional] 
 **court** | **str**| Filter by court. | [optional] 
 **eligible_for_sqm** | **bool**| Filter by SQM eligibility. | [optional] 
 **fee_scheme** | **str**| Fee scheme | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **first_conducting_solicitor** | **bool**| Filter by first conducting solicitor status. | [optional] 
 **key** | **str**| Filter by key. | [optional] 
 **limit** | **int**| A limit on the number of LaukCivilCertificatedRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **number_of_clients** | **str**| Filter by number of clients. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **party** | **str**| Filter by party. | [optional] 
 **post_transfer_clients_represented** | **str**| Filter by post-transfer clients represented. | [optional] 
 **rate_type** | **str**| Filter by rate type. | [optional] 
 **region** | **str**| Filter by region. | [optional] 
 **session_type** | **str**| Filter by session type. | [optional] 
 **user_type** | **str**| Filter by user type. | [optional] 

### Return type

[**LaukCivilCertificatedRateList**](LaukCivilCertificatedRateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

