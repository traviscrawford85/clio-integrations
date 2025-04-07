# openapi_client.NotesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**note_create**](NotesApi.md#note_create) | **POST** /notes.json | Create a new Note
[**note_destroy**](NotesApi.md#note_destroy) | **DELETE** /notes/{id}.json | Delete a single Note
[**note_index**](NotesApi.md#note_index) | **GET** /notes.json | Return the data for all Notes
[**note_show**](NotesApi.md#note_show) | **GET** /notes/{id}.json | Return the data for a single Note
[**note_update**](NotesApi.md#note_update) | **PATCH** /notes/{id}.json | Update a single Note


# **note_create**
> NoteShow note_create(x_api_version=x_api_version, fields=fields, note_create_request=note_create_request)

Create a new Note

Outlines the parameters and data fields used when creating a new Note

### Example


```python
import openapi_client
from openapi_client.models.note_create_request import NoteCreateRequest
from openapi_client.models.note_show import NoteShow
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
    api_instance = openapi_client.NotesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    note_create_request = openapi_client.NoteCreateRequest() # NoteCreateRequest | Request Body for Notes (optional)

    try:
        # Create a new Note
        api_response = api_instance.note_create(x_api_version=x_api_version, fields=fields, note_create_request=note_create_request)
        print("The response of NotesApi->note_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->note_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **note_create_request** | [**NoteCreateRequest**](NoteCreateRequest.md)| Request Body for Notes | [optional] 

### Return type

[**NoteShow**](NoteShow.md)

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

# **note_destroy**
> note_destroy(id, x_api_version=x_api_version)

Delete a single Note

Outlines the parameters, optional and required, used when deleting the record for a single Note

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
    api_instance = openapi_client.NotesApi(api_client)
    id = 56 # int | The unique identifier for the Note.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Note
        api_instance.note_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling NotesApi->note_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Note. | 
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

# **note_index**
> NoteList note_index(type, x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, fields=fields, has_time_entries=has_time_entries, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, query=query, updated_since=updated_since)

Return the data for all Notes

Outlines the parameters, optional and required, used when requesting the data for all Notes

### Example


```python
import openapi_client
from openapi_client.models.note_list import NoteList
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
    api_instance = openapi_client.NotesApi(api_client)
    type = 'type_example' # str | Filter Note records to those of the specified type.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Note records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Note records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    has_time_entries = True # bool | Filter Note records to those with or without associated time entries. (optional)
    ids = 56 # int | Filter Note records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Note records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the Note records with the matching property. (optional)
    order = 'order_example' # str | Orders the Note records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search across note subject and detail. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Note records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Notes
        api_response = api_instance.note_index(type, x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, fields=fields, has_time_entries=has_time_entries, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of NotesApi->note_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->note_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter Note records to those of the specified type. | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Note records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Note records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **has_time_entries** | **bool**| Filter Note records to those with or without associated time entries. | [optional] 
 **ids** | **int**| Filter Note records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Note records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Note records with the matching property. | [optional] 
 **order** | **str**| Orders the Note records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search across note subject and detail. | [optional] 
 **updated_since** | **datetime**| Filter Note records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**NoteList**](NoteList.md)

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

# **note_show**
> NoteShow note_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Note

Outlines the parameters, optional and required, used when requesting the data for a single Note

### Example


```python
import openapi_client
from openapi_client.models.note_show import NoteShow
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
    api_instance = openapi_client.NotesApi(api_client)
    id = 56 # int | The unique identifier for the Note.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Note
        api_response = api_instance.note_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of NotesApi->note_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->note_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Note. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**NoteShow**](NoteShow.md)

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

# **note_update**
> NoteShow note_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, note_update_request=note_update_request)

Update a single Note

Outlines the parameters and data fields used when updating a single Note

### Example


```python
import openapi_client
from openapi_client.models.note_show import NoteShow
from openapi_client.models.note_update_request import NoteUpdateRequest
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
    api_instance = openapi_client.NotesApi(api_client)
    id = 56 # int | The unique identifier for the Note.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    note_update_request = openapi_client.NoteUpdateRequest() # NoteUpdateRequest | Request Body for Notes (optional)

    try:
        # Update a single Note
        api_response = api_instance.note_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, note_update_request=note_update_request)
        print("The response of NotesApi->note_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->note_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Note. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **note_update_request** | [**NoteUpdateRequest**](NoteUpdateRequest.md)| Request Body for Notes | [optional] 

### Return type

[**NoteShow**](NoteShow.md)

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

