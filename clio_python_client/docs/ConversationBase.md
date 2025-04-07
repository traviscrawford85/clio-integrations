# ConversationBase


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

## Example

```python
from openapi_client.models.conversation_base import ConversationBase

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationBase from a JSON string
conversation_base_instance = ConversationBase.from_json(json)
# print the JSON string representation of the object
print(ConversationBase.to_json())

# convert the object into a dict
conversation_base_dict = conversation_base_instance.to_dict()
# create an instance of ConversationBase from a dict
conversation_base_from_dict = ConversationBase.from_dict(conversation_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


