# openapi_client.UsersApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_index**](UsersApi.md#user_index) | **GET** /users.json | Return the data for all Users
[**user_show**](UsersApi.md#user_show) | **GET** /users/{id}.json | Return the data for a single User
[**user_who_am_i**](UsersApi.md#user_who_am_i) | **GET** /users/who_am_i.json | Return the data for the current User


# **user_index**
> UserList user_index(x_api_version=x_api_version, created_since=created_since, enabled=enabled, fields=fields, ids=ids, include_co_counsel=include_co_counsel, limit=limit, name=name, order=order, page_token=page_token, pending_setup=pending_setup, role=role, subscription_type=subscription_type, updated_since=updated_since)

Return the data for all Users

Outlines the parameters, optional and required, used when requesting the data for all Users

### Example


```python
import openapi_client
from openapi_client.models.user_list import UserList
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
    api_instance = openapi_client.UsersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter User records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    enabled = True # bool | Filter User records to those that are enabled or disabled. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter User records to those having the specified unique identifiers. (optional)
    include_co_counsel = True # bool | Filter User to include co-counsel users (optional)
    limit = 56 # int | A limit on the number of User records to be returned. Limit can range between 1 and 2000. Default: `2000`. (optional)
    name = 'name_example' # str | Filter User records to those with the given name. (optional)
    order = 'order_example' # str | Orders the User records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    pending_setup = True # bool | Filter User records based on whether or not they are still being setup. (optional)
    role = 'role_example' # str | Filter User records to those with a specific role. (optional)
    subscription_type = 'subscription_type_example' # str | Filter User records to those with a specific subscription type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter User records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Users
        api_response = api_instance.user_index(x_api_version=x_api_version, created_since=created_since, enabled=enabled, fields=fields, ids=ids, include_co_counsel=include_co_counsel, limit=limit, name=name, order=order, page_token=page_token, pending_setup=pending_setup, role=role, subscription_type=subscription_type, updated_since=updated_since)
        print("The response of UsersApi->user_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter User records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **enabled** | **bool**| Filter User records to those that are enabled or disabled. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter User records to those having the specified unique identifiers. | [optional] 
 **include_co_counsel** | **bool**| Filter User to include co-counsel users | [optional] 
 **limit** | **int**| A limit on the number of User records to be returned. Limit can range between 1 and 2000. Default: &#x60;2000&#x60;. | [optional] 
 **name** | **str**| Filter User records to those with the given name. | [optional] 
 **order** | **str**| Orders the User records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **pending_setup** | **bool**| Filter User records based on whether or not they are still being setup. | [optional] 
 **role** | **str**| Filter User records to those with a specific role. | [optional] 
 **subscription_type** | **str**| Filter User records to those with a specific subscription type. | [optional] 
 **updated_since** | **datetime**| Filter User records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**UserList**](UserList.md)

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

# **user_show**
> UserShow user_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single User

Outlines the parameters, optional and required, used when requesting the data for a single User

### Example


```python
import openapi_client
from openapi_client.models.user_show import UserShow
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
    api_instance = openapi_client.UsersApi(api_client)
    id = 56 # int | The unique identifier for the User.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single User
        api_response = api_instance.user_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of UsersApi->user_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the User. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**UserShow**](UserShow.md)

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

# **user_who_am_i**
> UserShow user_who_am_i(if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for the current User

Outlines the parameters, optional and required, used when requesting the data for a single User

### Example


```python
import openapi_client
from openapi_client.models.user_show import UserShow
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
    api_instance = openapi_client.UsersApi(api_client)
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for the current User
        api_response = api_instance.user_who_am_i(if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of UsersApi->user_who_am_i:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_who_am_i: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**UserShow**](UserShow.md)

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

