# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Document* | [optional] 
**etag** | **str** | ETag for the *Document* | [optional] 
**created_at** | **datetime** | The time the *Document* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Document* was last updated (as a ISO-8601 timestamp) | [optional] 
**deleted_at** | **datetime** | The time the *Document* was deleted (as a ISO-8601 timestamp) | [optional] 
**type** | **str** | The type of the *Document* | [optional] 
**locked** | **bool** | Whether or not the Document is locked. Locked Document cannot be modified | [optional] 
**name** | **str** | The name of the Document | [optional] 
**received_at** | **datetime** | The time the last document version was received (as an ISO-8601 timestamp) | [optional] 
**filename** | **str** | The uploaded file name of the latest document version. | [optional] 
**size** | **int** | The file size | [optional] 
**content_type** | **str** | The uploaded file content type | [optional] 
**parent** | [**LinkedFolderBase**](LinkedFolderBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**document_category** | [**DocumentCategoryBase**](DocumentCategoryBase.md) |  | [optional] 
**creator** | [**ClioCreatorBase**](ClioCreatorBase.md) |  | [optional] 
**latest_document_version** | [**DocumentVersion**](DocumentVersion.md) |  | [optional] 
**group** | [**GroupBase**](GroupBase.md) |  | [optional] 
**external_properties** | [**List[ExternalPropertyBase]**](ExternalPropertyBase.md) | ExternalProperty | [optional] 
**document_versions** | [**List[DocumentVersionBase]**](DocumentVersionBase.md) | DocumentVersion | [optional] 

## Example

```python
from openapi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


