# openapi_client.MyEventsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**my_event_destroy**](MyEventsApi.md#my_event_destroy) | **DELETE** /internal_notifications/my_events/{id}.json | Clear (delete) a single in-app notification event
[**my_event_index**](MyEventsApi.md#my_event_index) | **GET** /internal_notifications/my_events.json | Return the data for all of my in-app notification events
[**my_event_update**](MyEventsApi.md#my_event_update) | **PATCH** /internal_notifications/my_events/{id}.json | Mark a single in-app notification event as read/unread


# **my_event_destroy**
> my_event_destroy(id, x_api_version=x_api_version)

Clear (delete) a single in-app notification event

Outlines the parameters, optional and required, used when deleting the record for a single MyEvent

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
    api_instance = openapi_client.MyEventsApi(api_client)
    id = 56 # int | The unique identifier for the MyEvent.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Clear (delete) a single in-app notification event
        api_instance.my_event_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling MyEventsApi->my_event_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the MyEvent. | 
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

# **my_event_index**
> MyEventList my_event_index(x_api_version=x_api_version, fields=fields, limit=limit, page_token=page_token)

Return the data for all of my in-app notification events

Outlines the parameters, optional and required, used when requesting the data for all MyEvents

### Example


```python
import openapi_client
from openapi_client.models.my_event_list import MyEventList
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
    api_instance = openapi_client.MyEventsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    limit = 56 # int | A limit on the number of MyEvent records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)

    try:
        # Return the data for all of my in-app notification events
        api_response = api_instance.my_event_index(x_api_version=x_api_version, fields=fields, limit=limit, page_token=page_token)
        print("The response of MyEventsApi->my_event_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyEventsApi->my_event_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **limit** | **int**| A limit on the number of MyEvent records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 

### Return type

[**MyEventList**](MyEventList.md)

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

# **my_event_update**
> MyEventShow my_event_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, my_event_update_request=my_event_update_request)

Mark a single in-app notification event as read/unread

Outlines the parameters and data fields used when updating a single MyEvent

### Example


```python
import openapi_client
from openapi_client.models.my_event_show import MyEventShow
from openapi_client.models.my_event_update_request import MyEventUpdateRequest
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
    api_instance = openapi_client.MyEventsApi(api_client)
    id = 56 # int | The unique identifier for the MyEvent.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    my_event_update_request = openapi_client.MyEventUpdateRequest() # MyEventUpdateRequest | Request Body for My Events (optional)

    try:
        # Mark a single in-app notification event as read/unread
        api_response = api_instance.my_event_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, my_event_update_request=my_event_update_request)
        print("The response of MyEventsApi->my_event_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyEventsApi->my_event_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the MyEvent. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **my_event_update_request** | [**MyEventUpdateRequest**](MyEventUpdateRequest.md)| Request Body for My Events | [optional] 

### Return type

[**MyEventShow**](MyEventShow.md)

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

