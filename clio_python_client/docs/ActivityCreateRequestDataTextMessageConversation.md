# ActivityCreateRequestDataTextMessageConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single TextMessageConversation associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_text_message_conversation import ActivityCreateRequestDataTextMessageConversation

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataTextMessageConversation from a JSON string
activity_create_request_data_text_message_conversation_instance = ActivityCreateRequestDataTextMessageConversation.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataTextMessageConversation.to_json())

# convert the object into a dict
activity_create_request_data_text_message_conversation_dict = activity_create_request_data_text_message_conversation_instance.to_dict()
# create an instance of ActivityCreateRequestDataTextMessageConversation from a dict
activity_create_request_data_text_message_conversation_from_dict = ActivityCreateRequestDataTextMessageConversation.from_dict(activity_create_request_data_text_message_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


