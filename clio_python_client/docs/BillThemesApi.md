# openapi_client.BillThemesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bill_theme_index**](BillThemesApi.md#bill_theme_index) | **GET** /bill_themes.json | Return the data for all BillThemes
[**bill_theme_update**](BillThemesApi.md#bill_theme_update) | **PATCH** /bill_themes/{id}.json | Update a single BillTheme


# **bill_theme_index**
> BillThemeList bill_theme_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)

Return the data for all BillThemes

Outlines the parameters, optional and required, used when requesting the data for all BillThemes

### Example


```python
import openapi_client
from openapi_client.models.bill_theme_list import BillThemeList
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
    api_instance = openapi_client.BillThemesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter BillTheme records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter BillTheme records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of BillTheme records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter BillTheme records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all BillThemes
        api_response = api_instance.bill_theme_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)
        print("The response of BillThemesApi->bill_theme_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillThemesApi->bill_theme_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter BillTheme records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter BillTheme records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of BillTheme records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter BillTheme records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**BillThemeList**](BillThemeList.md)

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

# **bill_theme_update**
> BillThemeShow bill_theme_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, bill_theme_update_request=bill_theme_update_request)

Update a single BillTheme

Outlines the parameters and data fields used when updating a single BillTheme

### Example


```python
import openapi_client
from openapi_client.models.bill_theme_show import BillThemeShow
from openapi_client.models.bill_theme_update_request import BillThemeUpdateRequest
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
    api_instance = openapi_client.BillThemesApi(api_client)
    id = 56 # int | The unique identifier for the BillTheme.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    bill_theme_update_request = openapi_client.BillThemeUpdateRequest() # BillThemeUpdateRequest | Request Body for Bill Themes (optional)

    try:
        # Update a single BillTheme
        api_response = api_instance.bill_theme_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, bill_theme_update_request=bill_theme_update_request)
        print("The response of BillThemesApi->bill_theme_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillThemesApi->bill_theme_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the BillTheme. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **bill_theme_update_request** | [**BillThemeUpdateRequest**](BillThemeUpdateRequest.md)| Request Body for Bill Themes | [optional] 

### Return type

[**BillThemeShow**](BillThemeShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

