# openapi_client.TaskTypesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_type_create**](TaskTypesApi.md#task_type_create) | **POST** /task_types.json | Create a new TaskType
[**task_type_index**](TaskTypesApi.md#task_type_index) | **GET** /task_types.json | Return the data for all TaskTypes
[**task_type_show**](TaskTypesApi.md#task_type_show) | **GET** /task_types/{id}.json | Return the data for a single TaskType
[**task_type_update**](TaskTypesApi.md#task_type_update) | **PATCH** /task_types/{id}.json | Update a single TaskType


# **task_type_create**
> TaskTypeShow task_type_create(x_api_version=x_api_version, fields=fields, task_type_create_request=task_type_create_request)

Create a new TaskType

Outlines the parameters and data fields used when creating a new TaskType

### Example


```python
import openapi_client
from openapi_client.models.task_type_create_request import TaskTypeCreateRequest
from openapi_client.models.task_type_show import TaskTypeShow
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_type_create_request = openapi_client.TaskTypeCreateRequest() # TaskTypeCreateRequest | Request Body for Task Types (optional)

    try:
        # Create a new TaskType
        api_response = api_instance.task_type_create(x_api_version=x_api_version, fields=fields, task_type_create_request=task_type_create_request)
        print("The response of TaskTypesApi->task_type_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->task_type_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_type_create_request** | [**TaskTypeCreateRequest**](TaskTypeCreateRequest.md)| Request Body for Task Types | [optional] 

### Return type

[**TaskTypeShow**](TaskTypeShow.md)

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

# **task_type_index**
> TaskTypeList task_type_index(x_api_version=x_api_version, created_since=created_since, enabled=enabled, fields=fields, ids=ids, limit=limit, name=name, order=order, page_token=page_token, query=query, updated_since=updated_since)

Return the data for all TaskTypes

Outlines the parameters, optional and required, used when requesting the data for all TaskTypes

### Example


```python
import openapi_client
from openapi_client.models.task_type_list import TaskTypeList
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TaskType records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    enabled = True # bool | Filter TaskType records to those that are enabled or disabled. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter TaskType records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of TaskType records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    name = 'name_example' # str | Filter TaskType records to those with the given name. (optional)
    order = 'order_example' # str | Orders the TaskType records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TaskType records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all TaskTypes
        api_response = api_instance.task_type_index(x_api_version=x_api_version, created_since=created_since, enabled=enabled, fields=fields, ids=ids, limit=limit, name=name, order=order, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of TaskTypesApi->task_type_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->task_type_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter TaskType records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **enabled** | **bool**| Filter TaskType records to those that are enabled or disabled. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter TaskType records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of TaskType records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **name** | **str**| Filter TaskType records to those with the given name. | [optional] 
 **order** | **str**| Orders the TaskType records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter TaskType records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**TaskTypeList**](TaskTypeList.md)

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

# **task_type_show**
> TaskTypeShow task_type_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single TaskType

Outlines the parameters, optional and required, used when requesting the data for a single TaskType

### Example


```python
import openapi_client
from openapi_client.models.task_type_show import TaskTypeShow
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    id = 56 # int | The unique identifier for the TaskType.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single TaskType
        api_response = api_instance.task_type_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of TaskTypesApi->task_type_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->task_type_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskType. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**TaskTypeShow**](TaskTypeShow.md)

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

# **task_type_update**
> TaskTypeShow task_type_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_type_update_request=task_type_update_request)

Update a single TaskType

Outlines the parameters and data fields used when updating a single TaskType

### Example


```python
import openapi_client
from openapi_client.models.task_type_show import TaskTypeShow
from openapi_client.models.task_type_update_request import TaskTypeUpdateRequest
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    id = 56 # int | The unique identifier for the TaskType.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_type_update_request = openapi_client.TaskTypeUpdateRequest() # TaskTypeUpdateRequest | Request Body for Task Types (optional)

    try:
        # Update a single TaskType
        api_response = api_instance.task_type_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_type_update_request=task_type_update_request)
        print("The response of TaskTypesApi->task_type_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->task_type_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskType. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_type_update_request** | [**TaskTypeUpdateRequest**](TaskTypeUpdateRequest.md)| Request Body for Task Types | [optional] 

### Return type

[**TaskTypeShow**](TaskTypeShow.md)

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

