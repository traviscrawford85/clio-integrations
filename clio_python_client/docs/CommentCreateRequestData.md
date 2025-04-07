# CommentCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**CommentCreateRequestDataItem**](CommentCreateRequestDataItem.md) |  | 
**message** | **str** | The content of the Comment. | 

## Example

```python
from openapi_client.models.comment_create_request_data import CommentCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CommentCreateRequestData from a JSON string
comment_create_request_data_instance = CommentCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(CommentCreateRequestData.to_json())

# convert the object into a dict
comment_create_request_data_dict = comment_create_request_data_instance.to_dict()
# create an instance of CommentCreateRequestData from a dict
comment_create_request_data_from_dict = CommentCreateRequestData.from_dict(comment_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


