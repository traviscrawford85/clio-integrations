# openapi_client.PracticeAreasApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**practice_area_create**](PracticeAreasApi.md#practice_area_create) | **POST** /practice_areas.json | Create a new PracticeArea
[**practice_area_destroy**](PracticeAreasApi.md#practice_area_destroy) | **DELETE** /practice_areas/{id}.json | Delete a single PracticeArea
[**practice_area_index**](PracticeAreasApi.md#practice_area_index) | **GET** /practice_areas.json | Return the data for all PracticeAreas
[**practice_area_show**](PracticeAreasApi.md#practice_area_show) | **GET** /practice_areas/{id}.json | Return the data for a single PracticeArea
[**practice_area_update**](PracticeAreasApi.md#practice_area_update) | **PATCH** /practice_areas/{id}.json | Update a single PracticeArea


# **practice_area_create**
> PracticeAreaShow practice_area_create(x_api_version=x_api_version, fields=fields, practice_area_create_request=practice_area_create_request)

Create a new PracticeArea

Outlines the parameters and data fields used when creating a new PracticeArea

### Example


```python
import openapi_client
from openapi_client.models.practice_area_create_request import PracticeAreaCreateRequest
from openapi_client.models.practice_area_show import PracticeAreaShow
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
    api_instance = openapi_client.PracticeAreasApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    practice_area_create_request = openapi_client.PracticeAreaCreateRequest() # PracticeAreaCreateRequest | Request Body for Practice Areas (optional)

    try:
        # Create a new PracticeArea
        api_response = api_instance.practice_area_create(x_api_version=x_api_version, fields=fields, practice_area_create_request=practice_area_create_request)
        print("The response of PracticeAreasApi->practice_area_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PracticeAreasApi->practice_area_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **practice_area_create_request** | [**PracticeAreaCreateRequest**](PracticeAreaCreateRequest.md)| Request Body for Practice Areas | [optional] 

### Return type

[**PracticeAreaShow**](PracticeAreaShow.md)

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

# **practice_area_destroy**
> practice_area_destroy(id, x_api_version=x_api_version)

Delete a single PracticeArea

Outlines the parameters, optional and required, used when deleting the record for a single PracticeArea

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
    api_instance = openapi_client.PracticeAreasApi(api_client)
    id = 56 # int | The unique identifier for the PracticeArea.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single PracticeArea
        api_instance.practice_area_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling PracticeAreasApi->practice_area_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the PracticeArea. | 
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

# **practice_area_index**
> PracticeAreaList practice_area_index(x_api_version=x_api_version, code=code, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, name=name, order=order, page_token=page_token, updated_since=updated_since)

Return the data for all PracticeAreas

Outlines the parameters, optional and required, used when requesting the data for all PracticeAreas

### Example


```python
import openapi_client
from openapi_client.models.practice_area_list import PracticeAreaList
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
    api_instance = openapi_client.PracticeAreasApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    code = 'code_example' # str | Filter PracticeArea records to those that match the given code. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter PracticeArea records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter PracticeArea records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of PracticeArea records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | Filter PracticeArea records to exclude Legal Aid UK Practice Areas when activities exist on the matter. (optional)
    name = 'name_example' # str | Filter PracticeArea records to those that match the given name. (optional)
    order = 'order_example' # str | Orders the PracticeArea records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter PracticeArea records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all PracticeAreas
        api_response = api_instance.practice_area_index(x_api_version=x_api_version, code=code, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, name=name, order=order, page_token=page_token, updated_since=updated_since)
        print("The response of PracticeAreasApi->practice_area_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PracticeAreasApi->practice_area_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **code** | **str**| Filter PracticeArea records to those that match the given code. | [optional] 
 **created_since** | **datetime**| Filter PracticeArea records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter PracticeArea records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of PracticeArea records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| Filter PracticeArea records to exclude Legal Aid UK Practice Areas when activities exist on the matter. | [optional] 
 **name** | **str**| Filter PracticeArea records to those that match the given name. | [optional] 
 **order** | **str**| Orders the PracticeArea records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter PracticeArea records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**PracticeAreaList**](PracticeAreaList.md)

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

# **practice_area_show**
> PracticeAreaShow practice_area_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single PracticeArea

Outlines the parameters, optional and required, used when requesting the data for a single PracticeArea

### Example


```python
import openapi_client
from openapi_client.models.practice_area_show import PracticeAreaShow
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
    api_instance = openapi_client.PracticeAreasApi(api_client)
    id = 56 # int | The unique identifier for the PracticeArea.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single PracticeArea
        api_response = api_instance.practice_area_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of PracticeAreasApi->practice_area_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PracticeAreasApi->practice_area_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the PracticeArea. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**PracticeAreaShow**](PracticeAreaShow.md)

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

# **practice_area_update**
> PracticeAreaShow practice_area_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, practice_area_update_request=practice_area_update_request)

Update a single PracticeArea

Outlines the parameters and data fields used when updating a single PracticeArea

### Example


```python
import openapi_client
from openapi_client.models.practice_area_show import PracticeAreaShow
from openapi_client.models.practice_area_update_request import PracticeAreaUpdateRequest
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
    api_instance = openapi_client.PracticeAreasApi(api_client)
    id = 56 # int | The unique identifier for the PracticeArea.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    practice_area_update_request = openapi_client.PracticeAreaUpdateRequest() # PracticeAreaUpdateRequest | Request Body for Practice Areas (optional)

    try:
        # Update a single PracticeArea
        api_response = api_instance.practice_area_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, practice_area_update_request=practice_area_update_request)
        print("The response of PracticeAreasApi->practice_area_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PracticeAreasApi->practice_area_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the PracticeArea. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **practice_area_update_request** | [**PracticeAreaUpdateRequest**](PracticeAreaUpdateRequest.md)| Request Body for Practice Areas | [optional] 

### Return type

[**PracticeAreaShow**](PracticeAreaShow.md)

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

