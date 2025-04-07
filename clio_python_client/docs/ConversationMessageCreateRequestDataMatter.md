# ConversationMessageCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the ConversationMessage. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.conversation_message_create_request_data_matter import ConversationMessageCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageCreateRequestDataMatter from a JSON string
conversation_message_create_request_data_matter_instance = ConversationMessageCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageCreateRequestDataMatter.to_json())

# convert the object into a dict
conversation_message_create_request_data_matter_dict = conversation_message_create_request_data_matter_instance.to_dict()
# create an instance of ConversationMessageCreateRequestDataMatter from a dict
conversation_message_create_request_data_matter_from_dict = ConversationMessageCreateRequestDataMatter.from_dict(conversation_message_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


