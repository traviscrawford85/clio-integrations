# ClientPortalBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ClientPortal* | [optional] 
**etag** | **str** | ETag for the *ClientPortal* | [optional] 
**created_at** | **datetime** | The time the *ClientPortal* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ClientPortal* was last updated (as a ISO-8601 timestamp) | [optional] 
**unread_count** | **int** | The number of unread count messages for the current user. | [optional] 
**unread_notifiable_count** | **int** | The number of unread messages for the current user once their notification settings have been applied. | [optional] 

## Example

```python
from openapi_client.models.client_portal_base import ClientPortalBase

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPortalBase from a JSON string
client_portal_base_instance = ClientPortalBase.from_json(json)
# print the JSON string representation of the object
print(ClientPortalBase.to_json())

# convert the object into a dict
client_portal_base_dict = client_portal_base_instance.to_dict()
# create an instance of ClientPortalBase from a dict
client_portal_base_from_dict = ClientPortalBase.from_dict(client_portal_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


