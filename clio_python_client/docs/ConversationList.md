# ConversationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Conversation]**](Conversation.md) | Conversation List Response | 

## Example

```python
from openapi_client.models.conversation_list import ConversationList

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationList from a JSON string
conversation_list_instance = ConversationList.from_json(json)
# print the JSON string representation of the object
print(ConversationList.to_json())

# convert the object into a dict
conversation_list_dict = conversation_list_instance.to_dict()
# create an instance of ConversationList from a dict
conversation_list_from_dict = ConversationList.from_dict(conversation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


