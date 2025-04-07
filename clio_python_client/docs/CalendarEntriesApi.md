# openapi_client.CalendarEntriesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_entry_create**](CalendarEntriesApi.md#calendar_entry_create) | **POST** /calendar_entries.json | Create a new CalendarEntry
[**calendar_entry_destroy**](CalendarEntriesApi.md#calendar_entry_destroy) | **DELETE** /calendar_entries/{id}.json | Delete a single CalendarEntry
[**calendar_entry_index**](CalendarEntriesApi.md#calendar_entry_index) | **GET** /calendar_entries.json | Return the data for all CalendarEntries
[**calendar_entry_show**](CalendarEntriesApi.md#calendar_entry_show) | **GET** /calendar_entries/{id}.json | Return the data for a single CalendarEntry
[**calendar_entry_update**](CalendarEntriesApi.md#calendar_entry_update) | **PATCH** /calendar_entries/{id}.json | Update a single CalendarEntry


# **calendar_entry_create**
> CalendarEntryShow calendar_entry_create(x_api_version=x_api_version, fields=fields, calendar_entry_create_request=calendar_entry_create_request)

Create a new CalendarEntry

Outlines the parameters and data fields used when creating a new CalendarEntry

### Example


```python
import openapi_client
from openapi_client.models.calendar_entry_create_request import CalendarEntryCreateRequest
from openapi_client.models.calendar_entry_show import CalendarEntryShow
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
    api_instance = openapi_client.CalendarEntriesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    calendar_entry_create_request = openapi_client.CalendarEntryCreateRequest() # CalendarEntryCreateRequest | Request Body for Calendar Entries (optional)

    try:
        # Create a new CalendarEntry
        api_response = api_instance.calendar_entry_create(x_api_version=x_api_version, fields=fields, calendar_entry_create_request=calendar_entry_create_request)
        print("The response of CalendarEntriesApi->calendar_entry_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEntriesApi->calendar_entry_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **calendar_entry_create_request** | [**CalendarEntryCreateRequest**](CalendarEntryCreateRequest.md)| Request Body for Calendar Entries | [optional] 

### Return type

[**CalendarEntryShow**](CalendarEntryShow.md)

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

# **calendar_entry_destroy**
> calendar_entry_destroy(id, x_api_version=x_api_version)

Delete a single CalendarEntry

Outlines the parameters, optional and required, used when deleting the record for a single CalendarEntry

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
    api_instance = openapi_client.CalendarEntriesApi(api_client)
    id = 56 # int | The unique identifier for the CalendarEntry.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single CalendarEntry
        api_instance.calendar_entry_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CalendarEntriesApi->calendar_entry_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CalendarEntry. | 
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

# **calendar_entry_index**
> CalendarEntryList calendar_entry_index(x_api_version=x_api_version, calendar_id=calendar_id, created_since=created_since, expanded=expanded, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, var_from=var_from, has_court_rule=has_court_rule, ids=ids, is_all_day=is_all_day, limit=limit, matter_id=matter_id, owner_entries_across_all_users=owner_entries_across_all_users, page_token=page_token, query=query, source=source, to=to, updated_since=updated_since, visible=visible)

Return the data for all CalendarEntries

Outlines the parameters, optional and required, used when requesting the data for all CalendarEntries

### Example


```python
import openapi_client
from openapi_client.models.calendar_entry_list import CalendarEntryList
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
    api_instance = openapi_client.CalendarEntriesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    calendar_id = 56 # int | The unique identifier for a single Calendar. The keyword `null` is not valid for this field. The list will be filtered to include only the CalendarEntry records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter CalendarEntry records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    expanded = True # bool | Returns a record for each occurrence of a recurring calendar event.  Non-recurring calendar events are unaffected and returned as separate records regardless of the expanded setting. (optional)
    external_property_name = 'external_property_name_example' # str | Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name`  (optional)
    external_property_value = 'external_property_value_example' # str | Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value`  (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Filter CalendarEntry records to those that end on or after the provided time (Expects an ISO-8601 timestamp). (optional)
    has_court_rule = True # bool | Allows matching court rule on calendar entry. (optional)
    ids = 56 # int | Filter CalendarEntry records to those having the specified unique identifiers. (optional)
    is_all_day = True # bool | Filter CalendarEntry records to those that are marked as all day events. (optional)
    limit = 56 # int | A limit on the number of CalendarEntry records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a CalendarEntry. The list will be filtered to include only the CalendarEntry records with the matching property. (optional)
    owner_entries_across_all_users = True # bool | Returns CalendarEntry records for all users related to a matter. Requires matter id. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Allows matching search on calendar entry. (optional)
    source = 'source_example' # str | Filter CalendarEntry records to those having a specific calendar visibility source (mobile, web). (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Filter CalendarEntry records to those that begin on or before the provided time (Expects an ISO-8601 timestamp). (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter CalendarEntry records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    visible = True # bool | Filter CalendarEntry records to those that are visible. (optional)

    try:
        # Return the data for all CalendarEntries
        api_response = api_instance.calendar_entry_index(x_api_version=x_api_version, calendar_id=calendar_id, created_since=created_since, expanded=expanded, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, var_from=var_from, has_court_rule=has_court_rule, ids=ids, is_all_day=is_all_day, limit=limit, matter_id=matter_id, owner_entries_across_all_users=owner_entries_across_all_users, page_token=page_token, query=query, source=source, to=to, updated_since=updated_since, visible=visible)
        print("The response of CalendarEntriesApi->calendar_entry_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEntriesApi->calendar_entry_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **calendar_id** | **int**| The unique identifier for a single Calendar. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the CalendarEntry records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter CalendarEntry records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **expanded** | **bool**| Returns a record for each occurrence of a recurring calendar event.  Non-recurring calendar events are unaffected and returned as separate records regardless of the expanded setting. | [optional] 
 **external_property_name** | **str**| Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60;  | [optional] 
 **external_property_value** | **str**| Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60;  | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **var_from** | **datetime**| Filter CalendarEntry records to those that end on or after the provided time (Expects an ISO-8601 timestamp). | [optional] 
 **has_court_rule** | **bool**| Allows matching court rule on calendar entry. | [optional] 
 **ids** | **int**| Filter CalendarEntry records to those having the specified unique identifiers. | [optional] 
 **is_all_day** | **bool**| Filter CalendarEntry records to those that are marked as all day events. | [optional] 
 **limit** | **int**| A limit on the number of CalendarEntry records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a CalendarEntry. The list will be filtered to include only the CalendarEntry records with the matching property. | [optional] 
 **owner_entries_across_all_users** | **bool**| Returns CalendarEntry records for all users related to a matter. Requires matter id. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Allows matching search on calendar entry. | [optional] 
 **source** | **str**| Filter CalendarEntry records to those having a specific calendar visibility source (mobile, web). | [optional] 
 **to** | **datetime**| Filter CalendarEntry records to those that begin on or before the provided time (Expects an ISO-8601 timestamp). | [optional] 
 **updated_since** | **datetime**| Filter CalendarEntry records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **visible** | **bool**| Filter CalendarEntry records to those that are visible. | [optional] 

### Return type

[**CalendarEntryList**](CalendarEntryList.md)

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

# **calendar_entry_show**
> CalendarEntryShow calendar_entry_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single CalendarEntry

Outlines the parameters, optional and required, used when requesting the data for a single CalendarEntry

### Example


```python
import openapi_client
from openapi_client.models.calendar_entry_show import CalendarEntryShow
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
    api_instance = openapi_client.CalendarEntriesApi(api_client)
    id = 56 # int | The unique identifier for the CalendarEntry.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single CalendarEntry
        api_response = api_instance.calendar_entry_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of CalendarEntriesApi->calendar_entry_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEntriesApi->calendar_entry_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CalendarEntry. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**CalendarEntryShow**](CalendarEntryShow.md)

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

# **calendar_entry_update**
> CalendarEntryShow calendar_entry_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, calendar_entry_update_request=calendar_entry_update_request)

Update a single CalendarEntry

Outlines the parameters and data fields used when updating a single CalendarEntry

### Example


```python
import openapi_client
from openapi_client.models.calendar_entry_show import CalendarEntryShow
from openapi_client.models.calendar_entry_update_request import CalendarEntryUpdateRequest
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
    api_instance = openapi_client.CalendarEntriesApi(api_client)
    id = 56 # int | The unique identifier for the CalendarEntry.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    calendar_entry_update_request = openapi_client.CalendarEntryUpdateRequest() # CalendarEntryUpdateRequest | Request Body for Calendar Entries (optional)

    try:
        # Update a single CalendarEntry
        api_response = api_instance.calendar_entry_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, calendar_entry_update_request=calendar_entry_update_request)
        print("The response of CalendarEntriesApi->calendar_entry_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEntriesApi->calendar_entry_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the CalendarEntry. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **calendar_entry_update_request** | [**CalendarEntryUpdateRequest**](CalendarEntryUpdateRequest.md)| Request Body for Calendar Entries | [optional] 

### Return type

[**CalendarEntryShow**](CalendarEntryShow.md)

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

