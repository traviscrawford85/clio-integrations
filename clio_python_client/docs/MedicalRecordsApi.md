# openapi_client.MedicalRecordsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**medical_record_destroy**](MedicalRecordsApi.md#medical_record_destroy) | **DELETE** /medical_records/{id}.json | Destroying a Medical Record
[**medical_record_update**](MedicalRecordsApi.md#medical_record_update) | **PATCH** /medical_records/{id}.json | Updating a Medical Record


# **medical_record_destroy**
> medical_record_destroy(id, x_api_version=x_api_version)

Destroying a Medical Record

Outlines the parameters, optional and required, used when deleting the record for a single MedicalRecord

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
    api_instance = openapi_client.MedicalRecordsApi(api_client)
    id = 56 # int | The unique identifier for the MedicalRecord.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Destroying a Medical Record
        api_instance.medical_record_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling MedicalRecordsApi->medical_record_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the MedicalRecord. | 
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

# **medical_record_update**
> MedicalRecordShow medical_record_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, medical_record_update_request=medical_record_update_request)

Updating a Medical Record

Outlines the parameters and data fields used when updating a single MedicalRecord

### Example


```python
import openapi_client
from openapi_client.models.medical_record_show import MedicalRecordShow
from openapi_client.models.medical_record_update_request import MedicalRecordUpdateRequest
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
    api_instance = openapi_client.MedicalRecordsApi(api_client)
    id = 56 # int | The unique identifier for the MedicalRecord.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    medical_record_update_request = openapi_client.MedicalRecordUpdateRequest() # MedicalRecordUpdateRequest | Request Body for Medical Records (optional)

    try:
        # Updating a Medical Record
        api_response = api_instance.medical_record_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, medical_record_update_request=medical_record_update_request)
        print("The response of MedicalRecordsApi->medical_record_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicalRecordsApi->medical_record_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the MedicalRecord. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **medical_record_update_request** | [**MedicalRecordUpdateRequest**](MedicalRecordUpdateRequest.md)| Request Body for Medical Records | [optional] 

### Return type

[**MedicalRecordShow**](MedicalRecordShow.md)

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

