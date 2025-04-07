# WebhookCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookCreateRequestData**](WebhookCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.webhook_create_request import WebhookCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateRequest from a JSON string
webhook_create_request_instance = WebhookCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookCreateRequest.to_json())

# convert the object into a dict
webhook_create_request_dict = webhook_create_request_instance.to_dict()
# create an instance of WebhookCreateRequest from a dict
webhook_create_request_from_dict = WebhookCreateRequest.from_dict(webhook_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


