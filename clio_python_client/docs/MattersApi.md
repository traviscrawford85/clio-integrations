# openapi_client.MattersApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matter_create**](MattersApi.md#matter_create) | **POST** /matters.json | Create a new Matter
[**matter_destroy**](MattersApi.md#matter_destroy) | **DELETE** /matters/{id}.json | Delete a single Matter
[**matter_index**](MattersApi.md#matter_index) | **GET** /matters.json | Return the data for all Matters
[**matter_show**](MattersApi.md#matter_show) | **GET** /matters/{id}.json | Return the data for a single Matter
[**matter_update**](MattersApi.md#matter_update) | **PATCH** /matters/{id}.json | Update a single Matter


# **matter_create**
> MatterShow matter_create(x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, matter_create_request=matter_create_request)

Create a new Matter

Outlines the parameters and data fields used when creating a new Matter

### Example


```python
import openapi_client
from openapi_client.models.matter_create_request import MatterCreateRequest
from openapi_client.models.matter_show import MatterShow
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
    api_instance = openapi_client.MattersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    custom_field_ids = 56 # int | Filter Matter's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    matter_create_request = openapi_client.MatterCreateRequest() # MatterCreateRequest | Request Body for Matters (optional)

    try:
        # Create a new Matter
        api_response = api_instance.matter_create(x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, matter_create_request=matter_create_request)
        print("The response of MattersApi->matter_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MattersApi->matter_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **custom_field_ids** | **int**| Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **matter_create_request** | [**MatterCreateRequest**](MatterCreateRequest.md)| Request Body for Matters | [optional] 

### Return type

[**MatterShow**](MatterShow.md)

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

# **matter_destroy**
> matter_destroy(id, x_api_version=x_api_version)

Delete a single Matter

Outlines the parameters, optional and required, used when deleting the record for a single Matter

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
    api_instance = openapi_client.MattersApi(api_client)
    id = 56 # int | The unique identifier for the Matter.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Matter
        api_instance.matter_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling MattersApi->matter_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Matter. | 
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

# **matter_index**
> MatterList matter_index(x_api_version=x_api_version, billable=billable, client_id=client_id, close_date=close_date, created_since=created_since, custom_field_ids=custom_field_ids, custom_field_values=custom_field_values, fields=fields, grant_id=grant_id, group_id=group_id, ids=ids, limit=limit, notification_event_subscriber_user_id=notification_event_subscriber_user_id, open_date=open_date, order=order, originating_attorney_id=originating_attorney_id, page_token=page_token, pending_date=pending_date, practice_area_id=practice_area_id, query=query, responsible_attorney_id=responsible_attorney_id, status=status, subscriber_user_id=subscriber_user_id, updated_since=updated_since)

Return the data for all Matters

Outlines the parameters, optional and required, used when requesting the data for all Matters

### Example


```python
import openapi_client
from openapi_client.models.matter_list import MatterList
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
    api_instance = openapi_client.MattersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    billable = True # bool | Filter Matter records to those which are billable. (optional)
    client_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property. (optional)
    close_date = 'close_date_example' # str | Filter Matter records by the close date. The date should be provided in the format YYYY-MM-DD.  e.g. `?close_date==2020-01-01`, `?close_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?close_date[]=>=2020-01-01&close_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned.  (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Matter records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    custom_field_ids = 56 # int | Filter Matter's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    custom_field_values = 'custom_field_values_example' # str | Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]`  (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    grant_id = 56 # int | The unique identifier for a single Grant. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. (optional)
    group_id = 56 # int | The unique identifier for a single Group. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property. (optional)
    ids = 56 # int | Filter Matter records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Matter records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    notification_event_subscriber_user_id = 56 # int | The unique identifier for a single NotificationEventSubscriber. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. (optional)
    open_date = 'open_date_example' # str | Filter Matter records by the open date. The date should be provided in the format YYYY-MM-DD.  e.g. `?open_date==2020-01-01`, `?open_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?open_date[]=>=2020-01-01&open_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned.  (optional)
    order = 'order_example' # str | Orders the Matter records by the given field. Default: `id(asc)`. (optional)
    originating_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    pending_date = 'pending_date_example' # str | Filter Matter records by the pending date. The date should be provided in the format YYYY-MM-DD.  e.g. `?pending_date==2020-01-01`, `?pending_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?pending_date[]=>=2020-01-01&pending_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned.  (optional)
    practice_area_id = 56 # int | The unique identifier for a single PracticeArea. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property. (optional)
    query = 'query_example' # str | Wildcard search for `display_number`, `number` or `description` matching a given string, as well as the `first_name`, `last_name` or `name` of the associated client. (optional)
    responsible_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. (optional)
    status = 'status_example' # str | Filter Matter records to those with a given status. It accepts comma-separated statuses, e.g. `open,pending`. (optional)
    subscriber_user_id = 56 # int | The unique identifier for a single NotificationEventSubscriber. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Matter records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Matters
        api_response = api_instance.matter_index(x_api_version=x_api_version, billable=billable, client_id=client_id, close_date=close_date, created_since=created_since, custom_field_ids=custom_field_ids, custom_field_values=custom_field_values, fields=fields, grant_id=grant_id, group_id=group_id, ids=ids, limit=limit, notification_event_subscriber_user_id=notification_event_subscriber_user_id, open_date=open_date, order=order, originating_attorney_id=originating_attorney_id, page_token=page_token, pending_date=pending_date, practice_area_id=practice_area_id, query=query, responsible_attorney_id=responsible_attorney_id, status=status, subscriber_user_id=subscriber_user_id, updated_since=updated_since)
        print("The response of MattersApi->matter_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MattersApi->matter_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **billable** | **bool**| Filter Matter records to those which are billable. | [optional] 
 **client_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **close_date** | **str**| Filter Matter records by the close date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?close_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?close_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?close_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;close_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned.  | [optional] 
 **created_since** | **datetime**| Filter Matter records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **custom_field_ids** | **int**| Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **custom_field_values** | **str**| Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60;  | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **grant_id** | **int**| The unique identifier for a single Grant. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **group_id** | **int**| The unique identifier for a single Group. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **ids** | **int**| Filter Matter records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Matter records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **notification_event_subscriber_user_id** | **int**| The unique identifier for a single NotificationEventSubscriber. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **open_date** | **str**| Filter Matter records by the open date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?open_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?open_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?open_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;open_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned.  | [optional] 
 **order** | **str**| Orders the Matter records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **originating_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **pending_date** | **str**| Filter Matter records by the pending date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?pending_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?pending_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?pending_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;pending_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned.  | [optional] 
 **practice_area_id** | **int**| The unique identifier for a single PracticeArea. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **query** | **str**| Wildcard search for &#x60;display_number&#x60;, &#x60;number&#x60; or &#x60;description&#x60; matching a given string, as well as the &#x60;first_name&#x60;, &#x60;last_name&#x60; or &#x60;name&#x60; of the associated client. | [optional] 
 **responsible_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **status** | **str**| Filter Matter records to those with a given status. It accepts comma-separated statuses, e.g. &#x60;open,pending&#x60;. | [optional] 
 **subscriber_user_id** | **int**| The unique identifier for a single NotificationEventSubscriber. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property. | [optional] 
 **updated_since** | **datetime**| Filter Matter records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**MatterList**](MatterList.md)

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

# **matter_show**
> MatterShow matter_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields)

Return the data for a single Matter

Outlines the parameters, optional and required, used when requesting the data for a single Matter

### Example


```python
import openapi_client
from openapi_client.models.matter_show import MatterShow
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
    api_instance = openapi_client.MattersApi(api_client)
    id = 56 # int | The unique identifier for the Matter.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    custom_field_ids = 56 # int | Filter Matter's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Matter
        api_response = api_instance.matter_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields)
        print("The response of MattersApi->matter_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MattersApi->matter_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Matter. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **custom_field_ids** | **int**| Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**MatterShow**](MatterShow.md)

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

# **matter_update**
> MatterShow matter_update(id, if_match=if_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, matter_update_request=matter_update_request)

Update a single Matter

Outlines the parameters and data fields used when updating a single Matter

### Example


```python
import openapi_client
from openapi_client.models.matter_show import MatterShow
from openapi_client.models.matter_update_request import MatterUpdateRequest
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
    api_instance = openapi_client.MattersApi(api_client)
    id = 56 # int | The unique identifier for the Matter.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    custom_field_ids = 56 # int | Filter Matter's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    matter_update_request = openapi_client.MatterUpdateRequest() # MatterUpdateRequest | Request Body for Matters (optional)

    try:
        # Update a single Matter
        api_response = api_instance.matter_update(id, if_match=if_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, matter_update_request=matter_update_request)
        print("The response of MattersApi->matter_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MattersApi->matter_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Matter. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **custom_field_ids** | **int**| Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **matter_update_request** | [**MatterUpdateRequest**](MatterUpdateRequest.md)| Request Body for Matters | [optional] 

### Return type

[**MatterShow**](MatterShow.md)

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

