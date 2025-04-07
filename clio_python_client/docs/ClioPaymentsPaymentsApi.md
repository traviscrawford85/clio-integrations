# openapi_client.ClioPaymentsPaymentsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clio_payments_payment_index**](ClioPaymentsPaymentsApi.md#clio_payments_payment_index) | **GET** /clio_payments/payments.json | Return the data for all ClioPaymentsPayments
[**clio_payments_payment_show**](ClioPaymentsPaymentsApi.md#clio_payments_payment_show) | **GET** /clio_payments/payments/{id}.json | Return the data for a single ClioPaymentsPayment


# **clio_payments_payment_index**
> ClioPaymentsPaymentList clio_payments_payment_index(x_api_version=x_api_version, bill_id=bill_id, contact_id=contact_id, fields=fields, ids=ids, limit=limit, page_token=page_token, state=state)

Return the data for all ClioPaymentsPayments

Outlines the parameters, optional and required, used when requesting the data for all ClioPaymentsPayments

### Example


```python
import openapi_client
from openapi_client.models.clio_payments_payment_list import ClioPaymentsPaymentList
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
    api_instance = openapi_client.ClioPaymentsPaymentsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    bill_id = 56 # int | Filter ClioPaymentsPayment records to those that are allocated to the specified bill. (optional)
    contact_id = 56 # int | Filter ClioPaymentsPayment records to those that are assigned to the specified contact. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter ClioPaymentsPayment records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of ClioPaymentsPayment records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    state = 'state_example' # str | Filter ClioPaymentsPayment records to those in a given state. (optional)

    try:
        # Return the data for all ClioPaymentsPayments
        api_response = api_instance.clio_payments_payment_index(x_api_version=x_api_version, bill_id=bill_id, contact_id=contact_id, fields=fields, ids=ids, limit=limit, page_token=page_token, state=state)
        print("The response of ClioPaymentsPaymentsApi->clio_payments_payment_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClioPaymentsPaymentsApi->clio_payments_payment_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **bill_id** | **int**| Filter ClioPaymentsPayment records to those that are allocated to the specified bill. | [optional] 
 **contact_id** | **int**| Filter ClioPaymentsPayment records to those that are assigned to the specified contact. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter ClioPaymentsPayment records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of ClioPaymentsPayment records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **state** | **str**| Filter ClioPaymentsPayment records to those in a given state. | [optional] 

### Return type

[**ClioPaymentsPaymentList**](ClioPaymentsPaymentList.md)

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

# **clio_payments_payment_show**
> ClioPaymentsPaymentShow clio_payments_payment_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single ClioPaymentsPayment

Outlines the parameters, optional and required, used when requesting the data for a single ClioPaymentsPayment

### Example


```python
import openapi_client
from openapi_client.models.clio_payments_payment_show import ClioPaymentsPaymentShow
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
    api_instance = openapi_client.ClioPaymentsPaymentsApi(api_client)
    id = 56 # int | The unique identifier for the ClioPaymentsPayment.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single ClioPaymentsPayment
        api_response = api_instance.clio_payments_payment_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ClioPaymentsPaymentsApi->clio_payments_payment_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClioPaymentsPaymentsApi->clio_payments_payment_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ClioPaymentsPayment. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ClioPaymentsPaymentShow**](ClioPaymentsPaymentShow.md)

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

