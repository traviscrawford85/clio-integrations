# ConversationMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ConversationMembership* | [optional] 
**etag** | **str** | ETag for the *ConversationMembership* | [optional] 
**read** | **bool** | Whether or not the ConversationMembership has been read by the member | [optional] 
**archived** | **bool** | Whether or not the ConversationMembership has been archived by the member | [optional] 
**created_at** | **datetime** | The time the *ConversationMembership* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ConversationMembership* was last updated (as a ISO-8601 timestamp) | [optional] 
**member** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.conversation_membership import ConversationMembership

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMembership from a JSON string
conversation_membership_instance = ConversationMembership.from_json(json)
# print the JSON string representation of the object
print(ConversationMembership.to_json())

# convert the object into a dict
conversation_membership_dict = conversation_membership_instance.to_dict()
# create an instance of ConversationMembership from a dict
conversation_membership_from_dict = ConversationMembership.from_dict(conversation_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


