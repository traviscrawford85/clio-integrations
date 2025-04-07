# openapi_client.ClioPaymentsLinksApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clio_payments_link_create**](ClioPaymentsLinksApi.md#clio_payments_link_create) | **POST** /clio_payments/links.json | Create a new ClioPaymentsLink
[**clio_payments_link_index**](ClioPaymentsLinksApi.md#clio_payments_link_index) | **GET** /clio_payments/links.json | Return the data for all ClioPaymentsLinks
[**clio_payments_link_show**](ClioPaymentsLinksApi.md#clio_payments_link_show) | **GET** /clio_payments/links/{id}.json | Return the data for a single ClioPaymentsLink
[**clio_payments_link_update**](ClioPaymentsLinksApi.md#clio_payments_link_update) | **PATCH** /clio_payments/links/{id}.json | Update a single ClioPaymentsLink


# **clio_payments_link_create**
> ClioPaymentsLinkShow clio_payments_link_create(x_api_version=x_api_version, fields=fields, clio_payments_link_create_request=clio_payments_link_create_request)

Create a new ClioPaymentsLink

Outlines the parameters and data fields used when creating a new ClioPaymentsLink

### Example


```python
import openapi_client
from openapi_client.models.clio_payments_link_create_request import ClioPaymentsLinkCreateRequest
from openapi_client.models.clio_payments_link_show import ClioPaymentsLinkShow
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
    api_instance = openapi_client.ClioPaymentsLinksApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    clio_payments_link_create_request = openapi_client.ClioPaymentsLinkCreateRequest() # ClioPaymentsLinkCreateRequest | Request Body for Links (optional)

    try:
        # Create a new ClioPaymentsLink
        api_response = api_instance.clio_payments_link_create(x_api_version=x_api_version, fields=fields, clio_payments_link_create_request=clio_payments_link_create_request)
        print("The response of ClioPaymentsLinksApi->clio_payments_link_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClioPaymentsLinksApi->clio_payments_link_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **clio_payments_link_create_request** | [**ClioPaymentsLinkCreateRequest**](ClioPaymentsLinkCreateRequest.md)| Request Body for Links | [optional] 

### Return type

[**ClioPaymentsLinkShow**](ClioPaymentsLinkShow.md)

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

# **clio_payments_link_index**
> ClioPaymentsLinkList clio_payments_link_index(x_api_version=x_api_version, active=active, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)

Return the data for all ClioPaymentsLinks

Outlines the parameters, optional and required, used when requesting the data for all ClioPaymentsLinks

### Example


```python
import openapi_client
from openapi_client.models.clio_payments_link_list import ClioPaymentsLinkList
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
    api_instance = openapi_client.ClioPaymentsLinksApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    active = True # bool | Filter ClioPaymentsLink records based on whether or not they have expired. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ClioPaymentsLink records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter ClioPaymentsLink records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of ClioPaymentsLink records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ClioPaymentsLink records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all ClioPaymentsLinks
        api_response = api_instance.clio_payments_link_index(x_api_version=x_api_version, active=active, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)
        print("The response of ClioPaymentsLinksApi->clio_payments_link_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClioPaymentsLinksApi->clio_payments_link_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **active** | **bool**| Filter ClioPaymentsLink records based on whether or not they have expired. | [optional] 
 **created_since** | **datetime**| Filter ClioPaymentsLink records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter ClioPaymentsLink records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of ClioPaymentsLink records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter ClioPaymentsLink records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ClioPaymentsLinkList**](ClioPaymentsLinkList.md)

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

# **clio_payments_link_show**
> ClioPaymentsLinkShow clio_payments_link_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single ClioPaymentsLink

Outlines the parameters, optional and required, used when requesting the data for a single ClioPaymentsLink

### Example


```python
import openapi_client
from openapi_client.models.clio_payments_link_show import ClioPaymentsLinkShow
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
    api_instance = openapi_client.ClioPaymentsLinksApi(api_client)
    id = 56 # int | The unique identifier for the ClioPaymentsLink.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single ClioPaymentsLink
        api_response = api_instance.clio_payments_link_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ClioPaymentsLinksApi->clio_payments_link_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClioPaymentsLinksApi->clio_payments_link_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ClioPaymentsLink. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ClioPaymentsLinkShow**](ClioPaymentsLinkShow.md)

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

# **clio_payments_link_update**
> ClioPaymentsLinkShow clio_payments_link_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, clio_payments_link_update_request=clio_payments_link_update_request)

Update a single ClioPaymentsLink

Outlines the parameters and data fields used when updating a single ClioPaymentsLink

### Example


```python
import openapi_client
from openapi_client.models.clio_payments_link_show import ClioPaymentsLinkShow
from openapi_client.models.clio_payments_link_update_request import ClioPaymentsLinkUpdateRequest
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
    api_instance = openapi_client.ClioPaymentsLinksApi(api_client)
    id = 56 # int | The unique identifier for the ClioPaymentsLink.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    clio_payments_link_update_request = openapi_client.ClioPaymentsLinkUpdateRequest() # ClioPaymentsLinkUpdateRequest | Request Body for Links (optional)

    try:
        # Update a single ClioPaymentsLink
        api_response = api_instance.clio_payments_link_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, clio_payments_link_update_request=clio_payments_link_update_request)
        print("The response of ClioPaymentsLinksApi->clio_payments_link_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClioPaymentsLinksApi->clio_payments_link_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ClioPaymentsLink. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **clio_payments_link_update_request** | [**ClioPaymentsLinkUpdateRequest**](ClioPaymentsLinkUpdateRequest.md)| Request Body for Links | [optional] 

### Return type

[**ClioPaymentsLinkShow**](ClioPaymentsLinkShow.md)

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

