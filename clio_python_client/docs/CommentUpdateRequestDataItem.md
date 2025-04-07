# CommentUpdateRequestDataItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the Document or Folder to which the Comment is associated. | [optional] 

## Example

```python
from openapi_client.models.comment_update_request_data_item import CommentUpdateRequestDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommentUpdateRequestDataItem from a JSON string
comment_update_request_data_item_instance = CommentUpdateRequestDataItem.from_json(json)
# print the JSON string representation of the object
print(CommentUpdateRequestDataItem.to_json())

# convert the object into a dict
comment_update_request_data_item_dict = comment_update_request_data_item_instance.to_dict()
# create an instance of CommentUpdateRequestDataItem from a dict
comment_update_request_data_item_from_dict = CommentUpdateRequestDataItem.from_dict(comment_update_request_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


