# openapi_client.BillingSettingsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_setting_show**](BillingSettingsApi.md#billing_setting_show) | **GET** /settings/billing.json | Return the billing settings


# **billing_setting_show**
> BillingSettingShow billing_setting_show(if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, duration=duration, fields=fields)

Return the billing settings

Outlines the parameters, optional and required, used when requesting the data for a single BillingSetting

### Example


```python
import openapi_client
from openapi_client.models.billing_setting_show import BillingSettingShow
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
    api_instance = openapi_client.BillingSettingsApi(api_client)
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    duration = 'duration_example' # str | Duration string for time rounding, conforming to the Chronic date parser. For example: '3h' or '2:15'. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the billing settings
        api_response = api_instance.billing_setting_show(if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, duration=duration, fields=fields)
        print("The response of BillingSettingsApi->billing_setting_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSettingsApi->billing_setting_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **duration** | **str**| Duration string for time rounding, conforming to the Chronic date parser. For example: &#39;3h&#39; or &#39;2:15&#39;. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**BillingSettingShow**](BillingSettingShow.md)

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

