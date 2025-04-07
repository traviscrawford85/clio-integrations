# WebhookList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Webhook]**](Webhook.md) | Webhook List Response | 

## Example

```python
from openapi_client.models.webhook_list import WebhookList

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookList from a JSON string
webhook_list_instance = WebhookList.from_json(json)
# print the JSON string representation of the object
print(WebhookList.to_json())

# convert the object into a dict
webhook_list_dict = webhook_list_instance.to_dict()
# create an instance of WebhookList from a dict
webhook_list_from_dict = WebhookList.from_dict(webhook_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


