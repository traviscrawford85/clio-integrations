# openapi_client.ReportsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_create**](ReportsApi.md#report_create) | **POST** /reports.json | Create a new Report
[**report_download**](ReportsApi.md#report_download) | **GET** /reports/{id}/download.json | Download the completed Report
[**report_index**](ReportsApi.md#report_index) | **GET** /reports.json | Return the data for all Reports
[**report_show**](ReportsApi.md#report_show) | **GET** /reports/{id}.json | Return the data for a single Report


# **report_create**
> ReportShow report_create(x_api_version=x_api_version, fields=fields, report_create_request=report_create_request)

Create a new Report

Outlines the parameters and data fields used when creating a new Report

### Example


```python
import openapi_client
from openapi_client.models.report_create_request import ReportCreateRequest
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
    api_instance = openapi_client.ReportsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    report_create_request = openapi_client.ReportCreateRequest() # ReportCreateRequest | Request Body for Reports (optional)

    try:
        # Create a new Report
        api_response = api_instance.report_create(x_api_version=x_api_version, fields=fields, report_create_request=report_create_request)
        print("The response of ReportsApi->report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **report_create_request** | [**ReportCreateRequest**](ReportCreateRequest.md)| Request Body for Reports | [optional] 

### Return type

[**ReportShow**](ReportShow.md)

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

# **report_download**
> report_download(id)

Download the completed Report

Download the completed Report

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
    api_instance = openapi_client.ReportsApi(api_client)
    id = 56 # int | The unique identifier for the Report.

    try:
        # Download the completed Report
        api_instance.report_download(id)
    except Exception as e:
        print("Exception when calling ReportsApi->report_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Report. | 

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
**303** | See Other |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_index**
> ReportList report_index(x_api_version=x_api_version, category=category, created_before=created_before, created_since=created_since, fields=fields, ids=ids, kind=kind, limit=limit, output_format=output_format, page_token=page_token, query=query, source=source, state=state, updated_since=updated_since)

Return the data for all Reports

Outlines the parameters, optional and required, used when requesting the data for all Reports

### Example


```python
import openapi_client
from openapi_client.models.report_list import ReportList
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
    api_instance = openapi_client.ReportsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    category = 'category_example' # str | Filters Report data by category. (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | Filters Report data by date. (Expects an ISO-8601 date). (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Report records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter Report records to those having the specified unique identifiers. (optional)
    kind = 'kind_example' # str | Filters Report data by kind. (optional)
    limit = 56 # int | A limit on the number of Report records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    output_format = 'output_format_example' # str | Filters Report data by format. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for Report name. (optional)
    source = 'source_example' # str | Filters Report data by source. (optional)
    state = 'state_example' # str | Filters Report data by state. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter Report records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Reports
        api_response = api_instance.report_index(x_api_version=x_api_version, category=category, created_before=created_before, created_since=created_since, fields=fields, ids=ids, kind=kind, limit=limit, output_format=output_format, page_token=page_token, query=query, source=source, state=state, updated_since=updated_since)
        print("The response of ReportsApi->report_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->report_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **category** | **str**| Filters Report data by category. | [optional] 
 **created_before** | **datetime**| Filters Report data by date. (Expects an ISO-8601 date). | [optional] 
 **created_since** | **datetime**| Filter Report records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter Report records to those having the specified unique identifiers. | [optional] 
 **kind** | **str**| Filters Report data by kind. | [optional] 
 **limit** | **int**| A limit on the number of Report records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **output_format** | **str**| Filters Report data by format. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for Report name. | [optional] 
 **source** | **str**| Filters Report data by source. | [optional] 
 **state** | **str**| Filters Report data by state. | [optional] 
 **updated_since** | **datetime**| Filter Report records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ReportList**](ReportList.md)

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

# **report_show**
> ReportShow report_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Report

Outlines the parameters, optional and required, used when requesting the data for a single Report

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
    api_instance = openapi_client.ReportsApi(api_client)
    id = 56 # int | The unique identifier for the Report.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Report
        api_response = api_instance.report_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ReportsApi->report_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->report_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Report. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

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
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

