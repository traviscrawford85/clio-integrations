# openapi_client.ExpenseCategoriesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expense_category_create**](ExpenseCategoriesApi.md#expense_category_create) | **POST** /expense_categories.json | Create a new ExpenseCategory
[**expense_category_destroy**](ExpenseCategoriesApi.md#expense_category_destroy) | **DELETE** /expense_categories/{id}.json | Delete a single ExpenseCategory
[**expense_category_index**](ExpenseCategoriesApi.md#expense_category_index) | **GET** /expense_categories.json | Return the data for all ExpenseCategories
[**expense_category_show**](ExpenseCategoriesApi.md#expense_category_show) | **GET** /expense_categories/{id}.json | Return the data for a single ExpenseCategory
[**expense_category_update**](ExpenseCategoriesApi.md#expense_category_update) | **PATCH** /expense_categories/{id}.json | Update a single ExpenseCategory
[**lauk_expense_category_index**](ExpenseCategoriesApi.md#lauk_expense_category_index) | **GET** /lauk_expense_categories.json | List Expense Categories


# **expense_category_create**
> ExpenseCategoryShow expense_category_create(x_api_version=x_api_version, fields=fields, expense_category_create_request=expense_category_create_request)

Create a new ExpenseCategory

Outlines the parameters and data fields used when creating a new ExpenseCategory

### Example


```python
import openapi_client
from openapi_client.models.expense_category_create_request import ExpenseCategoryCreateRequest
from openapi_client.models.expense_category_show import ExpenseCategoryShow
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
    api_instance = openapi_client.ExpenseCategoriesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    expense_category_create_request = openapi_client.ExpenseCategoryCreateRequest() # ExpenseCategoryCreateRequest | Request Body for Expense Categories (optional)

    try:
        # Create a new ExpenseCategory
        api_response = api_instance.expense_category_create(x_api_version=x_api_version, fields=fields, expense_category_create_request=expense_category_create_request)
        print("The response of ExpenseCategoriesApi->expense_category_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseCategoriesApi->expense_category_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **expense_category_create_request** | [**ExpenseCategoryCreateRequest**](ExpenseCategoryCreateRequest.md)| Request Body for Expense Categories | [optional] 

### Return type

[**ExpenseCategoryShow**](ExpenseCategoryShow.md)

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

# **expense_category_destroy**
> expense_category_destroy(id, x_api_version=x_api_version)

Delete a single ExpenseCategory

Outlines the parameters, optional and required, used when deleting the record for a single ExpenseCategory

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
    api_instance = openapi_client.ExpenseCategoriesApi(api_client)
    id = 56 # int | The unique identifier for the ExpenseCategory.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single ExpenseCategory
        api_instance.expense_category_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ExpenseCategoriesApi->expense_category_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ExpenseCategory. | 
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

# **expense_category_index**
> ExpenseCategoryList expense_category_index(x_api_version=x_api_version, created_since=created_since, entry_type=entry_type, fields=fields, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)

Return the data for all ExpenseCategories

Outlines the parameters, optional and required, used when requesting the data for all ExpenseCategories

### Example


```python
import openapi_client
from openapi_client.models.expense_category_list import ExpenseCategoryList
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
    api_instance = openapi_client.ExpenseCategoriesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ExpenseCategory records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    entry_type = 'entry_type_example' # str | Filter ExpenseCategory records to those that match the given type. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    limit = 56 # int | A limit on the number of ExpenseCategory records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the ExpenseCategory records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Allows matching search on expense category name. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ExpenseCategory records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all ExpenseCategories
        api_response = api_instance.expense_category_index(x_api_version=x_api_version, created_since=created_since, entry_type=entry_type, fields=fields, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of ExpenseCategoriesApi->expense_category_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseCategoriesApi->expense_category_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter ExpenseCategory records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **entry_type** | **str**| Filter ExpenseCategory records to those that match the given type. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **limit** | **int**| A limit on the number of ExpenseCategory records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the ExpenseCategory records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Allows matching search on expense category name. | [optional] 
 **updated_since** | **datetime**| Filter ExpenseCategory records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ExpenseCategoryList**](ExpenseCategoryList.md)

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

# **expense_category_show**
> ExpenseCategoryShow expense_category_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single ExpenseCategory

Outlines the parameters, optional and required, used when requesting the data for a single ExpenseCategory

### Example


```python
import openapi_client
from openapi_client.models.expense_category_show import ExpenseCategoryShow
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
    api_instance = openapi_client.ExpenseCategoriesApi(api_client)
    id = 56 # int | The unique identifier for the ExpenseCategory.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single ExpenseCategory
        api_response = api_instance.expense_category_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ExpenseCategoriesApi->expense_category_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseCategoriesApi->expense_category_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ExpenseCategory. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ExpenseCategoryShow**](ExpenseCategoryShow.md)

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

# **expense_category_update**
> ExpenseCategoryShow expense_category_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, expense_category_update_request=expense_category_update_request)

Update a single ExpenseCategory

Outlines the parameters and data fields used when updating a single ExpenseCategory

### Example


```python
import openapi_client
from openapi_client.models.expense_category_show import ExpenseCategoryShow
from openapi_client.models.expense_category_update_request import ExpenseCategoryUpdateRequest
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
    api_instance = openapi_client.ExpenseCategoriesApi(api_client)
    id = 56 # int | The unique identifier for the ExpenseCategory.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    expense_category_update_request = openapi_client.ExpenseCategoryUpdateRequest() # ExpenseCategoryUpdateRequest | Request Body for Expense Categories (optional)

    try:
        # Update a single ExpenseCategory
        api_response = api_instance.expense_category_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, expense_category_update_request=expense_category_update_request)
        print("The response of ExpenseCategoriesApi->expense_category_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseCategoriesApi->expense_category_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ExpenseCategory. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **expense_category_update_request** | [**ExpenseCategoryUpdateRequest**](ExpenseCategoryUpdateRequest.md)| Request Body for Expense Categories | [optional] 

### Return type

[**ExpenseCategoryShow**](ExpenseCategoryShow.md)

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

# **lauk_expense_category_index**
> LaukExpenseCategoryList lauk_expense_category_index(region, x_api_version=x_api_version, fields=fields, key=key, limit=limit, name=name, page_token=page_token, practice_area=practice_area)

List Expense Categories

Outlines the parameters, optional and required, used when requesting the data for all LaukExpenseCategories

### Example


```python
import openapi_client
from openapi_client.models.lauk_expense_category_list import LaukExpenseCategoryList
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
    api_instance = openapi_client.ExpenseCategoriesApi(api_client)
    region = 'region_example' # str | Sets the expense rate returned based on the region. If the region is set to London, it will return the London rate; otherwise, it will return the non-London rate.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    key = 'key_example' # str | Filter by key. (optional)
    limit = 56 # int | A limit on the number of LaukExpenseCategory records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    name = 'name_example' # str | Filter by expense name. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    practice_area = 'practice_area_example' # str | Filter by expense practice area. (optional)

    try:
        # List Expense Categories
        api_response = api_instance.lauk_expense_category_index(region, x_api_version=x_api_version, fields=fields, key=key, limit=limit, name=name, page_token=page_token, practice_area=practice_area)
        print("The response of ExpenseCategoriesApi->lauk_expense_category_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseCategoriesApi->lauk_expense_category_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| Sets the expense rate returned based on the region. If the region is set to London, it will return the London rate; otherwise, it will return the non-London rate. | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **key** | **str**| Filter by key. | [optional] 
 **limit** | **int**| A limit on the number of LaukExpenseCategory records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **name** | **str**| Filter by expense name. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **practice_area** | **str**| Filter by expense practice area. | [optional] 

### Return type

[**LaukExpenseCategoryList**](LaukExpenseCategoryList.md)

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

