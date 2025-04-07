# ConversationMessageBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ConversationMessage* | [optional] 
**etag** | **str** | ETag for the *ConversationMessage* | [optional] 
**var_date** | **str** | The creation date of the message in the current user&#39;s time zone | [optional] 
**body** | **str** | The main content of the *ConversationMessage* | [optional] 
**created_at** | **datetime** | The time the *ConversationMessage* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ConversationMessage* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.conversation_message_base import ConversationMessageBase

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageBase from a JSON string
conversation_message_base_instance = ConversationMessageBase.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageBase.to_json())

# convert the object into a dict
conversation_message_base_dict = conversation_message_base_instance.to_dict()
# create an instance of ConversationMessageBase from a dict
conversation_message_base_from_dict = ConversationMessageBase.from_dict(conversation_message_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


