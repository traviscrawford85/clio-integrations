# DocumentCategoryBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *DocumentCategory* | [optional] 
**etag** | **str** | ETag for the *DocumentCategory* | [optional] 
**name** | **str** | The name of the *DocumentCategory* | [optional] 
**created_at** | **datetime** | The time the *DocumentCategory* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *DocumentCategory* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.document_category_base import DocumentCategoryBase

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryBase from a JSON string
document_category_base_instance = DocumentCategoryBase.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryBase.to_json())

# convert the object into a dict
document_category_base_dict = document_category_base_instance.to_dict()
# create an instance of DocumentCategoryBase from a dict
document_category_base_from_dict = DocumentCategoryBase.from_dict(document_category_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


