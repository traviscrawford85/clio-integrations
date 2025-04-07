# openapi_client.BillsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bill_destroy**](BillsApi.md#bill_destroy) | **DELETE** /bills/{id}.json | Delete or void a Bill
[**bill_index**](BillsApi.md#bill_index) | **GET** /bills.json | Return the data for all Bills
[**bill_preview**](BillsApi.md#bill_preview) | **GET** /bills/{id}/preview.json | Returns the pre-rendered html for the Bill
[**bill_show**](BillsApi.md#bill_show) | **GET** /bills/{id}.json | Return the data for a single Bill
[**bill_update**](BillsApi.md#bill_update) | **PATCH** /bills/{id}.json | Update a single Bill


# **bill_destroy**
> bill_destroy(id, x_api_version=x_api_version)

Delete or void a Bill

This endpoint will transition a bill to either its deleted or voided state. A bill can only be deleted or voided if it has no payments recorded and its current state is one of the following: * Draft * Pending Approval * Unpaid  A bill will automatically be moved to a deleted or void state based on its current state. The mappings for this are: * Draft -> Deleted * Pending Approval -> Deleted * Unpaid -> Void 

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
    api_instance = openapi_client.BillsApi(api_client)
    id = 56 # int | The unique identifier for the Bill.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete or void a Bill
        api_instance.bill_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BillsApi->bill_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Bill. | 
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

# **bill_index**
> BillList bill_index(x_api_version=x_api_version, client_id=client_id, created_since=created_since, custom_field_values=custom_field_values, due_after=due_after, due_at=due_at, due_before=due_before, fields=fields, ids=ids, issued_after=issued_after, issued_before=issued_before, last_sent_end_date=last_sent_end_date, last_sent_start_date=last_sent_start_date, limit=limit, matter_id=matter_id, order=order, originating_attorney_id=originating_attorney_id, overdue_only=overdue_only, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, state=state, status=status, type=type, updated_since=updated_since)

Return the data for all Bills

Outlines the parameters, optional and required, used when requesting the data for all Bills

### Example


```python
import openapi_client
from openapi_client.models.bill_list import BillList
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
    api_instance = openapi_client.BillsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    client_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Bill records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Bill records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    custom_field_values = 'custom_field_values_example' # str | Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]`  (optional)
    due_after = '2013-10-20' # date | Filter Bill records to those that have a `due_date` after the one provided (Expects an ISO-8601 date). (optional)
    due_at = '2013-10-20' # date | Filter Bill records to those that have a specific `due_date` (Expects an ISO-8601 date). (optional)
    due_before = '2013-10-20' # date | Filter Bill records to those that have a `due_date` before the one provided (Expects an ISO-8601 date). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Bill records to those having the specified unique identifiers. (optional)
    issued_after = '2013-10-20' # date | Filter Bill records to those that have an `issue_date` after the one provided (Expects an ISO-8601 date). (optional)
    issued_before = '2013-10-20' # date | Filter Bill records to those that have an `issue_date` before the one provided (Expects an ISO-8601 date). (optional)
    last_sent_end_date = '2013-10-20' # date | Filter Bill records for those whose bills have been sent before the specified date (optional)
    last_sent_start_date = '2013-10-20' # date | Filter Bill records for those whose bills have been sent after the specified date (optional)
    limit = 56 # int | A limit on the number of Bill records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Bill. The list will be filtered to include only the Bill records with the matching property. (optional)
    order = 'order_example' # str | Orders the Bill records by the given field. Default: `id(asc)`. (optional)
    originating_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a Bill. The list will be filtered to include only the Bill records with the matching property. (optional)
    overdue_only = True # bool | Filter Bill records to those that are overdue. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 56 # int | Allows matching search on invoice number. (optional)
    responsible_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a Bill. The list will be filtered to include only the Bill records with the matching property. (optional)
    state = 'state_example' # str | Filter Bill records to those in a given state. (optional)
    status = 'status_example' # str | Filter Bill records to those with particular payment status. (optional)
    type = 'type_example' # str | Filter Bill records to those of a specific type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Bill records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Bills
        api_response = api_instance.bill_index(x_api_version=x_api_version, client_id=client_id, created_since=created_since, custom_field_values=custom_field_values, due_after=due_after, due_at=due_at, due_before=due_before, fields=fields, ids=ids, issued_after=issued_after, issued_before=issued_before, last_sent_end_date=last_sent_end_date, last_sent_start_date=last_sent_start_date, limit=limit, matter_id=matter_id, order=order, originating_attorney_id=originating_attorney_id, overdue_only=overdue_only, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, state=state, status=status, type=type, updated_since=updated_since)
        print("The response of BillsApi->bill_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->bill_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **client_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Bill records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Bill records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **custom_field_values** | **str**| Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60;  | [optional] 
 **due_after** | **date**| Filter Bill records to those that have a &#x60;due_date&#x60; after the one provided (Expects an ISO-8601 date). | [optional] 
 **due_at** | **date**| Filter Bill records to those that have a specific &#x60;due_date&#x60; (Expects an ISO-8601 date). | [optional] 
 **due_before** | **date**| Filter Bill records to those that have a &#x60;due_date&#x60; before the one provided (Expects an ISO-8601 date). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Bill records to those having the specified unique identifiers. | [optional] 
 **issued_after** | **date**| Filter Bill records to those that have an &#x60;issue_date&#x60; after the one provided (Expects an ISO-8601 date). | [optional] 
 **issued_before** | **date**| Filter Bill records to those that have an &#x60;issue_date&#x60; before the one provided (Expects an ISO-8601 date). | [optional] 
 **last_sent_end_date** | **date**| Filter Bill records for those whose bills have been sent before the specified date | [optional] 
 **last_sent_start_date** | **date**| Filter Bill records for those whose bills have been sent after the specified date | [optional] 
 **limit** | **int**| A limit on the number of Bill records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Bill. The list will be filtered to include only the Bill records with the matching property. | [optional] 
 **order** | **str**| Orders the Bill records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **originating_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Bill. The list will be filtered to include only the Bill records with the matching property. | [optional] 
 **overdue_only** | **bool**| Filter Bill records to those that are overdue. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **int**| Allows matching search on invoice number. | [optional] 
 **responsible_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Bill. The list will be filtered to include only the Bill records with the matching property. | [optional] 
 **state** | **str**| Filter Bill records to those in a given state. | [optional] 
 **status** | **str**| Filter Bill records to those with particular payment status. | [optional] 
 **type** | **str**| Filter Bill records to those of a specific type. | [optional] 
 **updated_since** | **datetime**| Filter Bill records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**BillList**](BillList.md)

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

# **bill_preview**
> bill_preview(id)

Returns the pre-rendered html for the Bill

This endpoint returns a pre-rendered HTML object that you can use to view a preview of your bills. The HTML provided contains all of the CSS rules it requires to show the bill correctly, as well as the DOCTYPE setting it requires. It's best to use an iframe, or similar object, to render the results of this endpoint. 

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
    api_instance = openapi_client.BillsApi(api_client)
    id = 56 # int | The unique identifier for the Bill.

    try:
        # Returns the pre-rendered html for the Bill
        api_instance.bill_preview(id)
    except Exception as e:
        print("Exception when calling BillsApi->bill_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Bill. | 

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
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bill_show**
> BillShow bill_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields, navigation_next=navigation_next, navigation_previous=navigation_previous)

Return the data for a single Bill

Outlines the parameters, optional and required, used when requesting the data for a single Bill

### Example


```python
import openapi_client
from openapi_client.models.bill_show import BillShow
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
    api_instance = openapi_client.BillsApi(api_client)
    id = 56 # int | The unique identifier for the Bill.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    navigation_next = 56 # int | The id of the next *Bill* available for viewing (optional)
    navigation_previous = 56 # int | The id of the previous *Bill* available for viewing (optional)

    try:
        # Return the data for a single Bill
        api_response = api_instance.bill_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields, navigation_next=navigation_next, navigation_previous=navigation_previous)
        print("The response of BillsApi->bill_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->bill_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Bill. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **navigation_next** | **int**| The id of the next *Bill* available for viewing | [optional] 
 **navigation_previous** | **int**| The id of the previous *Bill* available for viewing | [optional] 

### Return type

[**BillShow**](BillShow.md)

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

# **bill_update**
> BillShow bill_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, bill_update_request=bill_update_request)

Update a single Bill

Outlines the parameters and data fields used when updating a single Bill

### Example


```python
import openapi_client
from openapi_client.models.bill_show import BillShow
from openapi_client.models.bill_update_request import BillUpdateRequest
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
    api_instance = openapi_client.BillsApi(api_client)
    id = 56 # int | The unique identifier for the Bill.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    bill_update_request = openapi_client.BillUpdateRequest() # BillUpdateRequest | Request Body for Bills (optional)

    try:
        # Update a single Bill
        api_response = api_instance.bill_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, bill_update_request=bill_update_request)
        print("The response of BillsApi->bill_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->bill_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Bill. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **bill_update_request** | [**BillUpdateRequest**](BillUpdateRequest.md)| Request Body for Bills | [optional] 

### Return type

[**BillShow**](BillShow.md)

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

