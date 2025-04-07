# ConversationMessageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConversationMessage]**](ConversationMessage.md) | ConversationMessage List Response | 

## Example

```python
from openapi_client.models.conversation_message_list import ConversationMessageList

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageList from a JSON string
conversation_message_list_instance = ConversationMessageList.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageList.to_json())

# convert the object into a dict
conversation_message_list_dict = conversation_message_list_instance.to_dict()
# create an instance of ConversationMessageList from a dict
conversation_message_list_from_dict = ConversationMessageList.from_dict(conversation_message_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


