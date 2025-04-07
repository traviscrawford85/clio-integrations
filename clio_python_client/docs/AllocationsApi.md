# openapi_client.AllocationsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocation_index**](AllocationsApi.md#allocation_index) | **GET** /allocations.json | Return the data for all Allocations
[**allocation_show**](AllocationsApi.md#allocation_show) | **GET** /allocations/{id}.json | Return the data for a single Allocation


# **allocation_index**
> AllocationList allocation_index(x_api_version=x_api_version, bill_id=bill_id, contact_id=contact_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, parent_type=parent_type, status=status, updated_since=updated_since)

Return the data for all Allocations

Outlines the parameters, optional and required, used when requesting the data for all Allocations

### Example


```python
import openapi_client
from openapi_client.models.allocation_list import AllocationList
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
    api_instance = openapi_client.AllocationsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    bill_id = 56 # int | The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Allocation records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Allocation records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Allocation records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property. (optional)
    order = 'order_example' # str | Orders the Allocation records by the given field. Default: `date(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    parent_id = 56 # int | ID of parent (either a Payment or CreditMemo) this allocation belongs to (optional)
    parent_type = 56 # int | Filter Allocation records based on whether the parent is a CreditMemo or a Payment. (optional)
    status = 'status_example' # str | Filter Allocation records to only those that are voided (`\"invalid\"`) or not voided (`\"valid\"`). (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Allocation records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Allocations
        api_response = api_instance.allocation_index(x_api_version=x_api_version, bill_id=bill_id, contact_id=contact_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, parent_type=parent_type, status=status, updated_since=updated_since)
        print("The response of AllocationsApi->allocation_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationsApi->allocation_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **bill_id** | **int**| The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Allocation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Allocation records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Allocation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property. | [optional] 
 **order** | **str**| Orders the Allocation records by the given field. Default: &#x60;date(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **parent_id** | **int**| ID of parent (either a Payment or CreditMemo) this allocation belongs to | [optional] 
 **parent_type** | **int**| Filter Allocation records based on whether the parent is a CreditMemo or a Payment. | [optional] 
 **status** | **str**| Filter Allocation records to only those that are voided (&#x60;\&quot;invalid\&quot;&#x60;) or not voided (&#x60;\&quot;valid\&quot;&#x60;). | [optional] 
 **updated_since** | **datetime**| Filter Allocation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**AllocationList**](AllocationList.md)

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

# **allocation_show**
> AllocationShow allocation_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Allocation

Outlines the parameters, optional and required, used when requesting the data for a single Allocation

### Example


```python
import openapi_client
from openapi_client.models.allocation_show import AllocationShow
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
    api_instance = openapi_client.AllocationsApi(api_client)
    id = 56 # int | The unique identifier for the Allocation.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Allocation
        api_response = api_instance.allocation_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of AllocationsApi->allocation_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationsApi->allocation_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Allocation. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**AllocationShow**](AllocationShow.md)

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

