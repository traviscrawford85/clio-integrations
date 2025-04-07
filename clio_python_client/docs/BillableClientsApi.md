# openapi_client.BillableClientsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billable_client_index**](BillableClientsApi.md#billable_client_index) | **GET** /billable_clients.json | Return the data for all BillableClients


# **billable_client_index**
> BillableClientList billable_client_index(x_api_version=x_api_version, client_id=client_id, custom_field_values=custom_field_values, end_date=end_date, fields=fields, limit=limit, matter_id=matter_id, originating_attorney_id=originating_attorney_id, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, start_date=start_date)

Return the data for all BillableClients

Outlines the parameters, optional and required, used when requesting the data for all BillableClients

### Example


```python
import openapi_client
from openapi_client.models.billable_client_list import BillableClientList
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
    api_instance = openapi_client.BillableClientsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    client_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableClient records with the matching property. (optional)
    custom_field_values = 'custom_field_values_example' # str | Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]`  (optional)
    end_date = '2013-10-20' # date | Filter BillableClient records to those that have Matters with unbilled Activities on or before this date (Expects an ISO-8601 date). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    limit = 56 # int | A limit on the number of BillableClient records to be returned. Limit can range between 1 and 25. Default: `25`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableClient records with the matching property. (optional)
    originating_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `display_number` or `number` or `description` matching a given string. (optional)
    responsible_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property. (optional)
    start_date = '2013-10-20' # date | Filter BillableClient records to those that have Matters with unbilled Activities on or after this date (Expects an ISO-8601 date). (optional)

    try:
        # Return the data for all BillableClients
        api_response = api_instance.billable_client_index(x_api_version=x_api_version, client_id=client_id, custom_field_values=custom_field_values, end_date=end_date, fields=fields, limit=limit, matter_id=matter_id, originating_attorney_id=originating_attorney_id, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, start_date=start_date)
        print("The response of BillableClientsApi->billable_client_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableClientsApi->billable_client_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **client_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableClient records with the matching property. | [optional] 
 **custom_field_values** | **str**| Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60;  | [optional] 
 **end_date** | **date**| Filter BillableClient records to those that have Matters with unbilled Activities on or before this date (Expects an ISO-8601 date). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **limit** | **int**| A limit on the number of BillableClient records to be returned. Limit can range between 1 and 25. Default: &#x60;25&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableClient records with the matching property. | [optional] 
 **originating_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;display_number&#x60; or &#x60;number&#x60; or &#x60;description&#x60; matching a given string. | [optional] 
 **responsible_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property. | [optional] 
 **start_date** | **date**| Filter BillableClient records to those that have Matters with unbilled Activities on or after this date (Expects an ISO-8601 date). | [optional] 

### Return type

[**BillableClientList**](BillableClientList.md)

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

