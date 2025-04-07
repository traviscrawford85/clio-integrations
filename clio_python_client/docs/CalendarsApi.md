# openapi_client.CalendarsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_create**](CalendarsApi.md#calendar_create) | **POST** /calendars.json | Create a new Calendar
[**calendar_destroy**](CalendarsApi.md#calendar_destroy) | **DELETE** /calendars/{id}.json | Delete a single Calendar
[**calendar_index**](CalendarsApi.md#calendar_index) | **GET** /calendars.json | Return the data for all Calendars
[**calendar_show**](CalendarsApi.md#calendar_show) | **GET** /calendars/{id}.json | Return the data for a single Calendar
[**calendar_update**](CalendarsApi.md#calendar_update) | **PATCH** /calendars/{id}.json | Update a single Calendar


# **calendar_create**
> CalendarShow calendar_create(x_api_version=x_api_version, fields=fields, calendar_create_request=calendar_create_request)

Create a new Calendar

Outlines the parameters and data fields used when creating a new Calendar

### Example


```python
import openapi_client
from openapi_client.models.calendar_create_request import CalendarCreateRequest
from openapi_client.models.calendar_show import CalendarShow
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
    api_instance = openapi_client.CalendarsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    calendar_create_request = openapi_client.CalendarCreateRequest() # CalendarCreateRequest | Request Body for Calendars (optional)

    try:
        # Create a new Calendar
        api_response = api_instance.calendar_create(x_api_version=x_api_version, fields=fields, calendar_create_request=calendar_create_request)
        print("The response of CalendarsApi->calendar_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendar_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **calendar_create_request** | [**CalendarCreateRequest**](CalendarCreateRequest.md)| Request Body for Calendars | [optional] 

### Return type

[**CalendarShow**](CalendarShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_destroy**
> calendar_destroy(id, x_api_version=x_api_version)

Delete a single Calendar

Outlines the parameters, optional and required, used when deleting the record for a single Calendar

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CalendarsApi(api_client)
    id = 56 # int | The unique identifier for the Calendar.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Calendar
        api_instance.calendar_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendar_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Calendar. | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_index**
> CalendarList calendar_index(x_api_version=x_api_version, created_since=created_since, fields=fields, filter_inactive_users=filter_inactive_users, ids=ids, limit=limit, order=order, owner=owner, page_token=page_token, source=source, type=type, updated_since=updated_since, visible=visible, writeable=writeable)

Return the data for all Calendars

Outlines the parameters, optional and required, used when requesting the data for all Calendars

### Example


```python
import openapi_client
from openapi_client.models.calendar_list import CalendarList
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
    api_instance = openapi_client.CalendarsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Calendar records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    filter_inactive_users = True # bool | Filter any shared UserCalendar records whose owner is inactive. (optional)
    ids = 56 # int | Filter Calendar records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Calendar records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the Calendar records by the given field. Default: `id(asc)`. (optional)
    owner = True # bool | Filter Calendar records to those that the user owns. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    source = 'source_example' # str | Filter Calendar records to those having a specific calendar visibility source (mobile, web). (optional)
    type = 'type_example' # str | Filter Calendar records to those of the specified type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Calendar records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    visible = True # bool | Filter Calendar records to those that are visible. (optional)
    writeable = True # bool | Filter Calendar records to those which the user can write to. (optional)

    try:
        # Return the data for all Calendars
        api_response = api_instance.calendar_index(x_api_version=x_api_version, created_since=created_since, fields=fields, filter_inactive_users=filter_inactive_users, ids=ids, limit=limit, order=order, owner=owner, page_token=page_token, source=source, type=type, updated_since=updated_since, visible=visible, writeable=writeable)
        print("The response of CalendarsApi->calendar_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendar_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter Calendar records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **filter_inactive_users** | **bool**| Filter any shared UserCalendar records whose owner is inactive. | [optional] 
 **ids** | **int**| Filter Calendar records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Calendar records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the Calendar records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **owner** | **bool**| Filter Calendar records to those that the user owns. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **source** | **str**| Filter Calendar records to those having a specific calendar visibility source (mobile, web). | [optional] 
 **type** | **str**| Filter Calendar records to those of the specified type. | [optional] 
 **updated_since** | **datetime**| Filter Calendar records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **visible** | **bool**| Filter Calendar records to those that are visible. | [optional] 
 **writeable** | **bool**| Filter Calendar records to those which the user can write to. | [optional] 

### Return type

[**CalendarList**](CalendarList.md)

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

# **calendar_show**
> CalendarShow calendar_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Calendar

Outlines the parameters, optional and required, used when requesting the data for a single Calendar

### Example


```python
import openapi_client
from openapi_client.models.calendar_show import CalendarShow
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
    api_instance = openapi_client.CalendarsApi(api_client)
    id = 56 # int | The unique identifier for the Calendar.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Calendar
        api_response = api_instance.calendar_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of CalendarsApi->calendar_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendar_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Calendar. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**CalendarShow**](CalendarShow.md)

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

# **calendar_update**
> CalendarShow calendar_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, calendar_update_request=calendar_update_request)

Update a single Calendar

Outlines the parameters and data fields used when updating a single Calendar

### Example


```python
import openapi_client
from openapi_client.models.calendar_show import CalendarShow
from openapi_client.models.calendar_update_request import CalendarUpdateRequest
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
    api_instance = openapi_client.CalendarsApi(api_client)
    id = 56 # int | The unique identifier for the Calendar.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    calendar_update_request = openapi_client.CalendarUpdateRequest() # CalendarUpdateRequest | Request Body for Calendars (optional)

    try:
        # Update a single Calendar
        api_response = api_instance.calendar_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, calendar_update_request=calendar_update_request)
        print("The response of CalendarsApi->calendar_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendar_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Calendar. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **calendar_update_request** | [**CalendarUpdateRequest**](CalendarUpdateRequest.md)| Request Body for Calendars | [optional] 

### Return type

[**CalendarShow**](CalendarShow.md)

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

