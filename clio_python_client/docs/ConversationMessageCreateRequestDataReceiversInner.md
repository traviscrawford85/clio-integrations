# ConversationMessageCreateRequestDataReceiversInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single receiver for this ConversationMessage. | 
**type** | **str** | The type for a single receiver for this ConversationMessage, could be &#x60;Contact&#x60; or &#x60;User&#x60;. | 

## Example

```python
from openapi_client.models.conversation_message_create_request_data_receivers_inner import ConversationMessageCreateRequestDataReceiversInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageCreateRequestDataReceiversInner from a JSON string
conversation_message_create_request_data_receivers_inner_instance = ConversationMessageCreateRequestDataReceiversInner.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageCreateRequestDataReceiversInner.to_json())

# convert the object into a dict
conversation_message_create_request_data_receivers_inner_dict = conversation_message_create_request_data_receivers_inner_instance.to_dict()
# create an instance of ConversationMessageCreateRequestDataReceiversInner from a dict
conversation_message_create_request_data_receivers_inner_from_dict = ConversationMessageCreateRequestDataReceiversInner.from_dict(conversation_message_create_request_data_receivers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


