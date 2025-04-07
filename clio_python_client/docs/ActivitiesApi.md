# openapi_client.ActivitiesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activity_create**](ActivitiesApi.md#activity_create) | **POST** /activities.json | Create a new Activity
[**activity_destroy**](ActivitiesApi.md#activity_destroy) | **DELETE** /activities/{id}.json | Delete a single Activity
[**activity_index**](ActivitiesApi.md#activity_index) | **GET** /activities.json | Return the data for all Activities
[**activity_show**](ActivitiesApi.md#activity_show) | **GET** /activities/{id}.json | Return the data for a single Activity
[**activity_update**](ActivitiesApi.md#activity_update) | **PATCH** /activities/{id}.json | Update a single Activity


# **activity_create**
> ActivityShow activity_create(x_api_version=x_api_version, fields=fields, activity_create_request=activity_create_request)

Create a new Activity

Outlines the parameters and data fields used when creating a new Activity

### Example


```python
import openapi_client
from openapi_client.models.activity_create_request import ActivityCreateRequest
from openapi_client.models.activity_show import ActivityShow
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    activity_create_request = openapi_client.ActivityCreateRequest() # ActivityCreateRequest | Request Body for Activities (optional)

    try:
        # Create a new Activity
        api_response = api_instance.activity_create(x_api_version=x_api_version, fields=fields, activity_create_request=activity_create_request)
        print("The response of ActivitiesApi->activity_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activity_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **activity_create_request** | [**ActivityCreateRequest**](ActivityCreateRequest.md)| Request Body for Activities | [optional] 

### Return type

[**ActivityShow**](ActivityShow.md)

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

# **activity_destroy**
> activity_destroy(id, x_api_version=x_api_version)

Delete a single Activity

Outlines the parameters, optional and required, used when deleting the record for a single Activity

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
    api_instance = openapi_client.ActivitiesApi(api_client)
    id = 56 # int | The unique identifier for the Activity.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Activity
        api_instance.activity_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activity_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Activity. | 
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

# **activity_index**
> ActivityList activity_index(x_api_version=x_api_version, activity_description_id=activity_description_id, calendar_entry_id=calendar_entry_id, communication_id=communication_id, contact_note_id=contact_note_id, created_since=created_since, end_date=end_date, expense_category_id=expense_category_id, fields=fields, flat_rate=flat_rate, grant_id=grant_id, ids=ids, limit=limit, matter_id=matter_id, matter_note_id=matter_note_id, only_unaccounted_for=only_unaccounted_for, order=order, page_token=page_token, query=query, start_date=start_date, status=status, task_id=task_id, type=type, updated_since=updated_since, user_id=user_id)

Return the data for all Activities

Outlines the parameters, optional and required, used when requesting the data for all Activities

### Example


```python
import openapi_client
from openapi_client.models.activity_list import ActivityList
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    activity_description_id = 56 # int | The unique identifier for a single ActivityDescription. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    calendar_entry_id = 56 # int | The unique identifier for a single CalendarEntry. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    communication_id = 56 # int | The unique identifier for a single Communication. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    contact_note_id = 56 # int | The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter Activity records to those whose `date` is on or before the date provided (Expects an ISO-8601 date). (optional)
    expense_category_id = 56 # int | The unique identifier for a single ExpenseCategory. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    flat_rate = True # bool | Filter Activity TimeEntry records to those that have a flat rate, or not. (optional)
    grant_id = 56 # int | The unique identifier for a single Grant. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    ids = 56 # int | Filter Activity records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    matter_note_id = 56 # int | The unique identifier for a single Note. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    only_unaccounted_for = True # bool | Only unaccounted for activities. (optional)
    order = 'order_example' # str | Orders the Activity records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `note` matching a given string. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter Activity records to those whose `date` is on or after the date provided (Expects an ISO-8601 date). (optional)
    status = 'status_example' # str | Filter Activity records to those that are draft, billed, unbilled or non-billable. (optional)
    task_id = 56 # int | The unique identifier for a single Task. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)
    type = 'type_example' # str | Filter Activity records to those of a specific type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    user_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. (optional)

    try:
        # Return the data for all Activities
        api_response = api_instance.activity_index(x_api_version=x_api_version, activity_description_id=activity_description_id, calendar_entry_id=calendar_entry_id, communication_id=communication_id, contact_note_id=contact_note_id, created_since=created_since, end_date=end_date, expense_category_id=expense_category_id, fields=fields, flat_rate=flat_rate, grant_id=grant_id, ids=ids, limit=limit, matter_id=matter_id, matter_note_id=matter_note_id, only_unaccounted_for=only_unaccounted_for, order=order, page_token=page_token, query=query, start_date=start_date, status=status, task_id=task_id, type=type, updated_since=updated_since, user_id=user_id)
        print("The response of ActivitiesApi->activity_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activity_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **activity_description_id** | **int**| The unique identifier for a single ActivityDescription. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **calendar_entry_id** | **int**| The unique identifier for a single CalendarEntry. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **communication_id** | **int**| The unique identifier for a single Communication. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **contact_note_id** | **int**| The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **end_date** | **datetime**| Filter Activity records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date). | [optional] 
 **expense_category_id** | **int**| The unique identifier for a single ExpenseCategory. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **flat_rate** | **bool**| Filter Activity TimeEntry records to those that have a flat rate, or not. | [optional] 
 **grant_id** | **int**| The unique identifier for a single Grant. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **ids** | **int**| Filter Activity records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **matter_note_id** | **int**| The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **only_unaccounted_for** | **bool**| Only unaccounted for activities. | [optional] 
 **order** | **str**| Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;note&#x60; matching a given string. | [optional] 
 **start_date** | **datetime**| Filter Activity records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date). | [optional] 
 **status** | **str**| Filter Activity records to those that are draft, billed, unbilled or non-billable. | [optional] 
 **task_id** | **int**| The unique identifier for a single Task. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 
 **type** | **str**| Filter Activity records to those of a specific type. | [optional] 
 **updated_since** | **datetime**| Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **user_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property. | [optional] 

### Return type

[**ActivityList**](ActivityList.md)

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

# **activity_show**
> ActivityShow activity_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Activity

Outlines the parameters, optional and required, used when requesting the data for a single Activity

### Example


```python
import openapi_client
from openapi_client.models.activity_show import ActivityShow
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    id = 56 # int | The unique identifier for the Activity.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Activity
        api_response = api_instance.activity_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ActivitiesApi->activity_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activity_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Activity. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ActivityShow**](ActivityShow.md)

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

# **activity_update**
> ActivityShow activity_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, activity_update_request=activity_update_request)

Update a single Activity

Outlines the parameters and data fields used when updating a single Activity

### Example


```python
import openapi_client
from openapi_client.models.activity_show import ActivityShow
from openapi_client.models.activity_update_request import ActivityUpdateRequest
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    id = 56 # int | The unique identifier for the Activity.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    activity_update_request = openapi_client.ActivityUpdateRequest() # ActivityUpdateRequest | Request Body for Activities (optional)

    try:
        # Update a single Activity
        api_response = api_instance.activity_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, activity_update_request=activity_update_request)
        print("The response of ActivitiesApi->activity_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activity_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Activity. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **activity_update_request** | [**ActivityUpdateRequest**](ActivityUpdateRequest.md)| Request Body for Activities | [optional] 

### Return type

[**ActivityShow**](ActivityShow.md)

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

