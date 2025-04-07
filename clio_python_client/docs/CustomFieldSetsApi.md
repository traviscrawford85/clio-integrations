# openapi_client.CustomFieldSetsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_field_set_create**](CustomFieldSetsApi.md#custom_field_set_create) | **POST** /custom_field_sets.json | Create a new CustomFieldSet
[**custom_field_set_destroy**](CustomFieldSetsApi.md#custom_field_set_destroy) | **DELETE** /custom_field_sets/{id}.json | Delete a single CustomFieldSet
[**custom_field_set_index**](CustomFieldSetsApi.md#custom_field_set_index) | **GET** /custom_field_sets.json | Return the data for all CustomFieldSets
[**custom_field_set_show**](CustomFieldSetsApi.md#custom_field_set_show) | **GET** /custom_field_sets/{id}.json | Return the data for a single CustomFieldSet
[**custom_field_set_update**](CustomFieldSetsApi.md#custom_field_set_update) | **PATCH** /custom_field_sets/{id}.json | Update a single CustomFieldSet


# **custom_field_set_create**
> CustomFieldSetShow custom_field_set_create(x_api_version=x_api_version, fields=fields, custom_field_set_create_request=custom_field_set_create_request)

Create a new CustomFieldSet

Outlines the parameters and data fields used when creating a new CustomFieldSet

### Example


```python
import openapi_client
from openapi_client.models.custom_field_set_create_request import CustomFieldSetCreateRequest
from openapi_client.models.custom_field_set_show import CustomFieldSetShow
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
    api_instance = openapi_client.CustomFieldSetsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    custom_field_set_create_request = openapi_client.CustomFieldSetCreateRequest() # CustomFieldSetCreateRequest | Request Body for Custom Field Sets (optional)

    try:
        # Create a new CustomFieldSet
        api_response = api_instance.custom_field_set_create(x_api_version=x_api_version, fields=fields, custom_field_set_create_request=custom_field_set_create_request)
        print("The response of CustomFieldSetsApi->custom_field_set_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSetsApi->custom_field_set_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **custom_field_set_create_request** | [**CustomFieldSetCreateRequest**](CustomFieldSetCreateRequest.md)| Request Body for Custom Field Sets | [optional] 

### Return type

[**CustomFieldSetShow**](CustomFieldSetShow.md)

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

# **custom_field_set_destroy**
> custom_field_set_destroy(id, x_api_version=x_api_version)

Delete a single CustomFieldSet

Outlines the parameters, optional and required, used when deleting the record for a single CustomFieldSet

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
    api_instance = openapi_client.CustomFieldSetsApi(api_client)
    id = 56 # int | The unique identifier for the CustomFieldSet.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single CustomFieldSet
        api_instance.custom_field_set_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CustomFieldSetsApi->custom_field_set_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CustomFieldSet. | 
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

# **custom_field_set_index**
> CustomFieldSetList custom_field_set_index(x_api_version=x_api_version, created_since=created_since, displayed=displayed, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, parent_type=parent_type, query=query, updated_since=updated_since)

Return the data for all CustomFieldSets

Outlines the parameters, optional and required, used when requesting the data for all CustomFieldSets

### Example


```python
import openapi_client
from openapi_client.models.custom_field_set_list import CustomFieldSetList
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
    api_instance = openapi_client.CustomFieldSetsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter CustomFieldSet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    displayed = True # bool | Filter CustomFieldSet records to those that should be displayed by default. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter CustomFieldSet records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of CustomFieldSet records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the CustomFieldSet records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    parent_type = 'parent_type_example' # str | Filter CustomFieldSet records to those that have the specified `parent_type`. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter CustomFieldSet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all CustomFieldSets
        api_response = api_instance.custom_field_set_index(x_api_version=x_api_version, created_since=created_since, displayed=displayed, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, parent_type=parent_type, query=query, updated_since=updated_since)
        print("The response of CustomFieldSetsApi->custom_field_set_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSetsApi->custom_field_set_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter CustomFieldSet records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **displayed** | **bool**| Filter CustomFieldSet records to those that should be displayed by default. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter CustomFieldSet records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of CustomFieldSet records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the CustomFieldSet records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **parent_type** | **str**| Filter CustomFieldSet records to those that have the specified &#x60;parent_type&#x60;. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter CustomFieldSet records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**CustomFieldSetList**](CustomFieldSetList.md)

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

# **custom_field_set_show**
> CustomFieldSetShow custom_field_set_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single CustomFieldSet

Outlines the parameters, optional and required, used when requesting the data for a single CustomFieldSet

### Example


```python
import openapi_client
from openapi_client.models.custom_field_set_show import CustomFieldSetShow
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
    api_instance = openapi_client.CustomFieldSetsApi(api_client)
    id = 56 # int | The unique identifier for the CustomFieldSet.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single CustomFieldSet
        api_response = api_instance.custom_field_set_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of CustomFieldSetsApi->custom_field_set_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSetsApi->custom_field_set_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CustomFieldSet. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**CustomFieldSetShow**](CustomFieldSetShow.md)

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

# **custom_field_set_update**
> CustomFieldSetShow custom_field_set_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, custom_field_set_update_request=custom_field_set_update_request)

Update a single CustomFieldSet

Outlines the parameters and data fields used when updating a single CustomFieldSet

### Example


```python
import openapi_client
from openapi_client.models.custom_field_set_show import CustomFieldSetShow
from openapi_client.models.custom_field_set_update_request import CustomFieldSetUpdateRequest
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
    api_instance = openapi_client.CustomFieldSetsApi(api_client)
    id = 56 # int | The unique identifier for the CustomFieldSet.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    custom_field_set_update_request = openapi_client.CustomFieldSetUpdateRequest() # CustomFieldSetUpdateRequest | Request Body for Custom Field Sets (optional)

    try:
        # Update a single CustomFieldSet
        api_response = api_instance.custom_field_set_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, custom_field_set_update_request=custom_field_set_update_request)
        print("The response of CustomFieldSetsApi->custom_field_set_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSetsApi->custom_field_set_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CustomFieldSet. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **custom_field_set_update_request** | [**CustomFieldSetUpdateRequest**](CustomFieldSetUpdateRequest.md)| Request Body for Custom Field Sets | [optional] 

### Return type

[**CustomFieldSetShow**](CustomFieldSetShow.md)

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

