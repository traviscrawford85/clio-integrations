# ConversationMessageCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | [**ConversationMessageCreateRequestDataAttachment**](ConversationMessageCreateRequestDataAttachment.md) |  | [optional] 
**body** | **str** | The body value. | 
**conversation** | [**ConversationMessageCreateRequestDataConversation**](ConversationMessageCreateRequestDataConversation.md) |  | [optional] 
**matter** | [**ConversationMessageCreateRequestDataMatter**](ConversationMessageCreateRequestDataMatter.md) |  | [optional] 
**receivers** | [**List[ConversationMessageCreateRequestDataReceiversInner]**](ConversationMessageCreateRequestDataReceiversInner.md) |  | 
**subject** | **str** | The subject value. | 

## Example

```python
from openapi_client.models.conversation_message_create_request_data import ConversationMessageCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageCreateRequestData from a JSON string
conversation_message_create_request_data_instance = ConversationMessageCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageCreateRequestData.to_json())

# convert the object into a dict
conversation_message_create_request_data_dict = conversation_message_create_request_data_instance.to_dict()
# create an instance of ConversationMessageCreateRequestData from a dict
conversation_message_create_request_data_from_dict = ConversationMessageCreateRequestData.from_dict(conversation_message_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


