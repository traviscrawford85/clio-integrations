# ConversationMessageCreateRequestDataAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** | The document id of the attached document. | [optional] 
**document_version_id** | **int** | The document version id of the attached document. | [optional] 

## Example

```python
from openapi_client.models.conversation_message_create_request_data_attachment import ConversationMessageCreateRequestDataAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageCreateRequestDataAttachment from a JSON string
conversation_message_create_request_data_attachment_instance = ConversationMessageCreateRequestDataAttachment.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageCreateRequestDataAttachment.to_json())

# convert the object into a dict
conversation_message_create_request_data_attachment_dict = conversation_message_create_request_data_attachment_instance.to_dict()
# create an instance of ConversationMessageCreateRequestDataAttachment from a dict
conversation_message_create_request_data_attachment_from_dict = ConversationMessageCreateRequestDataAttachment.from_dict(conversation_message_create_request_data_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


