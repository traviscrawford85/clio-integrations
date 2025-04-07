# openapi_client.LineItemsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**line_item_destroy**](LineItemsApi.md#line_item_destroy) | **DELETE** /line_items/{id}.json | Delete a single LineItem
[**line_item_index**](LineItemsApi.md#line_item_index) | **GET** /line_items.json | Return the data for all LineItems
[**line_item_update**](LineItemsApi.md#line_item_update) | **PATCH** /line_items/{id}.json | Update a single LineItem


# **line_item_destroy**
> line_item_destroy(id, x_api_version=x_api_version)

Delete a single LineItem

A LineItem can not be deleted if it's Bill is not editable

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
    api_instance = openapi_client.LineItemsApi(api_client)
    id = 56 # int | The unique identifier for the LineItem.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single LineItem
        api_instance.line_item_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling LineItemsApi->line_item_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the LineItem. | 
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

# **line_item_index**
> LineItemList line_item_index(x_api_version=x_api_version, activity_id=activity_id, bill_id=bill_id, created_since=created_since, display=display, exclude_ids=exclude_ids, fields=fields, group_ordering=group_ordering, ids=ids, kind=kind, limit=limit, matter_id=matter_id, page_token=page_token, query=query, updated_since=updated_since)

Return the data for all LineItems

Outlines the parameters, optional and required, used when requesting the data for all LineItems

### Example


```python
import openapi_client
from openapi_client.models.line_item_list import LineItemList
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
    api_instance = openapi_client.LineItemsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    activity_id = 56 # int | The unique identifier for a single Activity. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property. (optional)
    bill_id = 56 # int | The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the LineItem records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter LineItem records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    display = True # bool | Set this flag to true to return only LineItems displayed on the bill. (optional)
    exclude_ids = 56 # int | Array containing LineItem identifiers that should be excluded from the query. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    group_ordering = 56 # int | Filters LineItem records to match given group ordering. (optional)
    ids = 56 # int | Filter LineItem records to those having the specified unique identifiers. (optional)
    kind = 'kind_example' # str | The kind of LineItem. (optional)
    limit = 56 # int | A limit on the number of LineItem records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `description` or `note` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter LineItem records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all LineItems
        api_response = api_instance.line_item_index(x_api_version=x_api_version, activity_id=activity_id, bill_id=bill_id, created_since=created_since, display=display, exclude_ids=exclude_ids, fields=fields, group_ordering=group_ordering, ids=ids, kind=kind, limit=limit, matter_id=matter_id, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of LineItemsApi->line_item_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LineItemsApi->line_item_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **activity_id** | **int**| The unique identifier for a single Activity. Use the keyword &#x60;null&#x60; to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property. | [optional] 
 **bill_id** | **int**| The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the LineItem records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter LineItem records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **display** | **bool**| Set this flag to true to return only LineItems displayed on the bill. | [optional] 
 **exclude_ids** | **int**| Array containing LineItem identifiers that should be excluded from the query. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **group_ordering** | **int**| Filters LineItem records to match given group ordering. | [optional] 
 **ids** | **int**| Filter LineItem records to those having the specified unique identifiers. | [optional] 
 **kind** | **str**| The kind of LineItem. | [optional] 
 **limit** | **int**| A limit on the number of LineItem records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;description&#x60; or &#x60;note&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter LineItem records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**LineItemList**](LineItemList.md)

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

# **line_item_update**
> LineItemShow line_item_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, line_item_update_request=line_item_update_request)

Update a single LineItem

Outlines the parameters and data fields used when updating a single LineItem

### Example


```python
import openapi_client
from openapi_client.models.line_item_show import LineItemShow
from openapi_client.models.line_item_update_request import LineItemUpdateRequest
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
    api_instance = openapi_client.LineItemsApi(api_client)
    id = 56 # int | The unique identifier for the LineItem.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    line_item_update_request = openapi_client.LineItemUpdateRequest() # LineItemUpdateRequest | Request Body for Line Items (optional)

    try:
        # Update a single LineItem
        api_response = api_instance.line_item_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, line_item_update_request=line_item_update_request)
        print("The response of LineItemsApi->line_item_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LineItemsApi->line_item_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the LineItem. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **line_item_update_request** | [**LineItemUpdateRequest**](LineItemUpdateRequest.md)| Request Body for Line Items | [optional] 

### Return type

[**LineItemShow**](LineItemShow.md)

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

