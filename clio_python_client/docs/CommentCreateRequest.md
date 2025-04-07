# CommentCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommentCreateRequestData**](CommentCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.comment_create_request import CommentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentCreateRequest from a JSON string
comment_create_request_instance = CommentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CommentCreateRequest.to_json())

# convert the object into a dict
comment_create_request_dict = comment_create_request_instance.to_dict()
# create an instance of CommentCreateRequest from a dict
comment_create_request_from_dict = CommentCreateRequest.from_dict(comment_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


