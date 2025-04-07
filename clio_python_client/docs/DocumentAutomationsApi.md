# openapi_client.DocumentAutomationsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_automation_create**](DocumentAutomationsApi.md#document_automation_create) | **POST** /document_automations.json | Create a new DocumentAutomation
[**document_automation_index**](DocumentAutomationsApi.md#document_automation_index) | **GET** /document_automations.json | Return the data for all DocumentAutomations
[**document_automation_show**](DocumentAutomationsApi.md#document_automation_show) | **GET** /document_automations/{id}.json | Return the data for a single DocumentAutomation


# **document_automation_create**
> DocumentAutomationShow document_automation_create(x_api_version=x_api_version, fields=fields, document_automation_create_request=document_automation_create_request)

Create a new DocumentAutomation

Outlines the parameters and data fields used when creating a new DocumentAutomation

### Example


```python
import openapi_client
from openapi_client.models.document_automation_create_request import DocumentAutomationCreateRequest
from openapi_client.models.document_automation_show import DocumentAutomationShow
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
    api_instance = openapi_client.DocumentAutomationsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    document_automation_create_request = openapi_client.DocumentAutomationCreateRequest() # DocumentAutomationCreateRequest | Request Body for Document Automations (optional)

    try:
        # Create a new DocumentAutomation
        api_response = api_instance.document_automation_create(x_api_version=x_api_version, fields=fields, document_automation_create_request=document_automation_create_request)
        print("The response of DocumentAutomationsApi->document_automation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAutomationsApi->document_automation_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **document_automation_create_request** | [**DocumentAutomationCreateRequest**](DocumentAutomationCreateRequest.md)| Request Body for Document Automations | [optional] 

### Return type

[**DocumentAutomationShow**](DocumentAutomationShow.md)

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

# **document_automation_index**
> DocumentAutomationList document_automation_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, updated_since=updated_since)

Return the data for all DocumentAutomations

Outlines the parameters, optional and required, used when requesting the data for all DocumentAutomations

### Example


```python
import openapi_client
from openapi_client.models.document_automation_list import DocumentAutomationList
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
    api_instance = openapi_client.DocumentAutomationsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter DocumentAutomation records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter DocumentAutomation records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of DocumentAutomation records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the DocumentAutomation records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter DocumentAutomation records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all DocumentAutomations
        api_response = api_instance.document_automation_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, updated_since=updated_since)
        print("The response of DocumentAutomationsApi->document_automation_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAutomationsApi->document_automation_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter DocumentAutomation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter DocumentAutomation records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of DocumentAutomation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the DocumentAutomation records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter DocumentAutomation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**DocumentAutomationList**](DocumentAutomationList.md)

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

# **document_automation_show**
> DocumentAutomationShow document_automation_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single DocumentAutomation

Outlines the parameters, optional and required, used when requesting the data for a single DocumentAutomation

### Example


```python
import openapi_client
from openapi_client.models.document_automation_show import DocumentAutomationShow
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
    api_instance = openapi_client.DocumentAutomationsApi(api_client)
    id = 56 # int | The unique identifier for the DocumentAutomation.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single DocumentAutomation
        api_response = api_instance.document_automation_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of DocumentAutomationsApi->document_automation_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAutomationsApi->document_automation_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the DocumentAutomation. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**DocumentAutomationShow**](DocumentAutomationShow.md)

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

