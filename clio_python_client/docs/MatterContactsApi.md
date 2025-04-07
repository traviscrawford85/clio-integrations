# openapi_client.MatterContactsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matter_contacts_index**](MatterContactsApi.md#matter_contacts_index) | **GET** /matters/{matter_id}/contacts.json | Return the related contact data for a single matter


# **matter_contacts_index**
> MatterContactsList matter_contacts_index(matter_id, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, limit=limit, order=order, page_token=page_token)

Return the related contact data for a single matter

Outlines the parameters, optional and required, used when requesting the data for all MatterContacts

### Example


```python
import openapi_client
from openapi_client.models.matter_contacts_list import MatterContactsList
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
    api_instance = openapi_client.MatterContactsApi(api_client)
    matter_id = 56 # int | Filters contact data by matter.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    custom_field_ids = 56 # int | IDs of custom fields to include in results. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    limit = 56 # int | A limit on the number of MatterContacts records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the MatterContacts records by the given field. Note that `id` is ordered by the `id` of the nested Relationship record. Default: `is_client(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)

    try:
        # Return the related contact data for a single matter
        api_response = api_instance.matter_contacts_index(matter_id, x_api_version=x_api_version, custom_field_ids=custom_field_ids, fields=fields, limit=limit, order=order, page_token=page_token)
        print("The response of MatterContactsApi->matter_contacts_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatterContactsApi->matter_contacts_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matter_id** | **int**| Filters contact data by matter. | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **custom_field_ids** | **int**| IDs of custom fields to include in results. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **limit** | **int**| A limit on the number of MatterContacts records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the MatterContacts records by the given field. Note that &#x60;id&#x60; is ordered by the &#x60;id&#x60; of the nested Relationship record. Default: &#x60;is_client(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 

### Return type

[**MatterContactsList**](MatterContactsList.md)

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

