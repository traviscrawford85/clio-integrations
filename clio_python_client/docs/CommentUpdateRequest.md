# CommentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommentUpdateRequestData**](CommentUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.comment_update_request import CommentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentUpdateRequest from a JSON string
comment_update_request_instance = CommentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CommentUpdateRequest.to_json())

# convert the object into a dict
comment_update_request_dict = comment_update_request_instance.to_dict()
# create an instance of CommentUpdateRequest from a dict
comment_update_request_from_dict = CommentUpdateRequest.from_dict(comment_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


