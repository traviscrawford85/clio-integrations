# CommentCreateRequestDataItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the Document or Folder to which the Comment is associated. | 

## Example

```python
from openapi_client.models.comment_create_request_data_item import CommentCreateRequestDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommentCreateRequestDataItem from a JSON string
comment_create_request_data_item_instance = CommentCreateRequestDataItem.from_json(json)
# print the JSON string representation of the object
print(CommentCreateRequestDataItem.to_json())

# convert the object into a dict
comment_create_request_data_item_dict = comment_create_request_data_item_instance.to_dict()
# create an instance of CommentCreateRequestDataItem from a dict
comment_create_request_data_item_from_dict = CommentCreateRequestDataItem.from_dict(comment_create_request_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


