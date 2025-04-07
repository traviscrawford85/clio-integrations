# openapi_client.ContactsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_create**](ContactsApi.md#contact_create) | **POST** /contacts.json | Create a new Contact
[**contact_destroy**](ContactsApi.md#contact_destroy) | **DELETE** /contacts/{id}.json | Delete a single Contact
[**contact_index**](ContactsApi.md#contact_index) | **GET** /contacts.json | Return the data for all Contacts
[**contact_show**](ContactsApi.md#contact_show) | **GET** /contacts/{id}.json | Return the data for a single Contact
[**contact_update**](ContactsApi.md#contact_update) | **PATCH** /contacts/{id}.json | Update a single Contact


# **contact_create**
> ContactShow contact_create(x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, contact_create_request=contact_create_request)

Create a new Contact

Outlines the parameters and data fields used when creating a new Contact

### Example


```python
import openapi_client
from openapi_client.models.contact_create_request import ContactCreateRequest
from openapi_client.models.contact_show import ContactShow
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
    api_instance = openapi_client.ContactsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    custom_field_ids = 56 # int | Filter Contact's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    contact_create_request = openapi_client.ContactCreateRequest() # ContactCreateRequest | Request Body for Contacts (optional)

    try:
        # Create a new Contact
        api_response = api_instance.contact_create(x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, contact_create_request=contact_create_request)
        print("The response of ContactsApi->contact_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contact_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **custom_field_ids** | **int**| Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **contact_create_request** | [**ContactCreateRequest**](ContactCreateRequest.md)| Request Body for Contacts | [optional] 

### Return type

[**ContactShow**](ContactShow.md)

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

# **contact_destroy**
> contact_destroy(id, x_api_version=x_api_version)

Delete a single Contact

Outlines the parameters, optional and required, used when deleting the record for a single Contact

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
    api_instance = openapi_client.ContactsApi(api_client)
    id = 56 # int | The unique identifier for the Contact.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Contact
        api_instance.contact_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ContactsApi->contact_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Contact. | 
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

# **contact_index**
> ContactList contact_index(x_api_version=x_api_version, client_only=client_only, clio_connect_only=clio_connect_only, created_since=created_since, custom_field_ids=custom_field_ids, custom_field_values=custom_field_values, email_only=email_only, exclude_ids=exclude_ids, fields=fields, ids=ids, initial=initial, limit=limit, order=order, page_token=page_token, query=query, shared_resource_id=shared_resource_id, type=type, updated_since=updated_since)

Return the data for all Contacts

Outlines the parameters, optional and required, used when requesting the data for all Contacts

### Example


```python
import openapi_client
from openapi_client.models.contact_list import ContactList
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
    api_instance = openapi_client.ContactsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    client_only = True # bool | Filter Contact records to those that are clients. (optional)
    clio_connect_only = True # bool | Filter Contact records to those that are Clio Connect users. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Contact records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    custom_field_ids = 56 # int | Filter Contact's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    custom_field_values = 'custom_field_values_example' # str | Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]`  (optional)
    email_only = True # bool | Filter Contact records to those that have email addresses. (optional)
    exclude_ids = 56 # int | Filter Contact records to those who are not included in the given list of unique identifiers. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Contact records to those having the specified unique identifiers. (optional)
    initial = 'initial_example' # str | Filter Contact records to those where the last name or company name start with the given initial. (optional)
    limit = 56 # int | A limit on the number of Contact records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the Contact records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for name, title, email address, address, phone number, web site, instant messenger address, custom fields, related matter name, or company name matching a given string.  (optional)
    shared_resource_id = 56 # int | Filter Contact records to those that currently have access to a given shared resource. (optional)
    type = 'type_example' # str | Filter Contact records to those that match the given type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Contact records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Contacts
        api_response = api_instance.contact_index(x_api_version=x_api_version, client_only=client_only, clio_connect_only=clio_connect_only, created_since=created_since, custom_field_ids=custom_field_ids, custom_field_values=custom_field_values, email_only=email_only, exclude_ids=exclude_ids, fields=fields, ids=ids, initial=initial, limit=limit, order=order, page_token=page_token, query=query, shared_resource_id=shared_resource_id, type=type, updated_since=updated_since)
        print("The response of ContactsApi->contact_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contact_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **client_only** | **bool**| Filter Contact records to those that are clients. | [optional] 
 **clio_connect_only** | **bool**| Filter Contact records to those that are Clio Connect users. | [optional] 
 **created_since** | **datetime**| Filter Contact records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **custom_field_ids** | **int**| Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **custom_field_values** | **str**| Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60;  | [optional] 
 **email_only** | **bool**| Filter Contact records to those that have email addresses. | [optional] 
 **exclude_ids** | **int**| Filter Contact records to those who are not included in the given list of unique identifiers. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Contact records to those having the specified unique identifiers. | [optional] 
 **initial** | **str**| Filter Contact records to those where the last name or company name start with the given initial. | [optional] 
 **limit** | **int**| A limit on the number of Contact records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the Contact records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for name, title, email address, address, phone number, web site, instant messenger address, custom fields, related matter name, or company name matching a given string.  | [optional] 
 **shared_resource_id** | **int**| Filter Contact records to those that currently have access to a given shared resource. | [optional] 
 **type** | **str**| Filter Contact records to those that match the given type. | [optional] 
 **updated_since** | **datetime**| Filter Contact records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ContactList**](ContactList.md)

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

# **contact_show**
> ContactShow contact_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields)

Return the data for a single Contact

Outlines the parameters, optional and required, used when requesting the data for a single Contact

### Example


```python
import openapi_client
from openapi_client.models.contact_show import ContactShow
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
    api_instance = openapi_client.ContactsApi(api_client)
    id = 56 # int | The unique identifier for the Contact.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    custom_field_ids = 56 # int | Filter Contact's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Contact
        api_response = api_instance.contact_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields)
        print("The response of ContactsApi->contact_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contact_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Contact. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **custom_field_ids** | **int**| Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ContactShow**](ContactShow.md)

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

# **contact_update**
> ContactShow contact_update(id, if_match=if_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, contact_update_request=contact_update_request)

Update a single Contact

Outlines the parameters and data fields used when updating a single Contact

### Example


```python
import openapi_client
from openapi_client.models.contact_show import ContactShow
from openapi_client.models.contact_update_request import ContactUpdateRequest
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
    api_instance = openapi_client.ContactsApi(api_client)
    id = 56 # int | The unique identifier for the Contact.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    custom_field_ids = 56 # int | Filter Contact's custom_field_values to only include values for the given custom field unique identifiers. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    contact_update_request = openapi_client.ContactUpdateRequest() # ContactUpdateRequest | Request Body for Contacts (optional)

    try:
        # Update a single Contact
        api_response = api_instance.contact_update(id, if_match=if_match, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, contact_update_request=contact_update_request)
        print("The response of ContactsApi->contact_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contact_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Contact. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **custom_field_ids** | **int**| Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **contact_update_request** | [**ContactUpdateRequest**](ContactUpdateRequest.md)| Request Body for Contacts | [optional] 

### Return type

[**ContactShow**](ContactShow.md)

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

