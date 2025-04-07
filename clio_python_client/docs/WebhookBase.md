# WebhookBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Webhook* | [optional] 
**etag** | **str** | ETag for the *Webhook* | [optional] 
**url** | **str** | The &#x60;https&#x60; URL to send the data to when the events are triggered | [optional] 
**fields** | **str** | Fields to be included in the webhook request | [optional] 
**shared_secret** | **str** | A shared secret used to create a signature for the payload | [optional] 
**model** | **str** | What kind of records the webhook is for | [optional] 
**status** | **str** | The current status of the webhook. | [optional] 
**events** | **List[str]** | The events your webhook is subscribed to. | [optional] 
**expires_at** | **datetime** | The time webhook will expire (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *Webhook* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Webhook* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.webhook_base import WebhookBase

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBase from a JSON string
webhook_base_instance = WebhookBase.from_json(json)
# print the JSON string representation of the object
print(WebhookBase.to_json())

# convert the object into a dict
webhook_base_dict = webhook_base_instance.to_dict()
# create an instance of WebhookBase from a dict
webhook_base_from_dict = WebhookBase.from_dict(webhook_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


