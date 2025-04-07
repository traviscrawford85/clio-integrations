# DocumentCategory


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
from openapi_client.models.document_category import DocumentCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategory from a JSON string
document_category_instance = DocumentCategory.from_json(json)
# print the JSON string representation of the object
print(DocumentCategory.to_json())

# convert the object into a dict
document_category_dict = document_category_instance.to_dict()
# create an instance of DocumentCategory from a dict
document_category_from_dict = DocumentCategory.from_dict(document_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


