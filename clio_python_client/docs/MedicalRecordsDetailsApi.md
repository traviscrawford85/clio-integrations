# openapi_client.MedicalRecordsDetailsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**medical_records_request_create**](MedicalRecordsDetailsApi.md#medical_records_request_create) | **POST** /medical_records_details.json | Creating a Medical Records Detail, Medical Records and Medical Bills
[**medical_records_request_destroy**](MedicalRecordsDetailsApi.md#medical_records_request_destroy) | **DELETE** /medical_records_details/{id}.json | Destroying a Medical Records Detail
[**medical_records_request_index**](MedicalRecordsDetailsApi.md#medical_records_request_index) | **GET** /medical_records_details.json | Return the data for all Medical Records Details
[**medical_records_request_show**](MedicalRecordsDetailsApi.md#medical_records_request_show) | **GET** /medical_records_details/{id}.json | Return the data for a single Medical Records Detail
[**medical_records_request_update**](MedicalRecordsDetailsApi.md#medical_records_request_update) | **PATCH** /medical_records_details/{id}.json | Updating a Medical Records Detail


# **medical_records_request_create**
> MedicalRecordsRequestShow medical_records_request_create(x_api_version=x_api_version, fields=fields, medical_records_request_create_request=medical_records_request_create_request)

Creating a Medical Records Detail, Medical Records and Medical Bills

This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical Bills. Medical Liens can also be created as a property under Medical Bills.  Reference the payload to see how the records are being passed in. 

### Example


```python
import openapi_client
from openapi_client.models.medical_records_request_create_request import MedicalRecordsRequestCreateRequest
from openapi_client.models.medical_records_request_show import MedicalRecordsRequestShow
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
    api_instance = openapi_client.MedicalRecordsDetailsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    medical_records_request_create_request = openapi_client.MedicalRecordsRequestCreateRequest() # MedicalRecordsRequestCreateRequest | Request Body for Medical Records Details (optional)

    try:
        # Creating a Medical Records Detail, Medical Records and Medical Bills
        api_response = api_instance.medical_records_request_create(x_api_version=x_api_version, fields=fields, medical_records_request_create_request=medical_records_request_create_request)
        print("The response of MedicalRecordsDetailsApi->medical_records_request_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicalRecordsDetailsApi->medical_records_request_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **medical_records_request_create_request** | [**MedicalRecordsRequestCreateRequest**](MedicalRecordsRequestCreateRequest.md)| Request Body for Medical Records Details | [optional] 

### Return type

[**MedicalRecordsRequestShow**](MedicalRecordsRequestShow.md)

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

# **medical_records_request_destroy**
> medical_records_request_destroy(id, x_api_version=x_api_version)

Destroying a Medical Records Detail

When a Medical Records Detail is destroyed, the child records, such as Medical Records, Medical Bills and Liens will also be destroyed in the same transaction. 

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
    api_instance = openapi_client.MedicalRecordsDetailsApi(api_client)
    id = 56 # int | The unique identifier for the Medical Records Detail.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Destroying a Medical Records Detail
        api_instance.medical_records_request_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling MedicalRecordsDetailsApi->medical_records_request_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Medical Records Detail. | 
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

# **medical_records_request_index**
> MedicalRecordsRequestList medical_records_request_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, treatment_end_date=treatment_end_date, treatment_start_date=treatment_start_date, updated_since=updated_since)

Return the data for all Medical Records Details

Outlines the parameters, optional and required, used when requesting the data for all Medical Records Details 

### Example


```python
import openapi_client
from openapi_client.models.medical_records_request_list import MedicalRecordsRequestList
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
    api_instance = openapi_client.MedicalRecordsDetailsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter MedicalRecordsRequest records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter MedicalRecordsRequest records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of Medical Records Detail records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    treatment_end_date = '2013-10-20T19:20:30+01:00' # datetime | Filters Medical Records data by treatment end date. (optional)
    treatment_start_date = '2013-10-20T19:20:30+01:00' # datetime | Filters Medical Records data by treatment start date. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter MedicalRecordsRequest records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all Medical Records Details
        api_response = api_instance.medical_records_request_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, page_token=page_token, treatment_end_date=treatment_end_date, treatment_start_date=treatment_start_date, updated_since=updated_since)
        print("The response of MedicalRecordsDetailsApi->medical_records_request_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicalRecordsDetailsApi->medical_records_request_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter MedicalRecordsRequest records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter MedicalRecordsRequest records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of Medical Records Detail records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **treatment_end_date** | **datetime**| Filters Medical Records data by treatment end date. | [optional] 
 **treatment_start_date** | **datetime**| Filters Medical Records data by treatment start date. | [optional] 
 **updated_since** | **datetime**| Filter MedicalRecordsRequest records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**MedicalRecordsRequestList**](MedicalRecordsRequestList.md)

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

# **medical_records_request_show**
> MedicalRecordsRequestShow medical_records_request_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single Medical Records Detail

Outlines the parameters, optional and required, used when requesting the data for a single Medical Records Details 

### Example


```python
import openapi_client
from openapi_client.models.medical_records_request_show import MedicalRecordsRequestShow
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
    api_instance = openapi_client.MedicalRecordsDetailsApi(api_client)
    id = 56 # int | The unique identifier for the Medical Records Detail.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single Medical Records Detail
        api_response = api_instance.medical_records_request_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of MedicalRecordsDetailsApi->medical_records_request_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicalRecordsDetailsApi->medical_records_request_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Medical Records Detail. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**MedicalRecordsRequestShow**](MedicalRecordsRequestShow.md)

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

# **medical_records_request_update**
> MedicalRecordsRequestShow medical_records_request_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, medical_records_request_update_request=medical_records_request_update_request)

Updating a Medical Records Detail

If there are records being passed into the Medical Records or Medical Bills parameter they will be treated as new records and new Medical Records / Medical Bills will be created. 

### Example


```python
import openapi_client
from openapi_client.models.medical_records_request_show import MedicalRecordsRequestShow
from openapi_client.models.medical_records_request_update_request import MedicalRecordsRequestUpdateRequest
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
    api_instance = openapi_client.MedicalRecordsDetailsApi(api_client)
    id = 56 # int | The unique identifier for the Medical Records Detail.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    medical_records_request_update_request = openapi_client.MedicalRecordsRequestUpdateRequest() # MedicalRecordsRequestUpdateRequest | Request Body for Medical Records Details (optional)

    try:
        # Updating a Medical Records Detail
        api_response = api_instance.medical_records_request_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, medical_records_request_update_request=medical_records_request_update_request)
        print("The response of MedicalRecordsDetailsApi->medical_records_request_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicalRecordsDetailsApi->medical_records_request_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the Medical Records Detail. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **medical_records_request_update_request** | [**MedicalRecordsRequestUpdateRequest**](MedicalRecordsRequestUpdateRequest.md)| Request Body for Medical Records Details | [optional] 

### Return type

[**MedicalRecordsRequestShow**](MedicalRecordsRequestShow.md)

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

