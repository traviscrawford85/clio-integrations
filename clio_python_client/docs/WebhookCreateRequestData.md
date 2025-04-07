# WebhookCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[str]** | The events your webhook is subscribed to. | [optional] 
**expires_at** | **datetime** | The date and time when the Webhook will expire. (Expects an ISO-8601 timestamp). | [optional] 
**fields** | **str** | Fields to be included in the Webhook request. | 
**model** | **str** | What model the Webhook is for. This field accepts either [the string identifier of the model or its ID](#section/Supported-Models) | 
**url** | **str** | The URL of where to POST the Webhook. Note that only URLs using the &#x60;https&#x60; protocol will be accepted. | 

## Example

```python
from openapi_client.models.webhook_create_request_data import WebhookCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateRequestData from a JSON string
webhook_create_request_data_instance = WebhookCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(WebhookCreateRequestData.to_json())

# convert the object into a dict
webhook_create_request_data_dict = webhook_create_request_data_instance.to_dict()
# create an instance of WebhookCreateRequestData from a dict
webhook_create_request_data_from_dict = WebhookCreateRequestData.from_dict(webhook_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


