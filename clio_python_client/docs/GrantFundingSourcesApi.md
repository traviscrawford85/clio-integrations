# openapi_client.GrantFundingSourcesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grant_funding_source_create**](GrantFundingSourcesApi.md#grant_funding_source_create) | **POST** /grant_funding_sources.json | Create a new grant funding source
[**grant_funding_source_destroy**](GrantFundingSourcesApi.md#grant_funding_source_destroy) | **DELETE** /grant_funding_sources/{id}.json | Delete a single grant funding source
[**grant_funding_source_index**](GrantFundingSourcesApi.md#grant_funding_source_index) | **GET** /grant_funding_sources.json | Return the data for all grant funding sources
[**grant_funding_source_update**](GrantFundingSourcesApi.md#grant_funding_source_update) | **PATCH** /grant_funding_sources/{id}.json | Update a single grant funding source


# **grant_funding_source_create**
> GrantFundingSourceShow grant_funding_source_create(x_api_version=x_api_version, fields=fields, grant_funding_source_create_request=grant_funding_source_create_request)

Create a new grant funding source

Outlines the parameters and data fields used when creating a new GrantFundingSource

### Example


```python
import openapi_client
from openapi_client.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest
from openapi_client.models.grant_funding_source_show import GrantFundingSourceShow
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
    api_instance = openapi_client.GrantFundingSourcesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    grant_funding_source_create_request = openapi_client.GrantFundingSourceCreateRequest() # GrantFundingSourceCreateRequest | Request Body for Grant Funding Sources (optional)

    try:
        # Create a new grant funding source
        api_response = api_instance.grant_funding_source_create(x_api_version=x_api_version, fields=fields, grant_funding_source_create_request=grant_funding_source_create_request)
        print("The response of GrantFundingSourcesApi->grant_funding_source_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantFundingSourcesApi->grant_funding_source_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **grant_funding_source_create_request** | [**GrantFundingSourceCreateRequest**](GrantFundingSourceCreateRequest.md)| Request Body for Grant Funding Sources | [optional] 

### Return type

[**GrantFundingSourceShow**](GrantFundingSourceShow.md)

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

# **grant_funding_source_destroy**
> GrantFundingSourceShow grant_funding_source_destroy(id, if_match=if_match, x_api_version=x_api_version, fields=fields, grant_funding_source_create_request=grant_funding_source_create_request)

Delete a single grant funding source

Outlines the parameters and data fields used when updating a single GrantFundingSource

### Example


```python
import openapi_client
from openapi_client.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest
from openapi_client.models.grant_funding_source_show import GrantFundingSourceShow
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
    api_instance = openapi_client.GrantFundingSourcesApi(api_client)
    id = 56 # int | The unique identifier for the GrantFundingSource.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    grant_funding_source_create_request = openapi_client.GrantFundingSourceCreateRequest() # GrantFundingSourceCreateRequest | Request Body for Grant Funding Sources (optional)

    try:
        # Delete a single grant funding source
        api_response = api_instance.grant_funding_source_destroy(id, if_match=if_match, x_api_version=x_api_version, fields=fields, grant_funding_source_create_request=grant_funding_source_create_request)
        print("The response of GrantFundingSourcesApi->grant_funding_source_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantFundingSourcesApi->grant_funding_source_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the GrantFundingSource. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **grant_funding_source_create_request** | [**GrantFundingSourceCreateRequest**](GrantFundingSourceCreateRequest.md)| Request Body for Grant Funding Sources | [optional] 

### Return type

[**GrantFundingSourceShow**](GrantFundingSourceShow.md)

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

# **grant_funding_source_index**
> GrantFundingSourceList grant_funding_source_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, name=name, page_token=page_token, updated_since=updated_since)

Return the data for all grant funding sources

Outlines the parameters, optional and required, used when requesting the data for all GrantFundingSources

### Example


```python
import openapi_client
from openapi_client.models.grant_funding_source_list import GrantFundingSourceList
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
    api_instance = openapi_client.GrantFundingSourcesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter GrantFundingSource records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter GrantFundingSource records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of GrantFundingSource records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    name = 'name_example' # str | Filter GrantFundingSource records to those that match the given name. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter GrantFundingSource records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all grant funding sources
        api_response = api_instance.grant_funding_source_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, name=name, page_token=page_token, updated_since=updated_since)
        print("The response of GrantFundingSourcesApi->grant_funding_source_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantFundingSourcesApi->grant_funding_source_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter GrantFundingSource records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter GrantFundingSource records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of GrantFundingSource records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **name** | **str**| Filter GrantFundingSource records to those that match the given name. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter GrantFundingSource records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**GrantFundingSourceList**](GrantFundingSourceList.md)

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

# **grant_funding_source_update**
> GrantFundingSourceShow grant_funding_source_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, grant_funding_source_create_request=grant_funding_source_create_request)

Update a single grant funding source

Outlines the parameters and data fields used when updating a single GrantFundingSource

### Example


```python
import openapi_client
from openapi_client.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest
from openapi_client.models.grant_funding_source_show import GrantFundingSourceShow
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
    api_instance = openapi_client.GrantFundingSourcesApi(api_client)
    id = 56 # int | The unique identifier for the GrantFundingSource.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    grant_funding_source_create_request = openapi_client.GrantFundingSourceCreateRequest() # GrantFundingSourceCreateRequest | Request Body for Grant Funding Sources (optional)

    try:
        # Update a single grant funding source
        api_response = api_instance.grant_funding_source_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, grant_funding_source_create_request=grant_funding_source_create_request)
        print("The response of GrantFundingSourcesApi->grant_funding_source_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantFundingSourcesApi->grant_funding_source_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the GrantFundingSource. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **grant_funding_source_create_request** | [**GrantFundingSourceCreateRequest**](GrantFundingSourceCreateRequest.md)| Request Body for Grant Funding Sources | [optional] 

### Return type

[**GrantFundingSourceShow**](GrantFundingSourceShow.md)

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

