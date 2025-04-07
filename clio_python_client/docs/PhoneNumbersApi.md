# openapi_client.PhoneNumbersApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**phone_number_index**](PhoneNumbersApi.md#phone_number_index) | **GET** /contacts/{contact_id}/phone_numbers.json | Return the data for all PhoneNumbers


# **phone_number_index**
> PhoneNumberList phone_number_index(contact_id, x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)

Return the data for all PhoneNumbers

Outlines the parameters, optional and required, used when requesting the data for all PhoneNumbers

### Example


```python
import openapi_client
from openapi_client.models.phone_number_list import PhoneNumberList
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
    api_instance = openapi_client.PhoneNumbersApi(api_client)
    contact_id = 56 # int | ID of the Contact
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter PhoneNumber records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter PhoneNumber records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of PhoneNumber records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter PhoneNumber records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all PhoneNumbers
        api_response = api_instance.phone_number_index(contact_id, x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, updated_since=updated_since)
        print("The response of PhoneNumbersApi->phone_number_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->phone_number_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| ID of the Contact | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter PhoneNumber records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter PhoneNumber records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of PhoneNumber records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter PhoneNumber records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**PhoneNumberList**](PhoneNumberList.md)

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

