# Conversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Conversation* | [optional] 
**etag** | **str** | ETag for the *Conversation* | [optional] 
**archived** | **bool** | Whether the conversation has been archived | [optional] 
**read_only** | **bool** | Whether the conversation is read only | [optional] 
**current_user_is_member** | **bool** | Whether the current user is a member of this conversation | [optional] 
**subject** | **str** | The subject of the *Conversation* | [optional] 
**message_count** | **int** | The number of messages in this conversation | [optional] 
**time_entries_count** | **int** | The number of time entries applied to this conversation | [optional] 
**read** | **bool** | Whether any messages in this conversation have been viewed | [optional] 
**created_at** | **datetime** | The time the *Conversation* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Conversation* was last updated (as a ISO-8601 timestamp) | [optional] 
**last_message** | [**ConversationMessageBase**](ConversationMessageBase.md) |  | [optional] 
**first_message** | [**ConversationMessageBase**](ConversationMessageBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**messages** | [**List[ConversationMessageBase]**](ConversationMessageBase.md) | ConversationMessage | [optional] 
**documents** | [**List[DocumentBase]**](DocumentBase.md) | Document | [optional] 
**memberships** | [**List[ConversationMembership]**](ConversationMembership.md) | ConversationMembership | [optional] 

## Example

```python
from openapi_client.models.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print(Conversation.to_json())

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_from_dict = Conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


