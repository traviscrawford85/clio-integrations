# openapi_client.BankAccountsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_account_create**](BankAccountsApi.md#bank_account_create) | **POST** /bank_accounts.json | Create a new BankAccount
[**bank_account_destroy**](BankAccountsApi.md#bank_account_destroy) | **DELETE** /bank_accounts/{id}.json | Delete a single BankAccount
[**bank_account_index**](BankAccountsApi.md#bank_account_index) | **GET** /bank_accounts.json | Return the data for all BankAccounts
[**bank_account_show**](BankAccountsApi.md#bank_account_show) | **GET** /bank_accounts/{id}.json | Return the data for a single BankAccount
[**bank_account_update**](BankAccountsApi.md#bank_account_update) | **PATCH** /bank_accounts/{id}.json | Update a single BankAccount


# **bank_account_create**
> BankAccountShow bank_account_create(x_api_version=x_api_version, fields=fields, bank_account_create_request=bank_account_create_request)

Create a new BankAccount

Outlines the parameters and data fields used when creating a new BankAccount

### Example


```python
import openapi_client
from openapi_client.models.bank_account_create_request import BankAccountCreateRequest
from openapi_client.models.bank_account_show import BankAccountShow
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
    api_instance = openapi_client.BankAccountsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    bank_account_create_request = openapi_client.BankAccountCreateRequest() # BankAccountCreateRequest | Request Body for Bank Accounts (optional)

    try:
        # Create a new BankAccount
        api_response = api_instance.bank_account_create(x_api_version=x_api_version, fields=fields, bank_account_create_request=bank_account_create_request)
        print("The response of BankAccountsApi->bank_account_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_account_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **bank_account_create_request** | [**BankAccountCreateRequest**](BankAccountCreateRequest.md)| Request Body for Bank Accounts | [optional] 

### Return type

[**BankAccountShow**](BankAccountShow.md)

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

# **bank_account_destroy**
> bank_account_destroy(id, x_api_version=x_api_version)

Delete a single BankAccount

Outlines the parameters, optional and required, used when deleting the record for a single BankAccount

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
    api_instance = openapi_client.BankAccountsApi(api_client)
    id = 56 # int | The unique identifier for the BankAccount.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single BankAccount
        api_instance.bank_account_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_account_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the BankAccount. | 
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

# **bank_account_index**
> BankAccountList bank_account_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, show_empty_accounts=show_empty_accounts, type=type, updated_since=updated_since, user_id=user_id)

Return the data for all BankAccounts

Outlines the parameters, optional and required, used when requesting the data for all BankAccounts

### Example


```python
import openapi_client
from openapi_client.models.bank_account_list import BankAccountList
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
    api_instance = openapi_client.BankAccountsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter BankAccount records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter BankAccount records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of BankAccount records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the BankAccount records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    show_empty_accounts = True # bool | Filter BankAccount records to those having a zero or non zero balance. (optional)
    type = 'type_example' # str | Filter BankAccount records to those having a specific type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter BankAccount records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    user_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a BankAccount. The list will be filtered to include only the BankAccount records with the matching property. (optional)

    try:
        # Return the data for all BankAccounts
        api_response = api_instance.bank_account_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, show_empty_accounts=show_empty_accounts, type=type, updated_since=updated_since, user_id=user_id)
        print("The response of BankAccountsApi->bank_account_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_account_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter BankAccount records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter BankAccount records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of BankAccount records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the BankAccount records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **show_empty_accounts** | **bool**| Filter BankAccount records to those having a zero or non zero balance. | [optional] 
 **type** | **str**| Filter BankAccount records to those having a specific type. | [optional] 
 **updated_since** | **datetime**| Filter BankAccount records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **user_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BankAccount. The list will be filtered to include only the BankAccount records with the matching property. | [optional] 

### Return type

[**BankAccountList**](BankAccountList.md)

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

# **bank_account_show**
> BankAccountShow bank_account_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single BankAccount

Outlines the parameters, optional and required, used when requesting the data for a single BankAccount

### Example


```python
import openapi_client
from openapi_client.models.bank_account_show import BankAccountShow
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
    api_instance = openapi_client.BankAccountsApi(api_client)
    id = 56 # int | The unique identifier for the BankAccount.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single BankAccount
        api_response = api_instance.bank_account_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of BankAccountsApi->bank_account_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_account_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the BankAccount. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**BankAccountShow**](BankAccountShow.md)

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

# **bank_account_update**
> BankAccountShow bank_account_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, bank_account_update_request=bank_account_update_request)

Update a single BankAccount

Outlines the parameters and data fields used when updating a single BankAccount

### Example


```python
import openapi_client
from openapi_client.models.bank_account_show import BankAccountShow
from openapi_client.models.bank_account_update_request import BankAccountUpdateRequest
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
    api_instance = openapi_client.BankAccountsApi(api_client)
    id = 56 # int | The unique identifier for the BankAccount.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    bank_account_update_request = openapi_client.BankAccountUpdateRequest() # BankAccountUpdateRequest | Request Body for Bank Accounts (optional)

    try:
        # Update a single BankAccount
        api_response = api_instance.bank_account_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, bank_account_update_request=bank_account_update_request)
        print("The response of BankAccountsApi->bank_account_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_account_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the BankAccount. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **bank_account_update_request** | [**BankAccountUpdateRequest**](BankAccountUpdateRequest.md)| Request Body for Bank Accounts | [optional] 

### Return type

[**BankAccountShow**](BankAccountShow.md)

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

