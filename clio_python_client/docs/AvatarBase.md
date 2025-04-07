# AvatarBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Avatar* | [optional] 
**etag** | **str** | ETag for the *Avatar* | [optional] 
**created_at** | **datetime** | The time the *Avatar* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Avatar* was last updated (as a ISO-8601 timestamp) | [optional] 
**url** | **str** | The URL for the *Avatar* | [optional] 
**destroy** | **bool** | Whether to destroy the *Avatar* | [optional] 

## Example

```python
from openapi_client.models.avatar_base import AvatarBase

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarBase from a JSON string
avatar_base_instance = AvatarBase.from_json(json)
# print the JSON string representation of the object
print(AvatarBase.to_json())

# convert the object into a dict
avatar_base_dict = avatar_base_instance.to_dict()
# create an instance of AvatarBase from a dict
avatar_base_from_dict = AvatarBase.from_dict(avatar_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


