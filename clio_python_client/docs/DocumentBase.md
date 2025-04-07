# DocumentBase


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

## Example

```python
from openapi_client.models.document_base import DocumentBase

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBase from a JSON string
document_base_instance = DocumentBase.from_json(json)
# print the JSON string representation of the object
print(DocumentBase.to_json())

# convert the object into a dict
document_base_dict = document_base_instance.to_dict()
# create an instance of DocumentBase from a dict
document_base_from_dict = DocumentBase.from_dict(document_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


