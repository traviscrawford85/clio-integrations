# openapi_client.CommunicationsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**communication_create**](CommunicationsApi.md#communication_create) | **POST** /communications.json | Create a new Communication
[**communication_destroy**](CommunicationsApi.md#communication_destroy) | **DELETE** /communications/{id}.json | Delete a single Communication
[**communication_index**](CommunicationsApi.md#communication_index) | **GET** /communications.json | Return the data for all Communications
[**communication_show**](CommunicationsApi.md#communication_show) | **GET** /communications/{id}.json | Return the data for a single Communication
[**communication_update**](CommunicationsApi.md#communication_update) | **PATCH** /communications/{id}.json | Update a single Communication


# **communication_create**
> CommunicationShow communication_create(x_api_version=x_api_version, fields=fields, communication_create_request=communication_create_request)

Create a new Communication

Outlines the parameters and data fields used when creating a new Communication

### Example


```python
import openapi_client
from openapi_client.models.communication_create_request import CommunicationCreateRequest
from openapi_client.models.communication_show import CommunicationShow
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
    api_instance = openapi_client.CommunicationsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    communication_create_request = openapi_client.CommunicationCreateRequest() # CommunicationCreateRequest | Request Body for Communications (optional)

    try:
        # Create a new Communication
        api_response = api_instance.communication_create(x_api_version=x_api_version, fields=fields, communication_create_request=communication_create_request)
        print("The response of CommunicationsApi->communication_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->communication_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **communication_create_request** | [**CommunicationCreateRequest**](CommunicationCreateRequest.md)| Request Body for Communications | [optional] 

### Return type

[**CommunicationShow**](CommunicationShow.md)

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

# **communication_destroy**
> communication_destroy(id, x_api_version=x_api_version)

Delete a single Communication

Outlines the parameters, optional and required, used when deleting the record for a single Communication

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
    api_instance = openapi_client.CommunicationsApi(api_client)
    id = 56 # int | The unique identifier for the Communication.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Communication
        api_instance.communication_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CommunicationsApi->communication_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Communication. | 
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

# **communication_index**
> CommunicationList communication_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, var_date=var_date, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, having_time_entries=having_time_entries, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, query=query, received_at=received_at, received_before=received_before, received_since=received_since, type=type, updated_since=updated_since, user_id=user_id)

Return the data for all Communications

Outlines the parameters, optional and required, used when requesting the data for all Communications

### Example


```python
import openapi_client
from openapi_client.models.communication_list import CommunicationList
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
    api_instance = openapi_client.CommunicationsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Communication records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Communication records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    var_date = '2013-10-20' # date | Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date). (optional)
    external_property_name = 'external_property_name_example' # str | Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name`  (optional)
    external_property_value = 'external_property_value_example' # str | Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value`  (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    having_time_entries = True # bool | Filter Communication records to those that do or do not have time entries. (optional)
    ids = 56 # int | Filter Communication records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Communication records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Communication. The list will be filtered to include only the Communication records with the matching property. (optional)
    order = 'order_example' # str | Orders the Communication records by the given field. Default: `date(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `body` or `subject` matching a given string. (optional)
    received_at = '2013-10-20T19:20:30+01:00' # datetime | Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time). (optional)
    received_before = '2013-10-20T19:20:30+01:00' # datetime | Filter Communication records to those whose `date` is on or before the date provided (Expects an ISO-8601 date). (optional)
    received_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Communication records to those whose `date` is on or after the date provided (Expects an ISO-8601 date). (optional)
    type = 'type_example' # str | Filter Communication records to those of the specified type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Communication records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    user_id = 56 # int | The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the Communication records with the matching property. (optional)

    try:
        # Return the data for all Communications
        api_response = api_instance.communication_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, var_date=var_date, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, having_time_entries=having_time_entries, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, query=query, received_at=received_at, received_before=received_before, received_since=received_since, type=type, updated_since=updated_since, user_id=user_id)
        print("The response of CommunicationsApi->communication_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->communication_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Communication records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Communication records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **var_date** | **date**| Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date). | [optional] 
 **external_property_name** | **str**| Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60;  | [optional] 
 **external_property_value** | **str**| Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60;  | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **having_time_entries** | **bool**| Filter Communication records to those that do or do not have time entries. | [optional] 
 **ids** | **int**| Filter Communication records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Communication records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Communication. The list will be filtered to include only the Communication records with the matching property. | [optional] 
 **order** | **str**| Orders the Communication records by the given field. Default: &#x60;date(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;body&#x60; or &#x60;subject&#x60; matching a given string. | [optional] 
 **received_at** | **datetime**| Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time). | [optional] 
 **received_before** | **datetime**| Filter Communication records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date). | [optional] 
 **received_since** | **datetime**| Filter Communication records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date). | [optional] 
 **type** | **str**| Filter Communication records to those of the specified type. | [optional] 
 **updated_since** | **datetime**| Filter Communication records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **user_id** | **int**| The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Communication records with the matching property. | [optional] 

### Return type

[**CommunicationList**](CommunicationList.md)

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

# **communication_show**
> CommunicationShow communication_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Communication

Outlines the parameters, optional and required, used when requesting the data for a single Communication

### Example


```python
import openapi_client
from openapi_client.models.communication_show import CommunicationShow
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
    api_instance = openapi_client.CommunicationsApi(api_client)
    id = 56 # int | The unique identifier for the Communication.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Communication
        api_response = api_instance.communication_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of CommunicationsApi->communication_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->communication_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Communication. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**CommunicationShow**](CommunicationShow.md)

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

# **communication_update**
> CommunicationShow communication_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, communication_update_request=communication_update_request)

Update a single Communication

Outlines the parameters and data fields used when updating a single Communication

### Example


```python
import openapi_client
from openapi_client.models.communication_show import CommunicationShow
from openapi_client.models.communication_update_request import CommunicationUpdateRequest
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
    api_instance = openapi_client.CommunicationsApi(api_client)
    id = 56 # int | The unique identifier for the Communication.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    communication_update_request = openapi_client.CommunicationUpdateRequest() # CommunicationUpdateRequest | Request Body for Communications (optional)

    try:
        # Update a single Communication
        api_response = api_instance.communication_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, communication_update_request=communication_update_request)
        print("The response of CommunicationsApi->communication_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->communication_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Communication. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **communication_update_request** | [**CommunicationUpdateRequest**](CommunicationUpdateRequest.md)| Request Body for Communications | [optional] 

### Return type

[**CommunicationShow**](CommunicationShow.md)

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

