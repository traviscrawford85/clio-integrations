# openapi_client.JurisdictionsToTriggersApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jurisdictions_to_trigger_index**](JurisdictionsToTriggersApi.md#jurisdictions_to_trigger_index) | **GET** /court_rules/jurisdictions/{jurisdiction_id}/triggers.json | Return the data for all triggers
[**jurisdictions_to_trigger_show**](JurisdictionsToTriggersApi.md#jurisdictions_to_trigger_show) | **GET** /court_rules/jurisdictions/{jurisdiction_id}/triggers/{id}.json | Return the data for the trigger


# **jurisdictions_to_trigger_index**
> JurisdictionsToTriggerList jurisdictions_to_trigger_index(jurisdiction_id, x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, is_requirements_required=is_requirements_required, is_served=is_served, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)

Return the data for all triggers

Outlines the parameters, optional and required, used when requesting the data for all JurisdictionsToTriggers

### Example


```python
import openapi_client
from openapi_client.models.jurisdictions_to_trigger_list import JurisdictionsToTriggerList
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
    api_instance = openapi_client.JurisdictionsToTriggersApi(api_client)
    jurisdiction_id = 56 # int | The unique identifier for the Jurisdiction.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter JurisdictionsToTrigger records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter JurisdictionsToTrigger records to those having the specified unique identifiers. (optional)
    is_requirements_required = True # bool | Filter JurisdictionsToTrigger records to those which require addition requirements to be checked (usually specifying trigger time). (optional)
    is_served = True # bool | Filter JurisdictionsToTrigger records to those which require a service type to be selected. (optional)
    limit = 56 # int | A limit on the number of JurisdictionsToTrigger records to be returned. Limit can range between 1 and 1000. Default: `1000`. (optional)
    order = 'order_example' # str | Orders the JurisdictionsToTrigger records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `description` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter JurisdictionsToTrigger records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all triggers
        api_response = api_instance.jurisdictions_to_trigger_index(jurisdiction_id, x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, is_requirements_required=is_requirements_required, is_served=is_served, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of JurisdictionsToTriggersApi->jurisdictions_to_trigger_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JurisdictionsToTriggersApi->jurisdictions_to_trigger_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jurisdiction_id** | **int**| The unique identifier for the Jurisdiction. | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter JurisdictionsToTrigger records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter JurisdictionsToTrigger records to those having the specified unique identifiers. | [optional] 
 **is_requirements_required** | **bool**| Filter JurisdictionsToTrigger records to those which require addition requirements to be checked (usually specifying trigger time). | [optional] 
 **is_served** | **bool**| Filter JurisdictionsToTrigger records to those which require a service type to be selected. | [optional] 
 **limit** | **int**| A limit on the number of JurisdictionsToTrigger records to be returned. Limit can range between 1 and 1000. Default: &#x60;1000&#x60;. | [optional] 
 **order** | **str**| Orders the JurisdictionsToTrigger records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;description&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter JurisdictionsToTrigger records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**JurisdictionsToTriggerList**](JurisdictionsToTriggerList.md)

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

# **jurisdictions_to_trigger_show**
> JurisdictionsToTriggerShow jurisdictions_to_trigger_show(id, jurisdiction_id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for the trigger

Outlines the parameters, optional and required, used when requesting the data for a single JurisdictionsToTrigger

### Example


```python
import openapi_client
from openapi_client.models.jurisdictions_to_trigger_show import JurisdictionsToTriggerShow
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
    api_instance = openapi_client.JurisdictionsToTriggersApi(api_client)
    id = 56 # int | The unique identifier for the JurisdictionsToTrigger.
    jurisdiction_id = 56 # int | The unique identifier for the Jurisdiction.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for the trigger
        api_response = api_instance.jurisdictions_to_trigger_show(id, jurisdiction_id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of JurisdictionsToTriggersApi->jurisdictions_to_trigger_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JurisdictionsToTriggersApi->jurisdictions_to_trigger_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the JurisdictionsToTrigger. | 
 **jurisdiction_id** | **int**| The unique identifier for the Jurisdiction. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**JurisdictionsToTriggerShow**](JurisdictionsToTriggerShow.md)

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

