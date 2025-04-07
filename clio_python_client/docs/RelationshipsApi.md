# openapi_client.RelationshipsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relationship_create**](RelationshipsApi.md#relationship_create) | **POST** /relationships.json | Create a new Relationship
[**relationship_destroy**](RelationshipsApi.md#relationship_destroy) | **DELETE** /relationships/{id}.json | Delete a single Relationship
[**relationship_index**](RelationshipsApi.md#relationship_index) | **GET** /relationships.json | Return the data for all Relationships
[**relationship_show**](RelationshipsApi.md#relationship_show) | **GET** /relationships/{id}.json | Return the data for a single Relationship
[**relationship_update**](RelationshipsApi.md#relationship_update) | **PATCH** /relationships/{id}.json | Update a single Relationship


# **relationship_create**
> RelationshipShow relationship_create(x_api_version=x_api_version, fields=fields, relationship_create_request=relationship_create_request)

Create a new Relationship

Outlines the parameters and data fields used when creating a new Relationship

### Example


```python
import openapi_client
from openapi_client.models.relationship_create_request import RelationshipCreateRequest
from openapi_client.models.relationship_show import RelationshipShow
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
    api_instance = openapi_client.RelationshipsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    relationship_create_request = openapi_client.RelationshipCreateRequest() # RelationshipCreateRequest | Request Body for Relationships (optional)

    try:
        # Create a new Relationship
        api_response = api_instance.relationship_create(x_api_version=x_api_version, fields=fields, relationship_create_request=relationship_create_request)
        print("The response of RelationshipsApi->relationship_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipsApi->relationship_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **relationship_create_request** | [**RelationshipCreateRequest**](RelationshipCreateRequest.md)| Request Body for Relationships | [optional] 

### Return type

[**RelationshipShow**](RelationshipShow.md)

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

# **relationship_destroy**
> relationship_destroy(id, x_api_version=x_api_version)

Delete a single Relationship

Outlines the parameters, optional and required, used when deleting the record for a single Relationship

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
    api_instance = openapi_client.RelationshipsApi(api_client)
    id = 56 # int | The unique identifier for the Relationship.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single Relationship
        api_instance.relationship_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling RelationshipsApi->relationship_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Relationship. | 
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

# **relationship_index**
> RelationshipList relationship_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, page_token=page_token, updated_since=updated_since)

Return the data for all Relationships

Outlines the parameters, optional and required, used when requesting the data for all Relationships

### Example


```python
import openapi_client
from openapi_client.models.relationship_list import RelationshipList
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
    api_instance = openapi_client.RelationshipsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    contact_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Relationship records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Relationship records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Relationship records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Relationship records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the Relationship records with the matching property. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Relationship records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Relationships
        api_response = api_instance.relationship_index(x_api_version=x_api_version, contact_id=contact_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, page_token=page_token, updated_since=updated_since)
        print("The response of RelationshipsApi->relationship_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipsApi->relationship_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **contact_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Relationship records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter Relationship records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Relationship records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Relationship records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Relationship records with the matching property. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **updated_since** | **datetime**| Filter Relationship records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**RelationshipList**](RelationshipList.md)

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

# **relationship_show**
> RelationshipShow relationship_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Relationship

Outlines the parameters, optional and required, used when requesting the data for a single Relationship

### Example


```python
import openapi_client
from openapi_client.models.relationship_show import RelationshipShow
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
    api_instance = openapi_client.RelationshipsApi(api_client)
    id = 56 # int | The unique identifier for the Relationship.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Relationship
        api_response = api_instance.relationship_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of RelationshipsApi->relationship_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipsApi->relationship_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Relationship. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**RelationshipShow**](RelationshipShow.md)

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

# **relationship_update**
> RelationshipShow relationship_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, relationship_create_request=relationship_create_request)

Update a single Relationship

Outlines the parameters and data fields used when updating a single Relationship

### Example


```python
import openapi_client
from openapi_client.models.relationship_create_request import RelationshipCreateRequest
from openapi_client.models.relationship_show import RelationshipShow
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
    api_instance = openapi_client.RelationshipsApi(api_client)
    id = 56 # int | The unique identifier for the Relationship.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    relationship_create_request = openapi_client.RelationshipCreateRequest() # RelationshipCreateRequest | Request Body for Relationships (optional)

    try:
        # Update a single Relationship
        api_response = api_instance.relationship_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, relationship_create_request=relationship_create_request)
        print("The response of RelationshipsApi->relationship_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipsApi->relationship_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Relationship. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **relationship_create_request** | [**RelationshipCreateRequest**](RelationshipCreateRequest.md)| Request Body for Relationships | [optional] 

### Return type

[**RelationshipShow**](RelationshipShow.md)

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

