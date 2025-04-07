# openapi_client.DocumentsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_copy**](DocumentsApi.md#document_copy) | **POST** /documents/{id}/copy.json | Copy a Document
[**document_create**](DocumentsApi.md#document_create) | **POST** /documents.json | Create a new Document
[**document_destroy**](DocumentsApi.md#document_destroy) | **DELETE** /documents/{id}.json | Delete a single Document
[**document_download**](DocumentsApi.md#document_download) | **GET** /documents/{id}/download.json | Download the Document
[**document_index**](DocumentsApi.md#document_index) | **GET** /documents.json | Return the data for all Documents
[**document_show**](DocumentsApi.md#document_show) | **GET** /documents/{id}.json | Return the data for a single Document
[**document_update**](DocumentsApi.md#document_update) | **PATCH** /documents/{id}.json | Update a single Document


# **document_copy**
> DocumentShow document_copy(id, fields=fields, document_copy_request=document_copy_request)

Copy a Document

Copies the latest document version of a Document into a new Document. The parameters `filename` and `name` will be copied from the source Document if none are provided. 

### Example


```python
import openapi_client
from openapi_client.models.document_copy_request import DocumentCopyRequest
from openapi_client.models.document_show import DocumentShow
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
    api_instance = openapi_client.DocumentsApi(api_client)
    id = 56 # int | The unique identifier for the Document.
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    document_copy_request = openapi_client.DocumentCopyRequest() # DocumentCopyRequest | Request Body for Documents (optional)

    try:
        # Copy a Document
        api_response = api_instance.document_copy(id, fields=fields, document_copy_request=document_copy_request)
        print("The response of DocumentsApi->document_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Document. | 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **document_copy_request** | [**DocumentCopyRequest**](DocumentCopyRequest.md)| Request Body for Documents | [optional] 

### Return type

[**DocumentShow**](DocumentShow.md)

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

# **document_create**
> DocumentShow document_create(x_api_version=x_api_version, fields=fields, document_create_request=document_create_request)

Create a new Document

Create a Document, or Create Document Version to an existing Document. 

### Example


```python
import openapi_client
from openapi_client.models.document_create_request import DocumentCreateRequest
from openapi_client.models.document_show import DocumentShow
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
    api_instance = openapi_client.DocumentsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    document_create_request = openapi_client.DocumentCreateRequest() # DocumentCreateRequest | Request Body for Documents (optional)

    try:
        # Create a new Document
        api_response = api_instance.document_create(x_api_version=x_api_version, fields=fields, document_create_request=document_create_request)
        print("The response of DocumentsApi->document_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **document_create_request** | [**DocumentCreateRequest**](DocumentCreateRequest.md)| Request Body for Documents | [optional] 

### Return type

[**DocumentShow**](DocumentShow.md)

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

# **document_destroy**
> document_destroy(id, x_api_version=x_api_version)

Delete a single Document

Deleting a Document using this method will move it to the trash instead of permanently deleting it. Trashed Documents are permanently deleted after 30 days. The following errors may be returned:  - `409 Conflict`: The Document (or one of its ancestor folders) is currently being modified by another request, and cannot be trashed. 

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
    api_instance = openapi_client.DocumentsApi(api_client)
    id = 56 # int | The unique identifier for the Document.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Document
        api_instance.document_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Document. | 
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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_download**
> document_download(id, document_version_id=document_version_id)

Download the Document

Download the Document

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
    api_instance = openapi_client.DocumentsApi(api_client)
    id = 56 # int | The unique identifier for the Document.
    document_version_id = 56 # int | The unique identifier for a DocumentVersion to be downloaded. Defaults to the latest. (optional)

    try:
        # Download the Document
        api_instance.document_download(id, document_version_id=document_version_id)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Document. | 
 **document_version_id** | **int**| The unique identifier for a DocumentVersion to be downloaded. Defaults to the latest. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | See Other |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_index**
> DocumentList document_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, document_category_id=document_category_id, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, ids=ids, include_deleted=include_deleted, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, query=query, scope=scope, show_uncompleted=show_uncompleted, updated_since=updated_since)

Return the data for all Documents

Outlines the parameters, optional and required, used when requesting the data for all Documents

### Example


```python
import openapi_client
from openapi_client.models.document_list import DocumentList
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
    api_instance = openapi_client.DocumentsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Document records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    document_category_id = 56 # int | The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property. (optional)
    external_property_name = 'external_property_name_example' # str | Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name`  (optional)
    external_property_value = 'external_property_value_example' # str | Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value`  (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Document records to those having the specified unique identifiers. (optional)
    include_deleted = True # bool | Allow trashed Document record to be included. (optional)
    limit = 56 # int | A limit on the number of Document records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property. (optional)
    order = 'order_example' # str | Orders the Document records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    parent_id = 56 # int | The unique identifier for a single Folder. Use the keyword `null` to match those without a Document. The list will be filtered to include only the Document records with the matching property. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching the given string. (optional)
    scope = 'scope_example' # str | Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`. (optional)
    show_uncompleted = True # bool | Allow Document record being uploaded to be included. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Document records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Documents
        api_response = api_instance.document_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, document_category_id=document_category_id, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, ids=ids, include_deleted=include_deleted, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, query=query, scope=scope, show_uncompleted=show_uncompleted, updated_since=updated_since)
        print("The response of DocumentsApi->document_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Document records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **document_category_id** | **int**| The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property. | [optional] 
 **external_property_name** | **str**| Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60;  | [optional] 
 **external_property_value** | **str**| Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60;  | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Document records to those having the specified unique identifiers. | [optional] 
 **include_deleted** | **bool**| Allow trashed Document record to be included. | [optional] 
 **limit** | **int**| A limit on the number of Document records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property. | [optional] 
 **order** | **str**| Orders the Document records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **parent_id** | **int**| The unique identifier for a single Folder. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching the given string. | [optional] 
 **scope** | **str**| Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;. | [optional] 
 **show_uncompleted** | **bool**| Allow Document record being uploaded to be included. | [optional] 
 **updated_since** | **datetime**| Filter Document records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

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

# **document_show**
> DocumentShow document_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Document

Outlines the parameters, optional and required, used when requesting the data for a single Document

### Example


```python
import openapi_client
from openapi_client.models.document_show import DocumentShow
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
    api_instance = openapi_client.DocumentsApi(api_client)
    id = 56 # int | The unique identifier for the Document.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Document
        api_response = api_instance.document_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of DocumentsApi->document_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Document. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**DocumentShow**](DocumentShow.md)

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

# **document_update**
> DocumentShow document_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, document_update_request=document_update_request)

Update a single Document

Update Document, move Document to another Folder, and/or restore a trashed Document. 

### Example


```python
import openapi_client
from openapi_client.models.document_show import DocumentShow
from openapi_client.models.document_update_request import DocumentUpdateRequest
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
    api_instance = openapi_client.DocumentsApi(api_client)
    id = 56 # int | The unique identifier for the Document.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    document_update_request = openapi_client.DocumentUpdateRequest() # DocumentUpdateRequest | Request Body for Documents (optional)

    try:
        # Update a single Document
        api_response = api_instance.document_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, document_update_request=document_update_request)
        print("The response of DocumentsApi->document_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Document. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **document_update_request** | [**DocumentUpdateRequest**](DocumentUpdateRequest.md)| Request Body for Documents | [optional] 

### Return type

[**DocumentShow**](DocumentShow.md)

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

