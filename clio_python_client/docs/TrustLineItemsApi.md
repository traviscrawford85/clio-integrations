# openapi_client.TrustLineItemsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trust_line_item_index**](TrustLineItemsApi.md#trust_line_item_index) | **GET** /trust_line_items.json | Return the data for all TrustLineItems
[**trust_line_item_update**](TrustLineItemsApi.md#trust_line_item_update) | **PATCH** /trust_line_items/{id}.json | Update a single TrustLineItem


# **trust_line_item_index**
> TrustLineItemList trust_line_item_index(x_api_version=x_api_version, bill_id=bill_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, updated_since=updated_since)

Return the data for all TrustLineItems

Outlines the parameters, optional and required, used when requesting the data for all TrustLineItems

### Example


```python
import openapi_client
from openapi_client.models.trust_line_item_list import TrustLineItemList
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
    api_instance = openapi_client.TrustLineItemsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    bill_id = 56 # int | The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the TrustLineItem records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TrustLineItem records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter TrustLineItem records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of TrustLineItem records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a TrustLineItem. The list will be filtered to include only the TrustLineItem records with the matching property. (optional)
    order = 'order_example' # str | Orders the TrustLineItem records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter TrustLineItem records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all TrustLineItems
        api_response = api_instance.trust_line_item_index(x_api_version=x_api_version, bill_id=bill_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, updated_since=updated_since)
        print("The response of TrustLineItemsApi->trust_line_item_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustLineItemsApi->trust_line_item_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **bill_id** | **int**| The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the TrustLineItem records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter TrustLineItem records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter TrustLineItem records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of TrustLineItem records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a TrustLineItem. The list will be filtered to include only the TrustLineItem records with the matching property. | [optional] 
 **order** | **str**| Orders the TrustLineItem records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter TrustLineItem records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**TrustLineItemList**](TrustLineItemList.md)

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

# **trust_line_item_update**
> TrustLineItemShow trust_line_item_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, trust_line_item_update_request=trust_line_item_update_request)

Update a single TrustLineItem

Outlines the parameters and data fields used when updating a single TrustLineItem

### Example


```python
import openapi_client
from openapi_client.models.trust_line_item_show import TrustLineItemShow
from openapi_client.models.trust_line_item_update_request import TrustLineItemUpdateRequest
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
    api_instance = openapi_client.TrustLineItemsApi(api_client)
    id = 56 # int | The unique identifier for the TrustLineItem.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    trust_line_item_update_request = openapi_client.TrustLineItemUpdateRequest() # TrustLineItemUpdateRequest | Request Body for Trust Line Items (optional)

    try:
        # Update a single TrustLineItem
        api_response = api_instance.trust_line_item_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, trust_line_item_update_request=trust_line_item_update_request)
        print("The response of TrustLineItemsApi->trust_line_item_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustLineItemsApi->trust_line_item_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the TrustLineItem. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **trust_line_item_update_request** | [**TrustLineItemUpdateRequest**](TrustLineItemUpdateRequest.md)| Request Body for Trust Line Items | [optional] 

### Return type

[**TrustLineItemShow**](TrustLineItemShow.md)

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

