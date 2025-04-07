# openapi_client.TrustRequestsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trust_request_create**](TrustRequestsApi.md#trust_request_create) | **POST** /trust_requests.json | Create a new TrustRequest


# **trust_request_create**
> TrustRequestShow trust_request_create(x_api_version=x_api_version, fields=fields, trust_request_create_request=trust_request_create_request)

Create a new TrustRequest

Outlines the parameters and data fields used when creating a new TrustRequest

### Example


```python
import openapi_client
from openapi_client.models.trust_request_create_request import TrustRequestCreateRequest
from openapi_client.models.trust_request_show import TrustRequestShow
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
    api_instance = openapi_client.TrustRequestsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    trust_request_create_request = openapi_client.TrustRequestCreateRequest() # TrustRequestCreateRequest | Request Body for Trust Requests (optional)

    try:
        # Create a new TrustRequest
        api_response = api_instance.trust_request_create(x_api_version=x_api_version, fields=fields, trust_request_create_request=trust_request_create_request)
        print("The response of TrustRequestsApi->trust_request_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustRequestsApi->trust_request_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **trust_request_create_request** | [**TrustRequestCreateRequest**](TrustRequestCreateRequest.md)| Request Body for Trust Requests | [optional] 

### Return type

[**TrustRequestShow**](TrustRequestShow.md)

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

