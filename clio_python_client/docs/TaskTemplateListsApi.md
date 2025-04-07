# openapi_client.TaskTemplateListsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_template_list_copy**](TaskTemplateListsApi.md#task_template_list_copy) | **POST** /task_template_lists/{id}/copy.json | Copy a TaskTemplateList
[**task_template_list_create**](TaskTemplateListsApi.md#task_template_list_create) | **POST** /task_template_lists.json | Create a new TaskTemplateList
[**task_template_list_destroy**](TaskTemplateListsApi.md#task_template_list_destroy) | **DELETE** /task_template_lists/{id}.json | Delete a single TaskTemplateList
[**task_template_list_index**](TaskTemplateListsApi.md#task_template_list_index) | **GET** /task_template_lists.json | Return the data for all TaskTemplateLists
[**task_template_list_show**](TaskTemplateListsApi.md#task_template_list_show) | **GET** /task_template_lists/{id}.json | Return the data for a single TaskTemplateList
[**task_template_list_update**](TaskTemplateListsApi.md#task_template_list_update) | **PATCH** /task_template_lists/{id}.json | Update a single TaskTemplateList


# **task_template_list_copy**
> TaskTemplateListShow task_template_list_copy(id, fields=fields, task_template_list_copy_request=task_template_list_copy_request)

Copy a TaskTemplateList

Creates a copy of the TaskTemplateList identified by the `id` path parameter. 

### Example


```python
import openapi_client
from openapi_client.models.task_template_list_copy_request import TaskTemplateListCopyRequest
from openapi_client.models.task_template_list_show import TaskTemplateListShow
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
    api_instance = openapi_client.TaskTemplateListsApi(api_client)
    id = 56 # int | The unique identifier for the TaskTemplateList.
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_template_list_copy_request = openapi_client.TaskTemplateListCopyRequest() # TaskTemplateListCopyRequest | Request Body for Task Template Lists (optional)

    try:
        # Copy a TaskTemplateList
        api_response = api_instance.task_template_list_copy(id, fields=fields, task_template_list_copy_request=task_template_list_copy_request)
        print("The response of TaskTemplateListsApi->task_template_list_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplateListsApi->task_template_list_copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskTemplateList. | 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_template_list_copy_request** | [**TaskTemplateListCopyRequest**](TaskTemplateListCopyRequest.md)| Request Body for Task Template Lists | [optional] 

### Return type

[**TaskTemplateListShow**](TaskTemplateListShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_template_list_create**
> TaskTemplateListShow task_template_list_create(x_api_version=x_api_version, fields=fields, task_template_list_create_request=task_template_list_create_request)

Create a new TaskTemplateList

Outlines the parameters and data fields used when creating a new TaskTemplateList

### Example


```python
import openapi_client
from openapi_client.models.task_template_list_create_request import TaskTemplateListCreateRequest
from openapi_client.models.task_template_list_show import TaskTemplateListShow
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
    api_instance = openapi_client.TaskTemplateListsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_template_list_create_request = openapi_client.TaskTemplateListCreateRequest() # TaskTemplateListCreateRequest | Request Body for Task Template Lists (optional)

    try:
        # Create a new TaskTemplateList
        api_response = api_instance.task_template_list_create(x_api_version=x_api_version, fields=fields, task_template_list_create_request=task_template_list_create_request)
        print("The response of TaskTemplateListsApi->task_template_list_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplateListsApi->task_template_list_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_template_list_create_request** | [**TaskTemplateListCreateRequest**](TaskTemplateListCreateRequest.md)| Request Body for Task Template Lists | [optional] 

### Return type

[**TaskTemplateListShow**](TaskTemplateListShow.md)

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

# **task_template_list_destroy**
> task_template_list_destroy(id, x_api_version=x_api_version)

Delete a single TaskTemplateList

Outlines the parameters, optional and required, used when deleting the record for a single TaskTemplateList

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
    api_instance = openapi_client.TaskTemplateListsApi(api_client)
    id = 56 # int | The unique identifier for the TaskTemplateList.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single TaskTemplateList
        api_instance.task_template_list_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling TaskTemplateListsApi->task_template_list_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskTemplateList. | 
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

# **task_template_list_index**
> TaskTemplateListList task_template_list_index(x_api_version=x_api_version, created_since=created_since, empty=empty, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, practice_area_id=practice_area_id, query=query, updated_since=updated_since)

Return the data for all TaskTemplateLists

Outlines the parameters, optional and required, used when requesting the data for all TaskTemplateLists

### Example


```python
import openapi_client
from openapi_client.models.task_template_list_list import TaskTemplateListList
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
    api_instance = openapi_client.TaskTemplateListsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TaskTemplateList records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    empty = True # bool | Filter TaskTemplateList records to those that either contain at least one task template or contain none. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter TaskTemplateList records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of TaskTemplateList records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the TaskTemplateList records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    practice_area_id = 56 # int | The unique identifier for a single PracticeArea. Use the keyword `null` to match those without a TaskTemplateList. The list will be filtered to include only the TaskTemplateList records with the matching property. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TaskTemplateList records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all TaskTemplateLists
        api_response = api_instance.task_template_list_index(x_api_version=x_api_version, created_since=created_since, empty=empty, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, practice_area_id=practice_area_id, query=query, updated_since=updated_since)
        print("The response of TaskTemplateListsApi->task_template_list_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplateListsApi->task_template_list_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter TaskTemplateList records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **empty** | **bool**| Filter TaskTemplateList records to those that either contain at least one task template or contain none. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter TaskTemplateList records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of TaskTemplateList records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the TaskTemplateList records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **practice_area_id** | **int**| The unique identifier for a single PracticeArea. Use the keyword &#x60;null&#x60; to match those without a TaskTemplateList. The list will be filtered to include only the TaskTemplateList records with the matching property. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter TaskTemplateList records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**TaskTemplateListList**](TaskTemplateListList.md)

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

# **task_template_list_show**
> TaskTemplateListShow task_template_list_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single TaskTemplateList

Outlines the parameters, optional and required, used when requesting the data for a single TaskTemplateList

### Example


```python
import openapi_client
from openapi_client.models.task_template_list_show import TaskTemplateListShow
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
    api_instance = openapi_client.TaskTemplateListsApi(api_client)
    id = 56 # int | The unique identifier for the TaskTemplateList.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single TaskTemplateList
        api_response = api_instance.task_template_list_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of TaskTemplateListsApi->task_template_list_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplateListsApi->task_template_list_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskTemplateList. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**TaskTemplateListShow**](TaskTemplateListShow.md)

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

# **task_template_list_update**
> TaskTemplateListShow task_template_list_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_template_list_update_request=task_template_list_update_request)

Update a single TaskTemplateList

Outlines the parameters and data fields used when updating a single TaskTemplateList

### Example


```python
import openapi_client
from openapi_client.models.task_template_list_show import TaskTemplateListShow
from openapi_client.models.task_template_list_update_request import TaskTemplateListUpdateRequest
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
    api_instance = openapi_client.TaskTemplateListsApi(api_client)
    id = 56 # int | The unique identifier for the TaskTemplateList.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_template_list_update_request = openapi_client.TaskTemplateListUpdateRequest() # TaskTemplateListUpdateRequest | Request Body for Task Template Lists (optional)

    try:
        # Update a single TaskTemplateList
        api_response = api_instance.task_template_list_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_template_list_update_request=task_template_list_update_request)
        print("The response of TaskTemplateListsApi->task_template_list_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplateListsApi->task_template_list_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskTemplateList. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_template_list_update_request** | [**TaskTemplateListUpdateRequest**](TaskTemplateListUpdateRequest.md)| Request Body for Task Template Lists | [optional] 

### Return type

[**TaskTemplateListShow**](TaskTemplateListShow.md)

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

