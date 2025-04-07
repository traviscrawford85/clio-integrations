# openapi_client.TasksApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_create**](TasksApi.md#task_create) | **POST** /tasks.json | Create a new Task
[**task_destroy**](TasksApi.md#task_destroy) | **DELETE** /tasks/{id}.json | Delete a single Task
[**task_index**](TasksApi.md#task_index) | **GET** /tasks.json | Return the data for all Tasks
[**task_show**](TasksApi.md#task_show) | **GET** /tasks/{id}.json | Return the data for a single Task
[**task_update**](TasksApi.md#task_update) | **PATCH** /tasks/{id}.json | Update a single Task


# **task_create**
> TaskShow task_create(x_api_version=x_api_version, fields=fields, task_create_request=task_create_request)

Create a new Task

Outlines the parameters and data fields used when creating a new Task

### Example


```python
import openapi_client
from openapi_client.models.task_create_request import TaskCreateRequest
from openapi_client.models.task_show import TaskShow
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
    api_instance = openapi_client.TasksApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_create_request = openapi_client.TaskCreateRequest() # TaskCreateRequest | Request Body for Tasks (optional)

    try:
        # Create a new Task
        api_response = api_instance.task_create(x_api_version=x_api_version, fields=fields, task_create_request=task_create_request)
        print("The response of TasksApi->task_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->task_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_create_request** | [**TaskCreateRequest**](TaskCreateRequest.md)| Request Body for Tasks | [optional] 

### Return type

[**TaskShow**](TaskShow.md)

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

# **task_destroy**
> task_destroy(id, x_api_version=x_api_version)

Delete a single Task

Outlines the parameters, optional and required, used when deleting the record for a single Task

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
    api_instance = openapi_client.TasksApi(api_client)
    id = 56 # int | The unique identifier for the Task.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Task
        api_instance.task_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling TasksApi->task_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Task. | 
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

# **task_index**
> TaskList task_index(x_api_version=x_api_version, assignee_id=assignee_id, assignee_type=assignee_type, assigner_id=assigner_id, cascading_source_id=cascading_source_id, client_id=client_id, complete=complete, created_since=created_since, due_at_from=due_at_from, due_at_present=due_at_present, due_at_to=due_at_to, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, permission=permission, priority=priority, query=query, responsible_attorney_id=responsible_attorney_id, status=status, statuses=statuses, statute_of_limitations=statute_of_limitations, task_type_id=task_type_id, time_entries_present=time_entries_present, updated_since=updated_since)

Return the data for all Tasks

Outlines the parameters, optional and required, used when requesting the data for all Tasks

### Example


```python
import openapi_client
from openapi_client.models.task_list import TaskList
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
    api_instance = openapi_client.TasksApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    assignee_id = 56 # int | The unique identifier for a single User or Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property. (optional)
    assignee_type = 'assignee_type_example' # str | Filter Task records to those with a specific assignee. Must be passed if filtering by assignee. (optional)
    assigner_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property. (optional)
    cascading_source_id = 56 # int | Filter Task records to those with a parent task that has the specified ID. (optional)
    client_id = 56 # int | The unique identifier for a single Contact. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property. (optional)
    complete = True # bool | Filter Task records to those which are complete or not. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Task records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    due_at_from = '2013-10-20' # date | Start of date range when querying by due_at in a range. (Expects an ISO-8601 date). (optional)
    due_at_present = True # bool | Filter Task records to those that have a due date specified, or not. (optional)
    due_at_to = '2013-10-20' # date | End of date range when querying by due_at in a range. (Expects an ISO-8601 date). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Task records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Task records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property. (optional)
    order = 'order_example' # str | Orders the Task records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    permission = 'permission_example' # str | Filter Task records to those with the given permission. Returns all tasks by default. (optional)
    priority = 'priority_example' # str | Filter Task records to those with the given priority. (optional)
    query = 'query_example' # str | Wildcard search for `name` or `description` matching a given string. (optional)
    responsible_attorney_id = 56 # int | Filter Task records to those that have an associated matter with a responsible attorney ID. (optional)
    status = 'status_example' # str | Filter Task records to those with the given status. Users without advanced tasks enabled may only specify 'complete' or 'pending'. (optional)
    statuses = 'statuses_example' # str | Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify 'complete' or 'pending'. (optional)
    statute_of_limitations = True # bool | Filter Task records to those which are a statute of limitations or not. (optional)
    task_type_id = 56 # int | The unique identifier for a single TaskType. Use the keyword `null` to match those without a Task. The list will be filtered to include only the Task records with the matching property. (optional)
    time_entries_present = True # bool | Filter Task records to those that have associated time entries, or not. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Task records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Tasks
        api_response = api_instance.task_index(x_api_version=x_api_version, assignee_id=assignee_id, assignee_type=assignee_type, assigner_id=assigner_id, cascading_source_id=cascading_source_id, client_id=client_id, complete=complete, created_since=created_since, due_at_from=due_at_from, due_at_present=due_at_present, due_at_to=due_at_to, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, permission=permission, priority=priority, query=query, responsible_attorney_id=responsible_attorney_id, status=status, statuses=statuses, statute_of_limitations=statute_of_limitations, task_type_id=task_type_id, time_entries_present=time_entries_present, updated_since=updated_since)
        print("The response of TasksApi->task_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->task_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **assignee_id** | **int**| The unique identifier for a single User or Contact. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property. | [optional] 
 **assignee_type** | **str**| Filter Task records to those with a specific assignee. Must be passed if filtering by assignee. | [optional] 
 **assigner_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property. | [optional] 
 **cascading_source_id** | **int**| Filter Task records to those with a parent task that has the specified ID. | [optional] 
 **client_id** | **int**| The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property. | [optional] 
 **complete** | **bool**| Filter Task records to those which are complete or not. | [optional] 
 **created_since** | **datetime**| Filter Task records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **due_at_from** | **date**| Start of date range when querying by due_at in a range. (Expects an ISO-8601 date). | [optional] 
 **due_at_present** | **bool**| Filter Task records to those that have a due date specified, or not. | [optional] 
 **due_at_to** | **date**| End of date range when querying by due_at in a range. (Expects an ISO-8601 date). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Task records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Task records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property. | [optional] 
 **order** | **str**| Orders the Task records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **permission** | **str**| Filter Task records to those with the given permission. Returns all tasks by default. | [optional] 
 **priority** | **str**| Filter Task records to those with the given priority. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; or &#x60;description&#x60; matching a given string. | [optional] 
 **responsible_attorney_id** | **int**| Filter Task records to those that have an associated matter with a responsible attorney ID. | [optional] 
 **status** | **str**| Filter Task records to those with the given status. Users without advanced tasks enabled may only specify &#39;complete&#39; or &#39;pending&#39;. | [optional] 
 **statuses** | **str**| Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify &#39;complete&#39; or &#39;pending&#39;. | [optional] 
 **statute_of_limitations** | **bool**| Filter Task records to those which are a statute of limitations or not. | [optional] 
 **task_type_id** | **int**| The unique identifier for a single TaskType. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property. | [optional] 
 **time_entries_present** | **bool**| Filter Task records to those that have associated time entries, or not. | [optional] 
 **updated_since** | **datetime**| Filter Task records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**TaskList**](TaskList.md)

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

# **task_show**
> TaskShow task_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Task

Outlines the parameters, optional and required, used when requesting the data for a single Task

### Example


```python
import openapi_client
from openapi_client.models.task_show import TaskShow
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
    api_instance = openapi_client.TasksApi(api_client)
    id = 56 # int | The unique identifier for the Task.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Task
        api_response = api_instance.task_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of TasksApi->task_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->task_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Task. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**TaskShow**](TaskShow.md)

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

# **task_update**
> TaskShow task_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_update_request=task_update_request)

Update a single Task

Outlines the parameters and data fields used when updating a single Task

### Example


```python
import openapi_client
from openapi_client.models.task_show import TaskShow
from openapi_client.models.task_update_request import TaskUpdateRequest
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
    api_instance = openapi_client.TasksApi(api_client)
    id = 56 # int | The unique identifier for the Task.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    task_update_request = openapi_client.TaskUpdateRequest() # TaskUpdateRequest | Request Body for Tasks (optional)

    try:
        # Update a single Task
        api_response = api_instance.task_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, task_update_request=task_update_request)
        print("The response of TasksApi->task_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->task_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Task. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **task_update_request** | [**TaskUpdateRequest**](TaskUpdateRequest.md)| Request Body for Tasks | [optional] 

### Return type

[**TaskShow**](TaskShow.md)

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

