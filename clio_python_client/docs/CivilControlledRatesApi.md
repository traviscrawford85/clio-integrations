# openapi_client.CivilControlledRatesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lauk_civil_controlled_rate_index**](CivilControlledRatesApi.md#lauk_civil_controlled_rate_index) | **GET** /lauk_civil_controlled_rates.json | List Civil Controlled Rates


# **lauk_civil_controlled_rate_index**
> LaukCivilControlledRateList lauk_civil_controlled_rate_index(x_api_version=x_api_version, activity=activity, category_of_law=category_of_law, fields=fields, key=key, limit=limit, matter_type_1=matter_type_1, matter_type_2=matter_type_2, page_token=page_token, rate_type=rate_type, region=region)

List Civil Controlled Rates

Outlines the parameters, optional and required, used when requesting the data for all LaukCivilControlledRates

### Example


```python
import openapi_client
from openapi_client.models.lauk_civil_controlled_rate_list import LaukCivilControlledRateList
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
    api_instance = openapi_client.CivilControlledRatesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    activity = 'activity_example' # str | Filter by activity. (optional)
    category_of_law = 'category_of_law_example' # str | Filter by category of law. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    key = 'key_example' # str | Filter by key. (optional)
    limit = 56 # int | A limit on the number of LaukCivilControlledRate records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_type_1 = 56 # int | Filter by matter type 1. (optional)
    matter_type_2 = 56 # int | Filter by matter type 2. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    rate_type = 'rate_type_example' # str | Filter by rate type. (optional)
    region = 'region_example' # str | Filter by region. (optional)

    try:
        # List Civil Controlled Rates
        api_response = api_instance.lauk_civil_controlled_rate_index(x_api_version=x_api_version, activity=activity, category_of_law=category_of_law, fields=fields, key=key, limit=limit, matter_type_1=matter_type_1, matter_type_2=matter_type_2, page_token=page_token, rate_type=rate_type, region=region)
        print("The response of CivilControlledRatesApi->lauk_civil_controlled_rate_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CivilControlledRatesApi->lauk_civil_controlled_rate_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **activity** | **str**| Filter by activity. | [optional] 
 **category_of_law** | **str**| Filter by category of law. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **key** | **str**| Filter by key. | [optional] 
 **limit** | **int**| A limit on the number of LaukCivilControlledRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_type_1** | **int**| Filter by matter type 1. | [optional] 
 **matter_type_2** | **int**| Filter by matter type 2. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **rate_type** | **str**| Filter by rate type. | [optional] 
 **region** | **str**| Filter by region. | [optional] 

### Return type

[**LaukCivilControlledRateList**](LaukCivilControlledRateList.md)

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

