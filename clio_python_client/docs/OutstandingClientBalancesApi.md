# openapi_client.OutstandingClientBalancesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outstanding_client_balance_index**](OutstandingClientBalancesApi.md#outstanding_client_balance_index) | **GET** /outstanding_client_balances.json | Return the data for all OutstandingClientBalances


# **outstanding_client_balance_index**
> OutstandingClientBalanceList outstanding_client_balance_index(x_api_version=x_api_version, contact_id=contact_id, fields=fields, last_paid_end_date=last_paid_end_date, last_paid_start_date=last_paid_start_date, limit=limit, newest_bill_due_end_date=newest_bill_due_end_date, newest_bill_due_start_date=newest_bill_due_start_date, originating_attorney_id=originating_attorney_id, page_token=page_token, responsible_attorney_id=responsible_attorney_id)

Return the data for all OutstandingClientBalances

Outlines the parameters, optional and required, used when requesting the data for all OutstandingClientBalances

### Example


```python
import openapi_client
from openapi_client.models.outstanding_client_balance_list import OutstandingClientBalanceList
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
    api_instance = openapi_client.OutstandingClientBalancesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. Use the keyword `null` to match those without a OutstandingClientBalance. The list will be filtered to include only the OutstandingClientBalance records with the matching property. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    last_paid_end_date = '2013-10-20' # date | Filter OutstandingClientBalance records for those whose bills have been paid before the specified date (optional)
    last_paid_start_date = '2013-10-20' # date | Filter OutstandingClientBalance records for those whose bills have been paid after the specified date (optional)
    limit = 56 # int | A limit on the number of OutstandingClientBalance records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    newest_bill_due_end_date = '2013-10-20' # date | Filter OutstandingClientBalance records for the contact's newest bill due date before the specified date (optional)
    newest_bill_due_start_date = '2013-10-20' # date | Filter OutstandingClientBalance records for the contact's newest bill due date after the specified date (optional)
    originating_attorney_id = 56 # int | Filters OutstandingClientBalance records to those with matters that have a matching originating attorney. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    responsible_attorney_id = 56 # int | Filter OutstandingClientBalance records to those with matters that have a matching responsible attorney (optional)

    try:
        # Return the data for all OutstandingClientBalances
        api_response = api_instance.outstanding_client_balance_index(x_api_version=x_api_version, contact_id=contact_id, fields=fields, last_paid_end_date=last_paid_end_date, last_paid_start_date=last_paid_start_date, limit=limit, newest_bill_due_end_date=newest_bill_due_end_date, newest_bill_due_start_date=newest_bill_due_start_date, originating_attorney_id=originating_attorney_id, page_token=page_token, responsible_attorney_id=responsible_attorney_id)
        print("The response of OutstandingClientBalancesApi->outstanding_client_balance_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutstandingClientBalancesApi->outstanding_client_balance_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a OutstandingClientBalance. The list will be filtered to include only the OutstandingClientBalance records with the matching property. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **last_paid_end_date** | **date**| Filter OutstandingClientBalance records for those whose bills have been paid before the specified date | [optional] 
 **last_paid_start_date** | **date**| Filter OutstandingClientBalance records for those whose bills have been paid after the specified date | [optional] 
 **limit** | **int**| A limit on the number of OutstandingClientBalance records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **newest_bill_due_end_date** | **date**| Filter OutstandingClientBalance records for the contact&#39;s newest bill due date before the specified date | [optional] 
 **newest_bill_due_start_date** | **date**| Filter OutstandingClientBalance records for the contact&#39;s newest bill due date after the specified date | [optional] 
 **originating_attorney_id** | **int**| Filters OutstandingClientBalance records to those with matters that have a matching originating attorney. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **responsible_attorney_id** | **int**| Filter OutstandingClientBalance records to those with matters that have a matching responsible attorney | [optional] 

### Return type

[**OutstandingClientBalanceList**](OutstandingClientBalanceList.md)

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

