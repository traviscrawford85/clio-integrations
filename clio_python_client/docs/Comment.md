# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Comment* | [optional] 
**etag** | **str** | ETag for the *Comment* | [optional] 
**message** | **str** | The content of the Comment | [optional] 
**created_at** | **datetime** | The time the *Comment* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Comment* was last updated (as a ISO-8601 timestamp) | [optional] 
**creator** | [**UserBase**](UserBase.md) |  | [optional] 
**document_version** | [**DocumentVersionBase**](DocumentVersionBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


