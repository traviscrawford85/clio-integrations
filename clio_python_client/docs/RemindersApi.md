# openapi_client.RemindersApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reminder_create**](RemindersApi.md#reminder_create) | **POST** /reminders.json | Create a new Reminder
[**reminder_destroy**](RemindersApi.md#reminder_destroy) | **DELETE** /reminders/{id}.json | Delete a single Reminder
[**reminder_index**](RemindersApi.md#reminder_index) | **GET** /reminders.json | Return the data for all Reminders
[**reminder_show**](RemindersApi.md#reminder_show) | **GET** /reminders/{id}.json | Return the data for a single Reminder
[**reminder_update**](RemindersApi.md#reminder_update) | **PATCH** /reminders/{id}.json | Update a single Reminder


# **reminder_create**
> ReminderShow reminder_create(x_api_version=x_api_version, fields=fields, reminder_create_request=reminder_create_request)

Create a new Reminder

Outlines the parameters and data fields used when creating a new Reminder

### Example


```python
import openapi_client
from openapi_client.models.reminder_create_request import ReminderCreateRequest
from openapi_client.models.reminder_show import ReminderShow
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
    api_instance = openapi_client.RemindersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    reminder_create_request = openapi_client.ReminderCreateRequest() # ReminderCreateRequest | Request Body for Reminders (optional)

    try:
        # Create a new Reminder
        api_response = api_instance.reminder_create(x_api_version=x_api_version, fields=fields, reminder_create_request=reminder_create_request)
        print("The response of RemindersApi->reminder_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemindersApi->reminder_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **reminder_create_request** | [**ReminderCreateRequest**](ReminderCreateRequest.md)| Request Body for Reminders | [optional] 

### Return type

[**ReminderShow**](ReminderShow.md)

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

# **reminder_destroy**
> reminder_destroy(id, x_api_version=x_api_version)

Delete a single Reminder

Outlines the parameters, optional and required, used when deleting the record for a single Reminder

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
    api_instance = openapi_client.RemindersApi(api_client)
    id = 56 # int | The unique identifier for the Reminder.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Reminder
        api_instance.reminder_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling RemindersApi->reminder_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Reminder. | 
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

# **reminder_index**
> ReminderList reminder_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, notification_method_id=notification_method_id, order=order, page_token=page_token, state=state, subject_id=subject_id, subject_type=subject_type, updated_since=updated_since, user_id=user_id)

Return the data for all Reminders

Outlines the parameters, optional and required, used when requesting the data for all Reminders

### Example


```python
import openapi_client
from openapi_client.models.reminder_list import ReminderList
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
    api_instance = openapi_client.RemindersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Reminder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Reminder records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Reminder records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    notification_method_id = 56 # int | The unique identifier for a single NotificationMethod. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property. (optional)
    order = 'order_example' # str | Orders the Reminder records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    state = 'state_example' # str | Filter Reminder records to those with a given state. (optional)
    subject_id = 56 # int | The unique identifier for a single CalendarEntry or Task. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property. (optional)
    subject_type = 'subject_type_example' # str | Filter Reminder records to those of a given subject type, required if using subject_id. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Reminder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    user_id = 56 # int | The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property. (optional)

    try:
        # Return the data for all Reminders
        api_response = api_instance.reminder_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, notification_method_id=notification_method_id, order=order, page_token=page_token, state=state, subject_id=subject_id, subject_type=subject_type, updated_since=updated_since, user_id=user_id)
        print("The response of RemindersApi->reminder_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemindersApi->reminder_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter Reminder records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Reminder records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Reminder records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **notification_method_id** | **int**| The unique identifier for a single NotificationMethod. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Reminder records with the matching property. | [optional] 
 **order** | **str**| Orders the Reminder records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **state** | **str**| Filter Reminder records to those with a given state. | [optional] 
 **subject_id** | **int**| The unique identifier for a single CalendarEntry or Task. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Reminder records with the matching property. | [optional] 
 **subject_type** | **str**| Filter Reminder records to those of a given subject type, required if using subject_id. | [optional] 
 **updated_since** | **datetime**| Filter Reminder records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **user_id** | **int**| The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Reminder records with the matching property. | [optional] 

### Return type

[**ReminderList**](ReminderList.md)

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

# **reminder_show**
> ReminderShow reminder_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Reminder

Outlines the parameters, optional and required, used when requesting the data for a single Reminder

### Example


```python
import openapi_client
from openapi_client.models.reminder_show import ReminderShow
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
    api_instance = openapi_client.RemindersApi(api_client)
    id = 56 # int | The unique identifier for the Reminder.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Reminder
        api_response = api_instance.reminder_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of RemindersApi->reminder_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemindersApi->reminder_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Reminder. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ReminderShow**](ReminderShow.md)

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

# **reminder_update**
> ReminderShow reminder_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, reminder_update_request=reminder_update_request)

Update a single Reminder

Outlines the parameters and data fields used when updating a single Reminder

### Example


```python
import openapi_client
from openapi_client.models.reminder_show import ReminderShow
from openapi_client.models.reminder_update_request import ReminderUpdateRequest
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
    api_instance = openapi_client.RemindersApi(api_client)
    id = 56 # int | The unique identifier for the Reminder.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    reminder_update_request = openapi_client.ReminderUpdateRequest() # ReminderUpdateRequest | Request Body for Reminders (optional)

    try:
        # Update a single Reminder
        api_response = api_instance.reminder_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, reminder_update_request=reminder_update_request)
        print("The response of RemindersApi->reminder_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemindersApi->reminder_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Reminder. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **reminder_update_request** | [**ReminderUpdateRequest**](ReminderUpdateRequest.md)| Request Body for Reminders | [optional] 

### Return type

[**ReminderShow**](ReminderShow.md)

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

