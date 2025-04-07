# openapi_client.FoldersApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_create**](FoldersApi.md#folder_create) | **POST** /folders.json | Create a new Folder
[**folder_destroy**](FoldersApi.md#folder_destroy) | **DELETE** /folders/{id}.json | Delete a single Folder
[**folder_index**](FoldersApi.md#folder_index) | **GET** /folders.json | Return the data for all Folders
[**folder_list**](FoldersApi.md#folder_list) | **GET** /folders/list.json | Return the data of the contents of a Folder
[**folder_show**](FoldersApi.md#folder_show) | **GET** /folders/{id}.json | Return the data for a single Folder
[**folder_update**](FoldersApi.md#folder_update) | **PATCH** /folders/{id}.json | Update a single Folder


# **folder_create**
> FolderShow folder_create(x_api_version=x_api_version, fields=fields, folder_create_request=folder_create_request)

Create a new Folder

Create a Folder to an existing folder. 

### Example


```python
import openapi_client
from openapi_client.models.folder_create_request import FolderCreateRequest
from openapi_client.models.folder_show import FolderShow
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
    api_instance = openapi_client.FoldersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    folder_create_request = openapi_client.FolderCreateRequest() # FolderCreateRequest | Request Body for Folders (optional)

    try:
        # Create a new Folder
        api_response = api_instance.folder_create(x_api_version=x_api_version, fields=fields, folder_create_request=folder_create_request)
        print("The response of FoldersApi->folder_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **folder_create_request** | [**FolderCreateRequest**](FolderCreateRequest.md)| Request Body for Folders | [optional] 

### Return type

[**FolderShow**](FolderShow.md)

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

# **folder_destroy**
> folder_destroy(id, x_api_version=x_api_version)

Delete a single Folder

Deleting a Folder using this method will move it to the trash instead of permanently deleting it. Trashed Folders are permanently deleted after 30 days. The following errors may be returned:  - `400 Bad Request`: The Folder cannot be trashed. The `type` of the error will be `DeleteFailed` and the `message` of the error will be one of the following:   - `Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash some of the items inside it before trying again.`   - `Delete failed: This item contains locked items and cannot be deleted.`   - `Delete failed: The root folder cannot be trashed` - `409 Conflict`: The Folder (or one of its descendants) is currently being modified by another request, and cannot be trashed. 

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
    api_instance = openapi_client.FoldersApi(api_client)
    id = 56 # int | The unique identifier for the Folder.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Folder
        api_instance.folder_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Folder. | 
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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_index**
> FolderList folder_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, document_category_id=document_category_id, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, ids=ids, include_deleted=include_deleted, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, query=query, scope=scope, updated_since=updated_since)

Return the data for all Folders

Outlines the parameters, optional and required, used when requesting the data for all Folders

### Example


```python
import openapi_client
from openapi_client.models.folder_list import FolderList
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
    api_instance = openapi_client.FoldersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Folder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    document_category_id = 56 # int | The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. (optional)
    external_property_name = 'external_property_name_example' # str | Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name`  (optional)
    external_property_value = 'external_property_value_example' # str | Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value`  (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Folder records to those having the specified unique identifiers. (optional)
    include_deleted = True # bool | Allow trashed Folder record to be included. (optional)
    limit = 56 # int | A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. (optional)
    order = 'order_example' # str | Orders the Folder records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    parent_id = 56 # int | The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword `null` is not valid for this field. If no Folder is provided, it will default to the account's root Folder.  When returning the data for all Folders, use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.  (optional)
    query = 'query_example' # str | Wildcard search for `name` matching the given string. (optional)
    scope = 'scope_example' # str | Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Folder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Folders
        api_response = api_instance.folder_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, document_category_id=document_category_id, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, ids=ids, include_deleted=include_deleted, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, query=query, scope=scope, updated_since=updated_since)
        print("The response of FoldersApi->folder_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Folder records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **document_category_id** | **int**| The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. | [optional] 
 **external_property_name** | **str**| Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60;  | [optional] 
 **external_property_value** | **str**| Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60;  | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Folder records to those having the specified unique identifiers. | [optional] 
 **include_deleted** | **bool**| Allow trashed Folder record to be included. | [optional] 
 **limit** | **int**| A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. | [optional] 
 **order** | **str**| Orders the Folder records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **parent_id** | **int**| The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword &#x60;null&#x60; is not valid for this field. If no Folder is provided, it will default to the account&#39;s root Folder.  When returning the data for all Folders, use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.  | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching the given string. | [optional] 
 **scope** | **str**| Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;. | [optional] 
 **updated_since** | **datetime**| Filter Folder records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**FolderList**](FolderList.md)

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

# **folder_list**
> ItemList folder_list(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, document_category_id=document_category_id, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, ids=ids, include_deleted=include_deleted, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, query=query, scope=scope, show_uncompleted=show_uncompleted, updated_since=updated_since)

Return the data of the contents of a Folder

Return the data of the contents of a Folder. 

### Example


```python
import openapi_client
from openapi_client.models.item_list import ItemList
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
    api_instance = openapi_client.FoldersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Folder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    document_category_id = 56 # int | The unique identifier for a single DocumentCategory. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. (optional)
    external_property_name = 'external_property_name_example' # str | Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name`  (optional)
    external_property_value = 'external_property_value_example' # str | Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value`  (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Folder records to those having the specified unique identifiers. (optional)
    include_deleted = True # bool | Allow trashed Folder record to be included. (optional)
    limit = 56 # int | A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. (optional)
    order = 'order_example' # str | Orders the Folder records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    parent_id = 56 # int | The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword `null` is not valid for this field. If no Folder is provided, it will default to the account's root Folder.  When returning the data for all Folders, use the keyword `null` to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.  (optional)
    query = 'query_example' # str | Wildcard search for `name` matching the given string. (optional)
    scope = 'scope_example' # str | Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is `children`. (optional)
    show_uncompleted = True # bool | Allow Folder record being uploaded to be included. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Folder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data of the contents of a Folder
        api_response = api_instance.folder_list(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, document_category_id=document_category_id, external_property_name=external_property_name, external_property_value=external_property_value, fields=fields, ids=ids, include_deleted=include_deleted, limit=limit, matter_id=matter_id, order=order, page_token=page_token, parent_id=parent_id, query=query, scope=scope, show_uncompleted=show_uncompleted, updated_since=updated_since)
        print("The response of FoldersApi->folder_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Folder records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **document_category_id** | **int**| The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. | [optional] 
 **external_property_name** | **str**| Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60;  | [optional] 
 **external_property_value** | **str**| Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60;  | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Folder records to those having the specified unique identifiers. | [optional] 
 **include_deleted** | **bool**| Allow trashed Folder record to be included. | [optional] 
 **limit** | **int**| A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. | [optional] 
 **order** | **str**| Orders the Folder records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **parent_id** | **int**| The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword &#x60;null&#x60; is not valid for this field. If no Folder is provided, it will default to the account&#39;s root Folder.  When returning the data for all Folders, use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.  | [optional] 
 **query** | **str**| Wildcard search for &#x60;name&#x60; matching the given string. | [optional] 
 **scope** | **str**| Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;. | [optional] 
 **show_uncompleted** | **bool**| Allow Folder record being uploaded to be included. | [optional] 
 **updated_since** | **datetime**| Filter Folder records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ItemList**](ItemList.md)

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

# **folder_show**
> FolderShow folder_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Folder

Outlines the parameters, optional and required, used when requesting the data for a single Folder

### Example


```python
import openapi_client
from openapi_client.models.folder_show import FolderShow
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
    api_instance = openapi_client.FoldersApi(api_client)
    id = 56 # int | The unique identifier for the Folder.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Folder
        api_response = api_instance.folder_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of FoldersApi->folder_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Folder. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**FolderShow**](FolderShow.md)

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

# **folder_update**
> FolderShow folder_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, folder_update_request=folder_update_request)

Update a single Folder

Update Folder, move Folder to another Folder, and/or restore a trashed Folder. 

### Example


```python
import openapi_client
from openapi_client.models.folder_show import FolderShow
from openapi_client.models.folder_update_request import FolderUpdateRequest
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
    api_instance = openapi_client.FoldersApi(api_client)
    id = 56 # int | The unique identifier for the Folder.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    folder_update_request = openapi_client.FolderUpdateRequest() # FolderUpdateRequest | Request Body for Folders (optional)

    try:
        # Update a single Folder
        api_response = api_instance.folder_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, folder_update_request=folder_update_request)
        print("The response of FoldersApi->folder_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Folder. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **folder_update_request** | [**FolderUpdateRequest**](FolderUpdateRequest.md)| Request Body for Folders | [optional] 

### Return type

[**FolderShow**](FolderShow.md)

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

