# openapi_client.DocumentCategoriesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_category_create**](DocumentCategoriesApi.md#document_category_create) | **POST** /document_categories.json | Create a new DocumentCategory
[**document_category_destroy**](DocumentCategoriesApi.md#document_category_destroy) | **DELETE** /document_categories/{id}.json | Delete a single DocumentCategory
[**document_category_index**](DocumentCategoriesApi.md#document_category_index) | **GET** /document_categories.json | Return the data for all DocumentCategories
[**document_category_show**](DocumentCategoriesApi.md#document_category_show) | **GET** /document_categories/{id}.json | Return the data for a single DocumentCategory
[**document_category_update**](DocumentCategoriesApi.md#document_category_update) | **PATCH** /document_categories/{id}.json | Update a single DocumentCategory


# **document_category_create**
> DocumentCategoryShow document_category_create(x_api_version=x_api_version, fields=fields, document_category_create_request=document_category_create_request)

Create a new DocumentCategory

Outlines the parameters and data fields used when creating a new DocumentCategory

### Example


```python
import openapi_client
from openapi_client.models.document_category_create_request import DocumentCategoryCreateRequest
from openapi_client.models.document_category_show import DocumentCategoryShow
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
    api_instance = openapi_client.DocumentCategoriesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    document_category_create_request = openapi_client.DocumentCategoryCreateRequest() # DocumentCategoryCreateRequest | Request Body for Document Categories (optional)

    try:
        # Create a new DocumentCategory
        api_response = api_instance.document_category_create(x_api_version=x_api_version, fields=fields, document_category_create_request=document_category_create_request)
        print("The response of DocumentCategoriesApi->document_category_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoriesApi->document_category_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **document_category_create_request** | [**DocumentCategoryCreateRequest**](DocumentCategoryCreateRequest.md)| Request Body for Document Categories | [optional] 

### Return type

[**DocumentCategoryShow**](DocumentCategoryShow.md)

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

# **document_category_destroy**
> document_category_destroy(id, x_api_version=x_api_version)

Delete a single DocumentCategory

Outlines the parameters, optional and required, used when deleting the record for a single DocumentCategory

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
    api_instance = openapi_client.DocumentCategoriesApi(api_client)
    id = 56 # int | The unique identifier for the DocumentCategory.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single DocumentCategory
        api_instance.document_category_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling DocumentCategoriesApi->document_category_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the DocumentCategory. | 
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

# **document_category_index**
> DocumentCategoryList document_category_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)

Return the data for all DocumentCategories

Outlines the parameters, optional and required, used when requesting the data for all DocumentCategories

### Example


```python
import openapi_client
from openapi_client.models.document_category_list import DocumentCategoryList
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
    api_instance = openapi_client.DocumentCategoriesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter DocumentCategory records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter DocumentCategory records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of DocumentCategory records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the DocumentCategory records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter DocumentCategory records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all DocumentCategories
        api_response = api_instance.document_category_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of DocumentCategoriesApi->document_category_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoriesApi->document_category_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter DocumentCategory records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter DocumentCategory records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of DocumentCategory records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the DocumentCategory records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter DocumentCategory records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**DocumentCategoryList**](DocumentCategoryList.md)

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

# **document_category_show**
> DocumentCategoryShow document_category_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single DocumentCategory

Outlines the parameters, optional and required, used when requesting the data for a single DocumentCategory

### Example


```python
import openapi_client
from openapi_client.models.document_category_show import DocumentCategoryShow
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
    api_instance = openapi_client.DocumentCategoriesApi(api_client)
    id = 56 # int | The unique identifier for the DocumentCategory.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single DocumentCategory
        api_response = api_instance.document_category_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of DocumentCategoriesApi->document_category_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoriesApi->document_category_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the DocumentCategory. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**DocumentCategoryShow**](DocumentCategoryShow.md)

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

# **document_category_update**
> DocumentCategoryShow document_category_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, document_category_update_request=document_category_update_request)

Update a single DocumentCategory

Outlines the parameters and data fields used when updating a single DocumentCategory

### Example


```python
import openapi_client
from openapi_client.models.document_category_show import DocumentCategoryShow
from openapi_client.models.document_category_update_request import DocumentCategoryUpdateRequest
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
    api_instance = openapi_client.DocumentCategoriesApi(api_client)
    id = 56 # int | The unique identifier for the DocumentCategory.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    document_category_update_request = openapi_client.DocumentCategoryUpdateRequest() # DocumentCategoryUpdateRequest | Request Body for Document Categories (optional)

    try:
        # Update a single DocumentCategory
        api_response = api_instance.document_category_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, document_category_update_request=document_category_update_request)
        print("The response of DocumentCategoriesApi->document_category_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoriesApi->document_category_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the DocumentCategory. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **document_category_update_request** | [**DocumentCategoryUpdateRequest**](DocumentCategoryUpdateRequest.md)| Request Body for Document Categories | [optional] 

### Return type

[**DocumentCategoryShow**](DocumentCategoryShow.md)

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

