# openapi_client.TaskTemplatesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_template_create**](TaskTemplatesApi.md#task_template_create) | **POST** /task_templates.json | Create a new TaskTemplate
[**task_template_destroy**](TaskTemplatesApi.md#task_template_destroy) | **DELETE** /task_templates/{id}.json | Delete a single TaskTemplate
[**task_template_index**](TaskTemplatesApi.md#task_template_index) | **GET** /task_templates.json | Return the data for all TaskTemplates
[**task_template_show**](TaskTemplatesApi.md#task_template_show) | **GET** /task_templates/{id}.json | Return the data for a single TaskTemplate
[**task_template_update**](TaskTemplatesApi.md#task_template_update) | **PATCH** /task_templates/{id}.json | Update a single TaskTemplate


# **task_template_create**
> TaskTemplateShow task_template_create(x_api_version=x_api_version, fields=fields, task_template_create_request=task_template_create_request)

Create a new TaskTemplate

Outlines the parameters and data fields used when creating a new TaskTemplate

### Example


```python
import openapi_client
from openapi_client.models.task_template_create_request import TaskTemplateCreateRequest
from openapi_client.models.task_template_show import TaskTemplateShow
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
    api_instance = openapi_client.TaskTemplatesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_template_create_request = openapi_client.TaskTemplateCreateRequest() # TaskTemplateCreateRequest | Request Body for Task Templates (optional)

    try:
        # Create a new TaskTemplate
        api_response = api_instance.task_template_create(x_api_version=x_api_version, fields=fields, task_template_create_request=task_template_create_request)
        print("The response of TaskTemplatesApi->task_template_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplatesApi->task_template_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_template_create_request** | [**TaskTemplateCreateRequest**](TaskTemplateCreateRequest.md)| Request Body for Task Templates | [optional] 

### Return type

[**TaskTemplateShow**](TaskTemplateShow.md)

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

# **task_template_destroy**
> task_template_destroy(id, x_api_version=x_api_version)

Delete a single TaskTemplate

Outlines the parameters, optional and required, used when deleting the record for a single TaskTemplate

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
    api_instance = openapi_client.TaskTemplatesApi(api_client)
    id = 56 # int | The unique identifier for the TaskTemplate.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single TaskTemplate
        api_instance.task_template_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling TaskTemplatesApi->task_template_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskTemplate. | 
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

# **task_template_index**
> TaskTemplateList task_template_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, priority=priority, query=query, task_template_list_id=task_template_list_id, updated_since=updated_since)

Return the data for all TaskTemplates

Outlines the parameters, optional and required, used when requesting the data for all TaskTemplates

### Example


```python
import openapi_client
from openapi_client.models.task_template_list import TaskTemplateList
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
    api_instance = openapi_client.TaskTemplatesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TaskTemplate records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter TaskTemplate records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of TaskTemplate records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the TaskTemplate records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    priority = 'priority_example' # str | Filter TaskTemplate records to those with the given priority. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching a given string. (optional)
    task_template_list_id = 56 # int | The unique identifier for a single TaskTemplateList. The keyword `null` is not valid for this field. The list will be filtered to include only the TaskTemplate records with the matching property. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TaskTemplate records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all TaskTemplates
        api_response = api_instance.task_template_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, priority=priority, query=query, task_template_list_id=task_template_list_id, updated_since=updated_since)
        print("The response of TaskTemplatesApi->task_template_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplatesApi->task_template_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter TaskTemplate records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter TaskTemplate records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of TaskTemplate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the TaskTemplate records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **priority** | **str**| Filter TaskTemplate records to those with the given priority. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching a given string. | [optional] 
 **task_template_list_id** | **int**| The unique identifier for a single TaskTemplateList. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the TaskTemplate records with the matching property. | [optional] 
 **updated_since** | **datetime**| Filter TaskTemplate records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**TaskTemplateList**](TaskTemplateList.md)

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

# **task_template_show**
> TaskTemplateShow task_template_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single TaskTemplate

Outlines the parameters, optional and required, used when requesting the data for a single TaskTemplate

### Example


```python
import openapi_client
from openapi_client.models.task_template_show import TaskTemplateShow
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
    api_instance = openapi_client.TaskTemplatesApi(api_client)
    id = 56 # int | The unique identifier for the TaskTemplate.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single TaskTemplate
        api_response = api_instance.task_template_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of TaskTemplatesApi->task_template_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplatesApi->task_template_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskTemplate. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**TaskTemplateShow**](TaskTemplateShow.md)

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

# **task_template_update**
> TaskTemplateShow task_template_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_template_update_request=task_template_update_request)

Update a single TaskTemplate

Outlines the parameters and data fields used when updating a single TaskTemplate

### Example


```python
import openapi_client
from openapi_client.models.task_template_show import TaskTemplateShow
from openapi_client.models.task_template_update_request import TaskTemplateUpdateRequest
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
    api_instance = openapi_client.TaskTemplatesApi(api_client)
    id = 56 # int | The unique identifier for the TaskTemplate.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_template_update_request = openapi_client.TaskTemplateUpdateRequest() # TaskTemplateUpdateRequest | Request Body for Task Templates (optional)

    try:
        # Update a single TaskTemplate
        api_response = api_instance.task_template_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_template_update_request=task_template_update_request)
        print("The response of TaskTemplatesApi->task_template_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTemplatesApi->task_template_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TaskTemplate. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_template_update_request** | [**TaskTemplateUpdateRequest**](TaskTemplateUpdateRequest.md)| Request Body for Task Templates | [optional] 

### Return type

[**TaskTemplateShow**](TaskTemplateShow.md)

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

