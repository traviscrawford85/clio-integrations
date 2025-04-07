# openapi_client.CriminalControlledRatesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lauk_criminal_controlled_rate_index**](CriminalControlledRatesApi.md#lauk_criminal_controlled_rate_index) | **GET** /lauk_criminal_controlled_rates.json | List Criminal Controlled Rates


# **lauk_criminal_controlled_rate_index**
> LaukCriminalControlledRateList lauk_criminal_controlled_rate_index(x_api_version=x_api_version, activity=activity, category_of_law=category_of_law, counsel=counsel, court=court, fields=fields, key=key, limit=limit, page_token=page_token, rate_type=rate_type, region=region, solicitor_type=solicitor_type, standard_fee_category=standard_fee_category)

List Criminal Controlled Rates

Outlines the parameters, optional and required, used when requesting the data for all LaukCriminalControlledRates

### Example


```python
import openapi_client
from openapi_client.models.lauk_criminal_controlled_rate_list import LaukCriminalControlledRateList
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
    api_instance = openapi_client.CriminalControlledRatesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    activity = 'activity_example' # str | Filter by activity. (optional)
    category_of_law = 'category_of_law_example' # str | Filter by category of law. (optional)
    counsel = 'counsel_example' # str | Filter by counsel. (optional)
    court = 'court_example' # str | Filter by court. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    key = 'key_example' # str | Filter by key. (optional)
    limit = 56 # int | A limit on the number of LaukCriminalControlledRate records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    rate_type = 'rate_type_example' # str | Filter by rate type. (optional)
    region = 'region_example' # str | Filter by region. (optional)
    solicitor_type = 'solicitor_type_example' # str | Filter by solicitor type. (optional)
    standard_fee_category = 'standard_fee_category_example' # str | Filter by standard fee category. (optional)

    try:
        # List Criminal Controlled Rates
        api_response = api_instance.lauk_criminal_controlled_rate_index(x_api_version=x_api_version, activity=activity, category_of_law=category_of_law, counsel=counsel, court=court, fields=fields, key=key, limit=limit, page_token=page_token, rate_type=rate_type, region=region, solicitor_type=solicitor_type, standard_fee_category=standard_fee_category)
        print("The response of CriminalControlledRatesApi->lauk_criminal_controlled_rate_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CriminalControlledRatesApi->lauk_criminal_controlled_rate_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **activity** | **str**| Filter by activity. | [optional] 
 **category_of_law** | **str**| Filter by category of law. | [optional] 
 **counsel** | **str**| Filter by counsel. | [optional] 
 **court** | **str**| Filter by court. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **key** | **str**| Filter by key. | [optional] 
 **limit** | **int**| A limit on the number of LaukCriminalControlledRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **rate_type** | **str**| Filter by rate type. | [optional] 
 **region** | **str**| Filter by region. | [optional] 
 **solicitor_type** | **str**| Filter by solicitor type. | [optional] 
 **standard_fee_category** | **str**| Filter by standard fee category. | [optional] 

### Return type

[**LaukCriminalControlledRateList**](LaukCriminalControlledRateList.md)

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

