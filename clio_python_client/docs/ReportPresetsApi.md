# openapi_client.ReportPresetsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_preset_create**](ReportPresetsApi.md#report_preset_create) | **POST** /report_presets.json | Create a new ReportPreset
[**report_preset_destroy**](ReportPresetsApi.md#report_preset_destroy) | **DELETE** /report_presets/{id}.json | Delete a single ReportPreset
[**report_preset_generate_report**](ReportPresetsApi.md#report_preset_generate_report) | **POST** /report_presets/{id}/generate_report.json | Generate a new report for a given preset
[**report_preset_index**](ReportPresetsApi.md#report_preset_index) | **GET** /report_presets.json | Return the data for all ReportPresets
[**report_preset_show**](ReportPresetsApi.md#report_preset_show) | **GET** /report_presets/{id}.json | Return the data for a single ReportPreset
[**report_preset_update**](ReportPresetsApi.md#report_preset_update) | **PATCH** /report_presets/{id}.json | Update a single ReportPreset


# **report_preset_create**
> ReportPresetShow report_preset_create(x_api_version=x_api_version, fields=fields, report_preset_create_request=report_preset_create_request)

Create a new ReportPreset

Outlines the parameters and data fields used when creating a new ReportPreset

### Example


```python
import openapi_client
from openapi_client.models.report_preset_create_request import ReportPresetCreateRequest
from openapi_client.models.report_preset_show import ReportPresetShow
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
    api_instance = openapi_client.ReportPresetsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    report_preset_create_request = openapi_client.ReportPresetCreateRequest() # ReportPresetCreateRequest | Request Body for Report Presets (optional)

    try:
        # Create a new ReportPreset
        api_response = api_instance.report_preset_create(x_api_version=x_api_version, fields=fields, report_preset_create_request=report_preset_create_request)
        print("The response of ReportPresetsApi->report_preset_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportPresetsApi->report_preset_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **report_preset_create_request** | [**ReportPresetCreateRequest**](ReportPresetCreateRequest.md)| Request Body for Report Presets | [optional] 

### Return type

[**ReportPresetShow**](ReportPresetShow.md)

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

# **report_preset_destroy**
> report_preset_destroy(id, x_api_version=x_api_version)

Delete a single ReportPreset

Outlines the parameters, optional and required, used when deleting the record for a single ReportPreset

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
    api_instance = openapi_client.ReportPresetsApi(api_client)
    id = 56 # int | The unique identifier for the ReportPreset.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single ReportPreset
        api_instance.report_preset_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ReportPresetsApi->report_preset_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ReportPreset. | 
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

# **report_preset_generate_report**
> ReportShow report_preset_generate_report(id)

Generate a new report for a given preset

Generate a new report for a given preset

### Example


```python
import openapi_client
from openapi_client.models.report_show import ReportShow
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
    api_instance = openapi_client.ReportPresetsApi(api_client)
    id = 56 # int | The unique identifier for the ReportPreset.

    try:
        # Generate a new report for a given preset
        api_response = api_instance.report_preset_generate_report(id)
        print("The response of ReportPresetsApi->report_preset_generate_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportPresetsApi->report_preset_generate_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ReportPreset. | 

### Return type

[**ReportShow**](ReportShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_preset_index**
> ReportPresetList report_preset_index(x_api_version=x_api_version, category=category, created_since=created_since, fields=fields, has_schedule=has_schedule, ids=ids, limit=limit, order=order, output_format=output_format, page_token=page_token, query=query, schedule_frequency=schedule_frequency, updated_since=updated_since)

Return the data for all ReportPresets

Outlines the parameters, optional and required, used when requesting the data for all ReportPresets

### Example


```python
import openapi_client
from openapi_client.models.report_preset_list import ReportPresetList
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
    api_instance = openapi_client.ReportPresetsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    category = 'category_example' # str | Filters ReportPreset data by category. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ReportPreset records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    has_schedule = True # bool | Filters ReportPreset records to those that have or do not have a Report Schedule. (optional)
    ids = 56 # int | Filter ReportPreset records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of ReportPreset records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the ReportPreset records by the given field. Default: `id(asc)`. (optional)
    output_format = 'output_format_example' # str | Filters ReportPreset data by format. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for ReportPreset name. (optional)
    schedule_frequency = 'schedule_frequency_example' # str | Filters ReportPreset records to those that have a Report Schedule of the specified frequency. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ReportPreset records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all ReportPresets
        api_response = api_instance.report_preset_index(x_api_version=x_api_version, category=category, created_since=created_since, fields=fields, has_schedule=has_schedule, ids=ids, limit=limit, order=order, output_format=output_format, page_token=page_token, query=query, schedule_frequency=schedule_frequency, updated_since=updated_since)
        print("The response of ReportPresetsApi->report_preset_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportPresetsApi->report_preset_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **category** | **str**| Filters ReportPreset data by category. | [optional] 
 **created_since** | **datetime**| Filter ReportPreset records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **has_schedule** | **bool**| Filters ReportPreset records to those that have or do not have a Report Schedule. | [optional] 
 **ids** | **int**| Filter ReportPreset records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of ReportPreset records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the ReportPreset records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **output_format** | **str**| Filters ReportPreset data by format. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for ReportPreset name. | [optional] 
 **schedule_frequency** | **str**| Filters ReportPreset records to those that have a Report Schedule of the specified frequency. | [optional] 
 **updated_since** | **datetime**| Filter ReportPreset records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ReportPresetList**](ReportPresetList.md)

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

# **report_preset_show**
> ReportPresetShow report_preset_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single ReportPreset

Outlines the parameters, optional and required, used when requesting the data for a single ReportPreset

### Example


```python
import openapi_client
from openapi_client.models.report_preset_show import ReportPresetShow
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
    api_instance = openapi_client.ReportPresetsApi(api_client)
    id = 56 # int | The unique identifier for the ReportPreset.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single ReportPreset
        api_response = api_instance.report_preset_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ReportPresetsApi->report_preset_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportPresetsApi->report_preset_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ReportPreset. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ReportPresetShow**](ReportPresetShow.md)

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

# **report_preset_update**
> ReportPresetShow report_preset_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, report_preset_update_request=report_preset_update_request)

Update a single ReportPreset

Outlines the parameters and data fields used when updating a single ReportPreset

### Example


```python
import openapi_client
from openapi_client.models.report_preset_show import ReportPresetShow
from openapi_client.models.report_preset_update_request import ReportPresetUpdateRequest
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
    api_instance = openapi_client.ReportPresetsApi(api_client)
    id = 56 # int | The unique identifier for the ReportPreset.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    report_preset_update_request = openapi_client.ReportPresetUpdateRequest() # ReportPresetUpdateRequest | Request Body for Report Presets (optional)

    try:
        # Update a single ReportPreset
        api_response = api_instance.report_preset_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, report_preset_update_request=report_preset_update_request)
        print("The response of ReportPresetsApi->report_preset_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportPresetsApi->report_preset_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ReportPreset. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **report_preset_update_request** | [**ReportPresetUpdateRequest**](ReportPresetUpdateRequest.md)| Request Body for Report Presets | [optional] 

### Return type

[**ReportPresetShow**](ReportPresetShow.md)

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

