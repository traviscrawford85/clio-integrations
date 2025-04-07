# CommentUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**CommentUpdateRequestDataItem**](CommentUpdateRequestDataItem.md) |  | [optional] 
**message** | **str** | The content of the Comment. | [optional] 

## Example

```python
from openapi_client.models.comment_update_request_data import CommentUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CommentUpdateRequestData from a JSON string
comment_update_request_data_instance = CommentUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CommentUpdateRequestData.to_json())

# convert the object into a dict
comment_update_request_data_dict = comment_update_request_data_instance.to_dict()
# create an instance of CommentUpdateRequestData from a dict
comment_update_request_data_from_dict = CommentUpdateRequestData.from_dict(comment_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


