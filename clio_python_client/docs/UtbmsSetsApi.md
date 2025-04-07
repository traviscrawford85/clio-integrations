# openapi_client.UtbmsSetsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utbms_set_index**](UtbmsSetsApi.md#utbms_set_index) | **GET** /utbms/sets.json | Return the data for all the utbms sets


# **utbms_set_index**
> UtbmsSetList utbms_set_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, updated_since=updated_since)

Return the data for all the utbms sets

Outlines the parameters, optional and required, used when requesting the data for all UtbmsSets

### Example


```python
import openapi_client
from openapi_client.models.utbms_set_list import UtbmsSetList
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
    api_instance = openapi_client.UtbmsSetsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter UtbmsSet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter UtbmsSet records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of UtbmsSet records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the UtbmsSet records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter UtbmsSet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all the utbms sets
        api_response = api_instance.utbms_set_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, updated_since=updated_since)
        print("The response of UtbmsSetsApi->utbms_set_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtbmsSetsApi->utbms_set_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter UtbmsSet records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter UtbmsSet records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of UtbmsSet records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the UtbmsSet records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter UtbmsSet records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**UtbmsSetList**](UtbmsSetList.md)

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

