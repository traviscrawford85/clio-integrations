# ConversationUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | Whether or not the Conversation has been archived. | [optional] 
**matter** | [**ConversationUpdateRequestDataMatter**](ConversationUpdateRequestDataMatter.md) |  | [optional] 
**read** | **bool** | Whether or not the Conversation has been read. | [optional] 

## Example

```python
from openapi_client.models.conversation_update_request_data import ConversationUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationUpdateRequestData from a JSON string
conversation_update_request_data_instance = ConversationUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ConversationUpdateRequestData.to_json())

# convert the object into a dict
conversation_update_request_data_dict = conversation_update_request_data_instance.to_dict()
# create an instance of ConversationUpdateRequestData from a dict
conversation_update_request_data_from_dict = ConversationUpdateRequestData.from_dict(conversation_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


