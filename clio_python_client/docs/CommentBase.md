# CommentBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Comment* | [optional] 
**etag** | **str** | ETag for the *Comment* | [optional] 
**message** | **str** | The content of the Comment | [optional] 
**created_at** | **datetime** | The time the *Comment* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Comment* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.comment_base import CommentBase

# TODO update the JSON string below
json = "{}"
# create an instance of CommentBase from a JSON string
comment_base_instance = CommentBase.from_json(json)
# print the JSON string representation of the object
print(CommentBase.to_json())

# convert the object into a dict
comment_base_dict = comment_base_instance.to_dict()
# create an instance of CommentBase from a dict
comment_base_from_dict = CommentBase.from_dict(comment_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


