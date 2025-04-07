# openapi_client.TextSnippetsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_snippet_create**](TextSnippetsApi.md#text_snippet_create) | **POST** /settings/text_snippets.json | Create a text snippet
[**text_snippet_destroy**](TextSnippetsApi.md#text_snippet_destroy) | **DELETE** /settings/text_snippets/{id}.json | Destroy a text snippet
[**text_snippet_index**](TextSnippetsApi.md#text_snippet_index) | **GET** /settings/text_snippets.json | Return all text snippets
[**text_snippet_show**](TextSnippetsApi.md#text_snippet_show) | **GET** /settings/text_snippets/{id}.json | Return the data for the text snippet
[**text_snippet_update**](TextSnippetsApi.md#text_snippet_update) | **PATCH** /settings/text_snippets/{id}.json | Update a text snippet


# **text_snippet_create**
> TextSnippetShow text_snippet_create(x_api_version=x_api_version, fields=fields, text_snippet_create_request=text_snippet_create_request)

Create a text snippet

Outlines the parameters and data fields used when creating a new TextSnippet

### Example


```python
import openapi_client
from openapi_client.models.text_snippet_create_request import TextSnippetCreateRequest
from openapi_client.models.text_snippet_show import TextSnippetShow
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
    api_instance = openapi_client.TextSnippetsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    text_snippet_create_request = openapi_client.TextSnippetCreateRequest() # TextSnippetCreateRequest | Request Body for Text Snippets (optional)

    try:
        # Create a text snippet
        api_response = api_instance.text_snippet_create(x_api_version=x_api_version, fields=fields, text_snippet_create_request=text_snippet_create_request)
        print("The response of TextSnippetsApi->text_snippet_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextSnippetsApi->text_snippet_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **text_snippet_create_request** | [**TextSnippetCreateRequest**](TextSnippetCreateRequest.md)| Request Body for Text Snippets | [optional] 

### Return type

[**TextSnippetShow**](TextSnippetShow.md)

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

# **text_snippet_destroy**
> text_snippet_destroy(id, x_api_version=x_api_version)

Destroy a text snippet

Outlines the parameters, optional and required, used when deleting the record for a single TextSnippet

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
    api_instance = openapi_client.TextSnippetsApi(api_client)
    id = 56 # int | The unique identifier for the TextSnippet.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Destroy a text snippet
        api_instance.text_snippet_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling TextSnippetsApi->text_snippet_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TextSnippet. | 
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

# **text_snippet_index**
> TextSnippetList text_snippet_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)

Return all text snippets

Outlines the parameters, optional and required, used when requesting the data for all TextSnippets

### Example


```python
import openapi_client
from openapi_client.models.text_snippet_list import TextSnippetList
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
    api_instance = openapi_client.TextSnippetsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TextSnippet records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter TextSnippet records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of TextSnippet records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the TextSnippet records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `snippet` or `phrase` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TextSnippet records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return all text snippets
        api_response = api_instance.text_snippet_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of TextSnippetsApi->text_snippet_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextSnippetsApi->text_snippet_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter TextSnippet records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter TextSnippet records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of TextSnippet records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the TextSnippet records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;snippet&#x60; or &#x60;phrase&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter TextSnippet records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**TextSnippetList**](TextSnippetList.md)

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

# **text_snippet_show**
> TextSnippetShow text_snippet_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for the text snippet

Outlines the parameters, optional and required, used when requesting the data for a single TextSnippet

### Example


```python
import openapi_client
from openapi_client.models.text_snippet_show import TextSnippetShow
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
    api_instance = openapi_client.TextSnippetsApi(api_client)
    id = 56 # int | The unique identifier for the TextSnippet.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for the text snippet
        api_response = api_instance.text_snippet_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of TextSnippetsApi->text_snippet_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextSnippetsApi->text_snippet_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TextSnippet. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**TextSnippetShow**](TextSnippetShow.md)

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

# **text_snippet_update**
> TextSnippetShow text_snippet_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, text_snippet_update_request=text_snippet_update_request)

Update a text snippet

Outlines the parameters and data fields used when updating a single TextSnippet

### Example


```python
import openapi_client
from openapi_client.models.text_snippet_show import TextSnippetShow
from openapi_client.models.text_snippet_update_request import TextSnippetUpdateRequest
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
    api_instance = openapi_client.TextSnippetsApi(api_client)
    id = 56 # int | The unique identifier for the TextSnippet.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    text_snippet_update_request = openapi_client.TextSnippetUpdateRequest() # TextSnippetUpdateRequest | Request Body for Text Snippets (optional)

    try:
        # Update a text snippet
        api_response = api_instance.text_snippet_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, text_snippet_update_request=text_snippet_update_request)
        print("The response of TextSnippetsApi->text_snippet_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextSnippetsApi->text_snippet_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TextSnippet. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **text_snippet_update_request** | [**TextSnippetUpdateRequest**](TextSnippetUpdateRequest.md)| Request Body for Text Snippets | [optional] 

### Return type

[**TextSnippetShow**](TextSnippetShow.md)

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

