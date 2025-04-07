# ActivityTextMessageConversationBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TextMessageConversation* | [optional] 
**etag** | **str** | ETag for the *TextMessageConversation* | [optional] 

## Example

```python
from openapi_client.models.activity_text_message_conversation_base import ActivityTextMessageConversationBase

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTextMessageConversationBase from a JSON string
activity_text_message_conversation_base_instance = ActivityTextMessageConversationBase.from_json(json)
# print the JSON string representation of the object
print(ActivityTextMessageConversationBase.to_json())

# convert the object into a dict
activity_text_message_conversation_base_dict = activity_text_message_conversation_base_instance.to_dict()
# create an instance of ActivityTextMessageConversationBase from a dict
activity_text_message_conversation_base_from_dict = ActivityTextMessageConversationBase.from_dict(activity_text_message_conversation_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


