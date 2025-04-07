# openapi_client.MatterDocketsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matter_docket_create**](MatterDocketsApi.md#matter_docket_create) | **POST** /court_rules/matter_dockets.json | Creates a matter docket
[**matter_docket_destroy**](MatterDocketsApi.md#matter_docket_destroy) | **DELETE** /court_rules/matter_dockets/{id}.json | Deletes the requested matter docket
[**matter_docket_index**](MatterDocketsApi.md#matter_docket_index) | **GET** /court_rules/matter_dockets.json | Return the data for all matter dockets
[**matter_docket_preview**](MatterDocketsApi.md#matter_docket_preview) | **GET** /court_rules/matter_dockets/preview.json | Preview calendar dates for the docket
[**matter_docket_show**](MatterDocketsApi.md#matter_docket_show) | **GET** /court_rules/matter_dockets/{id}.json | Return the data for the matter docket


# **matter_docket_create**
> MatterDocketShow matter_docket_create(x_api_version=x_api_version, fields=fields, matter_docket_create_request=matter_docket_create_request)

Creates a matter docket

Outlines the parameters and data fields used when creating a new MatterDocket

### Example


```python
import openapi_client
from openapi_client.models.matter_docket_create_request import MatterDocketCreateRequest
from openapi_client.models.matter_docket_show import MatterDocketShow
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
    api_instance = openapi_client.MatterDocketsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    matter_docket_create_request = openapi_client.MatterDocketCreateRequest() # MatterDocketCreateRequest | Request Body for Matter Dockets (optional)

    try:
        # Creates a matter docket
        api_response = api_instance.matter_docket_create(x_api_version=x_api_version, fields=fields, matter_docket_create_request=matter_docket_create_request)
        print("The response of MatterDocketsApi->matter_docket_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatterDocketsApi->matter_docket_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **matter_docket_create_request** | [**MatterDocketCreateRequest**](MatterDocketCreateRequest.md)| Request Body for Matter Dockets | [optional] 

### Return type

[**MatterDocketShow**](MatterDocketShow.md)

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

# **matter_docket_destroy**
> matter_docket_destroy(id, x_api_version=x_api_version)

Deletes the requested matter docket

Outlines the parameters, optional and required, used when deleting the record for a single MatterDocket

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
    api_instance = openapi_client.MatterDocketsApi(api_client)
    id = 56 # int | The unique identifier for the MatterDocket.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Deletes the requested matter docket
        api_instance.matter_docket_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling MatterDocketsApi->matter_docket_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the MatterDocket. | 
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

# **matter_docket_index**
> MatterDocketList matter_docket_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, matter_status=matter_status, order=order, page_token=page_token, query=query, service_type_id=service_type_id, status=status, updated_since=updated_since)

Return the data for all matter dockets

Outlines the parameters, optional and required, used when requesting the data for all MatterDockets

### Example


```python
import openapi_client
from openapi_client.models.matter_docket_list import MatterDocketList
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
    api_instance = openapi_client.MatterDocketsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter MatterDocket records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter MatterDocket records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of MatterDocket records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property. (optional)
    matter_status = 'matter_status_example' # str | Filter MatterDocket records to those with Matters having a specific status. (optional)
    order = 'order_example' # str | Orders the MatterDocket records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `name` matching a given string. (optional)
    service_type_id = 56 # int | The unique identifier for a single ServiceType. Use the keyword `null` to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property. (optional)
    status = 'status_example' # str | Filter MatterDocket records to those having a specific status. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter MatterDocket records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all matter dockets
        api_response = api_instance.matter_docket_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, matter_status=matter_status, order=order, page_token=page_token, query=query, service_type_id=service_type_id, status=status, updated_since=updated_since)
        print("The response of MatterDocketsApi->matter_docket_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatterDocketsApi->matter_docket_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter MatterDocket records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter MatterDocket records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of MatterDocket records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property. | [optional] 
 **matter_status** | **str**| Filter MatterDocket records to those with Matters having a specific status. | [optional] 
 **order** | **str**| Orders the MatterDocket records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching a given string. | [optional] 
 **service_type_id** | **int**| The unique identifier for a single ServiceType. Use the keyword &#x60;null&#x60; to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property. | [optional] 
 **status** | **str**| Filter MatterDocket records to those having a specific status. | [optional] 
 **updated_since** | **datetime**| Filter MatterDocket records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**MatterDocketList**](MatterDocketList.md)

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

# **matter_docket_preview**
> matter_docket_preview(jurisdiction_id, service_type_id, start_date, start_time, trigger_id, event_prefix=event_prefix)

Preview calendar dates for the docket

Preview calendar dates for the docket

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
    api_instance = openapi_client.MatterDocketsApi(api_client)
    jurisdiction_id = 56 # int | The unique identifier for a single Jurisdiction. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.
    service_type_id = 56 # int | The unique identifier for a single ServiceType. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.
    start_date = '2013-10-20T19:20:30+01:00' # datetime | The date the MatterDocket should start. (Expects an ISO-8601 date).
    start_time = '2013-10-20T19:20:30+01:00' # datetime | The time the MatterDocket should start. (Expects an ISO-8601 timestamp).
    trigger_id = 56 # int | The unique identifier for a single JurisdictionsToTrigger. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.
    event_prefix = 'event_prefix_example' # str | The prefix that will be added to the beginning of all court rule event titles (optional)

    try:
        # Preview calendar dates for the docket
        api_instance.matter_docket_preview(jurisdiction_id, service_type_id, start_date, start_time, trigger_id, event_prefix=event_prefix)
    except Exception as e:
        print("Exception when calling MatterDocketsApi->matter_docket_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jurisdiction_id** | **int**| The unique identifier for a single Jurisdiction. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property. | 
 **service_type_id** | **int**| The unique identifier for a single ServiceType. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property. | 
 **start_date** | **datetime**| The date the MatterDocket should start. (Expects an ISO-8601 date). | 
 **start_time** | **datetime**| The time the MatterDocket should start. (Expects an ISO-8601 timestamp). | 
 **trigger_id** | **int**| The unique identifier for a single JurisdictionsToTrigger. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property. | 
 **event_prefix** | **str**| The prefix that will be added to the beginning of all court rule event titles | [optional] 

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
**303** | See Other |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matter_docket_show**
> MatterDocketShow matter_docket_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for the matter docket

Outlines the parameters, optional and required, used when requesting the data for a single MatterDocket

### Example


```python
import openapi_client
from openapi_client.models.matter_docket_show import MatterDocketShow
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
    api_instance = openapi_client.MatterDocketsApi(api_client)
    id = 56 # int | The unique identifier for the MatterDocket.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for the matter docket
        api_response = api_instance.matter_docket_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of MatterDocketsApi->matter_docket_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatterDocketsApi->matter_docket_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the MatterDocket. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**MatterDocketShow**](MatterDocketShow.md)

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

