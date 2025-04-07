# ConversationMessageCreateRequestDataConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Conversation associated with this ConversationMessage. | [optional] 

## Example

```python
from openapi_client.models.conversation_message_create_request_data_conversation import ConversationMessageCreateRequestDataConversation

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageCreateRequestDataConversation from a JSON string
conversation_message_create_request_data_conversation_instance = ConversationMessageCreateRequestDataConversation.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageCreateRequestDataConversation.to_json())

# convert the object into a dict
conversation_message_create_request_data_conversation_dict = conversation_message_create_request_data_conversation_instance.to_dict()
# create an instance of ConversationMessageCreateRequestDataConversation from a dict
conversation_message_create_request_data_conversation_from_dict = ConversationMessageCreateRequestDataConversation.from_dict(conversation_message_create_request_data_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


