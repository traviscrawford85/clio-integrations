# InstantMessengerBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *InstantMessenger* | [optional] 
**etag** | **str** | ETag for the *InstantMessenger* | [optional] 
**address** | **str** | The address of the *InstantMessenger* | [optional] 
**name** | **str** | The type of *InstantMessenger* it is | [optional] 
**created_at** | **datetime** | The time the *InstantMessenger* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *InstantMessenger* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.instant_messenger_base import InstantMessengerBase

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMessengerBase from a JSON string
instant_messenger_base_instance = InstantMessengerBase.from_json(json)
# print the JSON string representation of the object
print(InstantMessengerBase.to_json())

# convert the object into a dict
instant_messenger_base_dict = instant_messenger_base_instance.to_dict()
# create an instance of InstantMessengerBase from a dict
instant_messenger_base_from_dict = InstantMessengerBase.from_dict(instant_messenger_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


