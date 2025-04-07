# ConversationMembershipBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ConversationMembership* | [optional] 
**etag** | **str** | ETag for the *ConversationMembership* | [optional] 
**read** | **bool** | Whether or not the ConversationMembership has been read by the member | [optional] 
**archived** | **bool** | Whether or not the ConversationMembership has been archived by the member | [optional] 
**created_at** | **datetime** | The time the *ConversationMembership* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ConversationMembership* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.conversation_membership_base import ConversationMembershipBase

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMembershipBase from a JSON string
conversation_membership_base_instance = ConversationMembershipBase.from_json(json)
# print the JSON string representation of the object
print(ConversationMembershipBase.to_json())

# convert the object into a dict
conversation_membership_base_dict = conversation_membership_base_instance.to_dict()
# create an instance of ConversationMembershipBase from a dict
conversation_membership_base_from_dict = ConversationMembershipBase.from_dict(conversation_membership_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


