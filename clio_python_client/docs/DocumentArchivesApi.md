# openapi_client.DocumentArchivesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_archive_create**](DocumentArchivesApi.md#document_archive_create) | **POST** /document_archives.json | Create a new DocumentArchive
[**document_archive_download**](DocumentArchivesApi.md#document_archive_download) | **GET** /document_archives/{id}/download.json | Download the DocumentArchive
[**document_archive_show**](DocumentArchivesApi.md#document_archive_show) | **GET** /document_archives/{id}.json | Return the data for a single DocumentArchive


# **document_archive_create**
> DocumentArchiveShow document_archive_create(x_api_version=x_api_version, fields=fields, document_archive_create_request=document_archive_create_request)

Create a new DocumentArchive

Outlines the parameters and data fields used when creating a new DocumentArchive

### Example


```python
import openapi_client
from openapi_client.models.document_archive_create_request import DocumentArchiveCreateRequest
from openapi_client.models.document_archive_show import DocumentArchiveShow
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
    api_instance = openapi_client.DocumentArchivesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    document_archive_create_request = openapi_client.DocumentArchiveCreateRequest() # DocumentArchiveCreateRequest | Request Body for Document Archives (optional)

    try:
        # Create a new DocumentArchive
        api_response = api_instance.document_archive_create(x_api_version=x_api_version, fields=fields, document_archive_create_request=document_archive_create_request)
        print("The response of DocumentArchivesApi->document_archive_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentArchivesApi->document_archive_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **document_archive_create_request** | [**DocumentArchiveCreateRequest**](DocumentArchiveCreateRequest.md)| Request Body for Document Archives | [optional] 

### Return type

[**DocumentArchiveShow**](DocumentArchiveShow.md)

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

# **document_archive_download**
> document_archive_download(id)

Download the DocumentArchive

Download the DocumentArchive

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
    api_instance = openapi_client.DocumentArchivesApi(api_client)
    id = 56 # int | The unique identifier for the DocumentArchive.

    try:
        # Download the DocumentArchive
        api_instance.document_archive_download(id)
    except Exception as e:
        print("Exception when calling DocumentArchivesApi->document_archive_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the DocumentArchive. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_archive_show**
> DocumentArchiveShow document_archive_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single DocumentArchive

Outlines the parameters, optional and required, used when requesting the data for a single DocumentArchive

### Example


```python
import openapi_client
from openapi_client.models.document_archive_show import DocumentArchiveShow
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
    api_instance = openapi_client.DocumentArchivesApi(api_client)
    id = 56 # int | The unique identifier for the DocumentArchive.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single DocumentArchive
        api_response = api_instance.document_archive_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of DocumentArchivesApi->document_archive_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentArchivesApi->document_archive_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the DocumentArchive. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**DocumentArchiveShow**](DocumentArchiveShow.md)

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

