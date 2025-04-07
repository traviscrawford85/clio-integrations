# WebhookUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[str]** | The events your webhook is subscribed to. | [optional] 
**expires_at** | **datetime** | The date and time when the Webhook will expire. (Expects an ISO-8601 timestamp). | [optional] 
**fields** | **str** | Fields to be included in the Webhook request. | [optional] 
**model** | **str** | What model the Webhook is for. This field accepts either [the string identifier of the model or its ID](#section/Supported-Models) | [optional] 
**url** | **str** | The URL of where to POST the Webhook. Note that only URLs using the &#x60;https&#x60; protocol will be accepted. | [optional] 

## Example

```python
from openapi_client.models.webhook_update_request_data import WebhookUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUpdateRequestData from a JSON string
webhook_update_request_data_instance = WebhookUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(WebhookUpdateRequestData.to_json())

# convert the object into a dict
webhook_update_request_data_dict = webhook_update_request_data_instance.to_dict()
# create an instance of WebhookUpdateRequestData from a dict
webhook_update_request_data_from_dict = WebhookUpdateRequestData.from_dict(webhook_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


