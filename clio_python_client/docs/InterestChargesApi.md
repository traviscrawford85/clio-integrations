# openapi_client.InterestChargesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interest_charge_destroy**](InterestChargesApi.md#interest_charge_destroy) | **DELETE** /interest_charges/{id}.json | Delete a single InterestCharge
[**interest_charge_index**](InterestChargesApi.md#interest_charge_index) | **GET** /interest_charges.json | Return the data for all InterestCharges


# **interest_charge_destroy**
> interest_charge_destroy(id, x_api_version=x_api_version)

Delete a single InterestCharge

Outlines the parameters, optional and required, used when deleting the record for a single InterestCharge

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
    api_instance = openapi_client.InterestChargesApi(api_client)
    id = 56 # int | The unique identifier for the InterestCharge.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single InterestCharge
        api_instance.interest_charge_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling InterestChargesApi->interest_charge_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the InterestCharge. | 
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

# **interest_charge_index**
> InterestChargeList interest_charge_index(x_api_version=x_api_version, bill_id=bill_id, created_since=created_since, exclude_ids=exclude_ids, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)

Return the data for all InterestCharges

Outlines the parameters, optional and required, used when requesting the data for all InterestCharges

### Example


```python
import openapi_client
from openapi_client.models.interest_charge_list import InterestChargeList
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
    api_instance = openapi_client.InterestChargesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    bill_id = 56 # int | The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the InterestCharge records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter InterestCharge records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    exclude_ids = 56 # int | Array containing *InterestCharge* identifiers that should be excluded from the query. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter InterestCharge records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of InterestCharge records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter InterestCharge records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all InterestCharges
        api_response = api_instance.interest_charge_index(x_api_version=x_api_version, bill_id=bill_id, created_since=created_since, exclude_ids=exclude_ids, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)
        print("The response of InterestChargesApi->interest_charge_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterestChargesApi->interest_charge_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **bill_id** | **int**| The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the InterestCharge records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter InterestCharge records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **exclude_ids** | **int**| Array containing *InterestCharge* identifiers that should be excluded from the query. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter InterestCharge records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of InterestCharge records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter InterestCharge records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**InterestChargeList**](InterestChargeList.md)

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

