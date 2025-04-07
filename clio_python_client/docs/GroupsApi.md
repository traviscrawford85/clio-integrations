# openapi_client.GroupsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_create**](GroupsApi.md#group_create) | **POST** /groups.json | Create a new Group
[**group_destroy**](GroupsApi.md#group_destroy) | **DELETE** /groups/{id}.json | Delete a single Group
[**group_index**](GroupsApi.md#group_index) | **GET** /groups.json | Return the data for all Groups
[**group_show**](GroupsApi.md#group_show) | **GET** /groups/{id}.json | Return the data for a single Group
[**group_update**](GroupsApi.md#group_update) | **PATCH** /groups/{id}.json | Update a single Group


# **group_create**
> GroupShow group_create(x_api_version=x_api_version, fields=fields, group_create_request=group_create_request)

Create a new Group

Outlines the parameters and data fields used when creating a new Group

### Example


```python
import openapi_client
from openapi_client.models.group_create_request import GroupCreateRequest
from openapi_client.models.group_show import GroupShow
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
    api_instance = openapi_client.GroupsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    group_create_request = openapi_client.GroupCreateRequest() # GroupCreateRequest | Request Body for Groups (optional)

    try:
        # Create a new Group
        api_response = api_instance.group_create(x_api_version=x_api_version, fields=fields, group_create_request=group_create_request)
        print("The response of GroupsApi->group_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->group_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **group_create_request** | [**GroupCreateRequest**](GroupCreateRequest.md)| Request Body for Groups | [optional] 

### Return type

[**GroupShow**](GroupShow.md)

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

# **group_destroy**
> group_destroy(id, x_api_version=x_api_version)

Delete a single Group

Outlines the parameters, optional and required, used when deleting the record for a single Group

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
    api_instance = openapi_client.GroupsApi(api_client)
    id = 56 # int | The unique identifier for the Group.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Group
        api_instance.group_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling GroupsApi->group_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Group. | 
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

# **group_index**
> GroupList group_index(x_api_version=x_api_version, archived=archived, created_since=created_since, fields=fields, ids=ids, limit=limit, name=name, order=order, page_token=page_token, query=query, type=type, updated_since=updated_since, user_id=user_id)

Return the data for all Groups

Outlines the parameters, optional and required, used when requesting the data for all Groups

### Example


```python
import openapi_client
from openapi_client.models.group_list import GroupList
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
    api_instance = openapi_client.GroupsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    archived = True # bool | Filter archived Group records. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Group records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Group records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Group records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    name = 'name_example' # str | Filter Group records to those that match the given name. (optional)
    order = 'order_example' # str | Orders the Group records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching a given string. (optional)
    type = 'type_example' # str | Filter Group records to those that match the given type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Group records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    user_id = 56 # int | The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the Group records with the matching property. (optional)

    try:
        # Return the data for all Groups
        api_response = api_instance.group_index(x_api_version=x_api_version, archived=archived, created_since=created_since, fields=fields, ids=ids, limit=limit, name=name, order=order, page_token=page_token, query=query, type=type, updated_since=updated_since, user_id=user_id)
        print("The response of GroupsApi->group_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->group_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **archived** | **bool**| Filter archived Group records. | [optional] 
 **created_since** | **datetime**| Filter Group records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Group records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Group records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **name** | **str**| Filter Group records to those that match the given name. | [optional] 
 **order** | **str**| Orders the Group records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching a given string. | [optional] 
 **type** | **str**| Filter Group records to those that match the given type. | [optional] 
 **updated_since** | **datetime**| Filter Group records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **user_id** | **int**| The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Group records with the matching property. | [optional] 

### Return type

[**GroupList**](GroupList.md)

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

# **group_show**
> GroupShow group_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Group

Outlines the parameters, optional and required, used when requesting the data for a single Group

### Example


```python
import openapi_client
from openapi_client.models.group_show import GroupShow
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
    api_instance = openapi_client.GroupsApi(api_client)
    id = 56 # int | The unique identifier for the Group.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Group
        api_response = api_instance.group_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of GroupsApi->group_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->group_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Group. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**GroupShow**](GroupShow.md)

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

# **group_update**
> GroupShow group_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, group_create_request=group_create_request)

Update a single Group

Outlines the parameters and data fields used when updating a single Group

### Example


```python
import openapi_client
from openapi_client.models.group_create_request import GroupCreateRequest
from openapi_client.models.group_show import GroupShow
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
    api_instance = openapi_client.GroupsApi(api_client)
    id = 56 # int | The unique identifier for the Group.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    group_create_request = openapi_client.GroupCreateRequest() # GroupCreateRequest | Request Body for Groups (optional)

    try:
        # Update a single Group
        api_response = api_instance.group_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, group_create_request=group_create_request)
        print("The response of GroupsApi->group_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->group_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Group. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **group_create_request** | [**GroupCreateRequest**](GroupCreateRequest.md)| Request Body for Groups | [optional] 

### Return type

[**GroupShow**](GroupShow.md)

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

