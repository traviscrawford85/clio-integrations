# openapi_client.ConversationsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_index**](ConversationsApi.md#conversation_index) | **GET** /conversations.json | Return the data for all Conversations
[**conversation_show**](ConversationsApi.md#conversation_show) | **GET** /conversations/{id}.json | Return the data for a single Conversation
[**conversation_update**](ConversationsApi.md#conversation_update) | **PATCH** /conversations/{id}.json | Update a single Conversation


# **conversation_index**
> ConversationList conversation_index(x_api_version=x_api_version, archived=archived, contact_id=contact_id, created_since=created_since, var_date=var_date, fields=fields, for_user=for_user, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, read_status=read_status, time_entries=time_entries, updated_since=updated_since)

Return the data for all Conversations

Outlines the parameters, optional and required, used when requesting the data for all Conversations

### Example


```python
import openapi_client
from openapi_client.models.conversation_list import ConversationList
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
    api_instance = openapi_client.ConversationsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    archived = True # bool | Filter archived Conversation records. (optional)
    contact_id = 56 # int | Filter Conversation records for the contact. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Conversation records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    var_date = '2013-10-20' # date | Filter Conversation records created on a given date. (Expects an ISO-8601 date). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    for_user = True # bool | If set to true, filter Conversation records accessible to any groups of the user. Note that the user may not be member of the conversations.  If set to false, filter Conversation records of which the user is a member.  (optional)
    ids = 56 # int | Filter Conversation records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Conversation records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. Use the keyword `null` to match those without a Conversation. The list will be filtered to include only the Conversation records with the matching property. (optional)
    order = 'order_example' # str | Orders the Conversation records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    read_status = True # bool | Filter Conversation records to those which have been read. (optional)
    time_entries = True # bool | Filter Conversation records to those with or without associated time entries. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Conversation records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Conversations
        api_response = api_instance.conversation_index(x_api_version=x_api_version, archived=archived, contact_id=contact_id, created_since=created_since, var_date=var_date, fields=fields, for_user=for_user, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, read_status=read_status, time_entries=time_entries, updated_since=updated_since)
        print("The response of ConversationsApi->conversation_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversation_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **archived** | **bool**| Filter archived Conversation records. | [optional] 
 **contact_id** | **int**| Filter Conversation records for the contact. | [optional] 
 **created_since** | **datetime**| Filter Conversation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **var_date** | **date**| Filter Conversation records created on a given date. (Expects an ISO-8601 date). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **for_user** | **bool**| If set to true, filter Conversation records accessible to any groups of the user. Note that the user may not be member of the conversations.  If set to false, filter Conversation records of which the user is a member.  | [optional] 
 **ids** | **int**| Filter Conversation records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Conversation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Conversation. The list will be filtered to include only the Conversation records with the matching property. | [optional] 
 **order** | **str**| Orders the Conversation records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **read_status** | **bool**| Filter Conversation records to those which have been read. | [optional] 
 **time_entries** | **bool**| Filter Conversation records to those with or without associated time entries. | [optional] 
 **updated_since** | **datetime**| Filter Conversation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ConversationList**](ConversationList.md)

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

# **conversation_show**
> ConversationShow conversation_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Conversation

Outlines the parameters, optional and required, used when requesting the data for a single Conversation

### Example


```python
import openapi_client
from openapi_client.models.conversation_show import ConversationShow
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
    api_instance = openapi_client.ConversationsApi(api_client)
    id = 56 # int | The unique identifier for the Conversation.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Conversation
        api_response = api_instance.conversation_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ConversationsApi->conversation_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversation_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Conversation. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ConversationShow**](ConversationShow.md)

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

# **conversation_update**
> ConversationShow conversation_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, conversation_update_request=conversation_update_request)

Update a single Conversation

Outlines the parameters and data fields used when updating a single Conversation

### Example


```python
import openapi_client
from openapi_client.models.conversation_show import ConversationShow
from openapi_client.models.conversation_update_request import ConversationUpdateRequest
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
    api_instance = openapi_client.ConversationsApi(api_client)
    id = 56 # int | The unique identifier for the Conversation.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    conversation_update_request = openapi_client.ConversationUpdateRequest() # ConversationUpdateRequest | Request Body for Conversations (optional)

    try:
        # Update a single Conversation
        api_response = api_instance.conversation_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, conversation_update_request=conversation_update_request)
        print("The response of ConversationsApi->conversation_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversation_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Conversation. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **conversation_update_request** | [**ConversationUpdateRequest**](ConversationUpdateRequest.md)| Request Body for Conversations | [optional] 

### Return type

[**ConversationShow**](ConversationShow.md)

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

