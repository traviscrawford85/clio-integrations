# DocumentTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *DocumentTemplate* | [optional] 
**etag** | **str** | ETag for the *DocumentTemplate* | [optional] 
**size** | **int** | The size in bytes of the template | [optional] 
**content_type** | **str** | A standard MIME type describing the format of the object data. | [optional] 
**filename** | **str** | The name of the original file that was uploaded | [optional] 
**created_at** | **datetime** | The time the *DocumentTemplate* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *DocumentTemplate* was last updated (as a ISO-8601 timestamp) | [optional] 
**document_category** | [**DocumentCategoryBase**](DocumentCategoryBase.md) |  | [optional] 
**last_modified_by** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_template import DocumentTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplate from a JSON string
document_template_instance = DocumentTemplate.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplate.to_json())

# convert the object into a dict
document_template_dict = document_template_instance.to_dict()
# create an instance of DocumentTemplate from a dict
document_template_from_dict = DocumentTemplate.from_dict(document_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


