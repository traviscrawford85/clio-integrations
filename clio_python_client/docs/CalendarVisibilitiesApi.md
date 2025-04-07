# openapi_client.CalendarVisibilitiesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_visibility_index**](CalendarVisibilitiesApi.md#calendar_visibility_index) | **GET** /task_calendars.json | Return the data for all CalendarVisibilities
[**calendar_visibility_show**](CalendarVisibilitiesApi.md#calendar_visibility_show) | **GET** /task_calendars/{id}.json | Return the data for a single CalendarVisibility
[**calendar_visibility_update**](CalendarVisibilitiesApi.md#calendar_visibility_update) | **PATCH** /task_calendars/{id}.json | Update a single CalendarVisibility


# **calendar_visibility_index**
> CalendarVisibilityList calendar_visibility_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)

Return the data for all CalendarVisibilities

Outlines the parameters, optional and required, used when requesting the data for all CalendarVisibilities

### Example


```python
import openapi_client
from openapi_client.models.calendar_visibility_list import CalendarVisibilityList
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
    api_instance = openapi_client.CalendarVisibilitiesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter CalendarVisibility records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter CalendarVisibility records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of CalendarVisibility records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter CalendarVisibility records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all CalendarVisibilities
        api_response = api_instance.calendar_visibility_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)
        print("The response of CalendarVisibilitiesApi->calendar_visibility_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarVisibilitiesApi->calendar_visibility_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter CalendarVisibility records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter CalendarVisibility records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of CalendarVisibility records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter CalendarVisibility records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**CalendarVisibilityList**](CalendarVisibilityList.md)

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

# **calendar_visibility_show**
> CalendarVisibilityShow calendar_visibility_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single CalendarVisibility

Outlines the parameters, optional and required, used when requesting the data for a single CalendarVisibility

### Example


```python
import openapi_client
from openapi_client.models.calendar_visibility_show import CalendarVisibilityShow
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
    api_instance = openapi_client.CalendarVisibilitiesApi(api_client)
    id = 56 # int | The unique identifier for the CalendarVisibility.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single CalendarVisibility
        api_response = api_instance.calendar_visibility_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of CalendarVisibilitiesApi->calendar_visibility_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarVisibilitiesApi->calendar_visibility_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CalendarVisibility. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**CalendarVisibilityShow**](CalendarVisibilityShow.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_visibility_update**
> CalendarVisibilityShow calendar_visibility_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, calendar_visibility_update_request=calendar_visibility_update_request)

Update a single CalendarVisibility

Outlines the parameters and data fields used when updating a single CalendarVisibility

### Example


```python
import openapi_client
from openapi_client.models.calendar_visibility_show import CalendarVisibilityShow
from openapi_client.models.calendar_visibility_update_request import CalendarVisibilityUpdateRequest
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
    api_instance = openapi_client.CalendarVisibilitiesApi(api_client)
    id = 56 # int | The unique identifier for the CalendarVisibility.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    calendar_visibility_update_request = openapi_client.CalendarVisibilityUpdateRequest() # CalendarVisibilityUpdateRequest | Request Body for Task Calendars (optional)

    try:
        # Update a single CalendarVisibility
        api_response = api_instance.calendar_visibility_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, calendar_visibility_update_request=calendar_visibility_update_request)
        print("The response of CalendarVisibilitiesApi->calendar_visibility_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarVisibilitiesApi->calendar_visibility_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CalendarVisibility. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **calendar_visibility_update_request** | [**CalendarVisibilityUpdateRequest**](CalendarVisibilityUpdateRequest.md)| Request Body for Task Calendars | [optional] 

### Return type

[**CalendarVisibilityShow**](CalendarVisibilityShow.md)

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

