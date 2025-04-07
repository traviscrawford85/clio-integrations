# ConversationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ConversationUpdateRequestData**](ConversationUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.conversation_update_request import ConversationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationUpdateRequest from a JSON string
conversation_update_request_instance = ConversationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ConversationUpdateRequest.to_json())

# convert the object into a dict
conversation_update_request_dict = conversation_update_request_instance.to_dict()
# create an instance of ConversationUpdateRequest from a dict
conversation_update_request_from_dict = ConversationUpdateRequest.from_dict(conversation_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


