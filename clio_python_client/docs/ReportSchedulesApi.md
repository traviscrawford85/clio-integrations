# openapi_client.ReportSchedulesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_schedule_create**](ReportSchedulesApi.md#report_schedule_create) | **POST** /report_schedules.json | Create a new ReportSchedule
[**report_schedule_destroy**](ReportSchedulesApi.md#report_schedule_destroy) | **DELETE** /report_schedules/{id}.json | Delete a single ReportSchedule
[**report_schedule_index**](ReportSchedulesApi.md#report_schedule_index) | **GET** /report_schedules.json | Return the data for all ReportSchedules
[**report_schedule_show**](ReportSchedulesApi.md#report_schedule_show) | **GET** /report_schedules/{id}.json | Return the data for a single ReportSchedule
[**report_schedule_update**](ReportSchedulesApi.md#report_schedule_update) | **PATCH** /report_schedules/{id}.json | Update a single ReportSchedule


# **report_schedule_create**
> ReportScheduleShow report_schedule_create(x_api_version=x_api_version, fields=fields, report_schedule_create_request=report_schedule_create_request)

Create a new ReportSchedule

Outlines the parameters and data fields used when creating a new ReportSchedule

### Example


```python
import openapi_client
from openapi_client.models.report_schedule_create_request import ReportScheduleCreateRequest
from openapi_client.models.report_schedule_show import ReportScheduleShow
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
    api_instance = openapi_client.ReportSchedulesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    report_schedule_create_request = openapi_client.ReportScheduleCreateRequest() # ReportScheduleCreateRequest | Request Body for Report Schedules (optional)

    try:
        # Create a new ReportSchedule
        api_response = api_instance.report_schedule_create(x_api_version=x_api_version, fields=fields, report_schedule_create_request=report_schedule_create_request)
        print("The response of ReportSchedulesApi->report_schedule_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportSchedulesApi->report_schedule_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **report_schedule_create_request** | [**ReportScheduleCreateRequest**](ReportScheduleCreateRequest.md)| Request Body for Report Schedules | [optional] 

### Return type

[**ReportScheduleShow**](ReportScheduleShow.md)

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

# **report_schedule_destroy**
> report_schedule_destroy(id, x_api_version=x_api_version)

Delete a single ReportSchedule

Outlines the parameters, optional and required, used when deleting the record for a single ReportSchedule

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
    api_instance = openapi_client.ReportSchedulesApi(api_client)
    id = 56 # int | The unique identifier for the ReportSchedule.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single ReportSchedule
        api_instance.report_schedule_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ReportSchedulesApi->report_schedule_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ReportSchedule. | 
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

# **report_schedule_index**
> ReportScheduleList report_schedule_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)

Return the data for all ReportSchedules

Outlines the parameters, optional and required, used when requesting the data for all ReportSchedules

### Example


```python
import openapi_client
from openapi_client.models.report_schedule_list import ReportScheduleList
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
    api_instance = openapi_client.ReportSchedulesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ReportSchedule records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter ReportSchedule records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of ReportSchedule records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ReportSchedule records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all ReportSchedules
        api_response = api_instance.report_schedule_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)
        print("The response of ReportSchedulesApi->report_schedule_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportSchedulesApi->report_schedule_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter ReportSchedule records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter ReportSchedule records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of ReportSchedule records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter ReportSchedule records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ReportScheduleList**](ReportScheduleList.md)

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

# **report_schedule_show**
> ReportScheduleShow report_schedule_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single ReportSchedule

Outlines the parameters, optional and required, used when requesting the data for a single ReportSchedule

### Example


```python
import openapi_client
from openapi_client.models.report_schedule_show import ReportScheduleShow
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
    api_instance = openapi_client.ReportSchedulesApi(api_client)
    id = 56 # int | The unique identifier for the ReportSchedule.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single ReportSchedule
        api_response = api_instance.report_schedule_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ReportSchedulesApi->report_schedule_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportSchedulesApi->report_schedule_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ReportSchedule. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ReportScheduleShow**](ReportScheduleShow.md)

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

# **report_schedule_update**
> ReportScheduleShow report_schedule_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, report_schedule_update_request=report_schedule_update_request)

Update a single ReportSchedule

Outlines the parameters and data fields used when updating a single ReportSchedule

### Example


```python
import openapi_client
from openapi_client.models.report_schedule_show import ReportScheduleShow
from openapi_client.models.report_schedule_update_request import ReportScheduleUpdateRequest
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
    api_instance = openapi_client.ReportSchedulesApi(api_client)
    id = 56 # int | The unique identifier for the ReportSchedule.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    report_schedule_update_request = openapi_client.ReportScheduleUpdateRequest() # ReportScheduleUpdateRequest | Request Body for Report Schedules (optional)

    try:
        # Update a single ReportSchedule
        api_response = api_instance.report_schedule_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, report_schedule_update_request=report_schedule_update_request)
        print("The response of ReportSchedulesApi->report_schedule_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportSchedulesApi->report_schedule_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ReportSchedule. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **report_schedule_update_request** | [**ReportScheduleUpdateRequest**](ReportScheduleUpdateRequest.md)| Request Body for Report Schedules | [optional] 

### Return type

[**ReportScheduleShow**](ReportScheduleShow.md)

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

