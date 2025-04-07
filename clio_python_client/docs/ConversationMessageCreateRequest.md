# ConversationMessageCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ConversationMessageCreateRequestData**](ConversationMessageCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.conversation_message_create_request import ConversationMessageCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageCreateRequest from a JSON string
conversation_message_create_request_instance = ConversationMessageCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageCreateRequest.to_json())

# convert the object into a dict
conversation_message_create_request_dict = conversation_message_create_request_instance.to_dict()
# create an instance of ConversationMessageCreateRequest from a dict
conversation_message_create_request_from_dict = ConversationMessageCreateRequest.from_dict(conversation_message_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


