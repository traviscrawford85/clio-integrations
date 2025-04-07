# openapi_client.DocumentVersionsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_version_index**](DocumentVersionsApi.md#document_version_index) | **GET** /documents/{id}/versions.json | Return the data for all DocumentVersions


# **document_version_index**
> DocumentVersionList document_version_index(id, id2, x_api_version=x_api_version, fields=fields, fully_uploaded=fully_uploaded, limit=limit, page_token=page_token)

Return the data for all DocumentVersions

Outlines the parameters, optional and required, used when requesting the data for all DocumentVersions

### Example


```python
import openapi_client
from openapi_client.models.document_version_list import DocumentVersionList
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
    api_instance = openapi_client.DocumentVersionsApi(api_client)
    id = 56 # int | The unique identifier for the DocumentVersion.
    id2 = 56 # int | ID of the Document
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    fully_uploaded = True # bool | Filter DocumentVersion records to those with the given `fully_uploaded` status. (optional)
    limit = 56 # int | A limit on the number of DocumentVersion records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)

    try:
        # Return the data for all DocumentVersions
        api_response = api_instance.document_version_index(id, id2, x_api_version=x_api_version, fields=fields, fully_uploaded=fully_uploaded, limit=limit, page_token=page_token)
        print("The response of DocumentVersionsApi->document_version_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVersionsApi->document_version_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the DocumentVersion. | 
 **id2** | **int**| ID of the Document | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **fully_uploaded** | **bool**| Filter DocumentVersion records to those with the given &#x60;fully_uploaded&#x60; status. | [optional] 
 **limit** | **int**| A limit on the number of DocumentVersion records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 

### Return type

[**DocumentVersionList**](DocumentVersionList.md)

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

