# DocumentArchiveBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *DocumentArchive* | [optional] 
**etag** | **str** | ETag for the *DocumentArchive* | [optional] 
**created_at** | **datetime** | The time the *DocumentArchive* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *DocumentArchive* was last updated (as a ISO-8601 timestamp) | [optional] 
**size** | **int** | The size of the DocumentArchive in bytes. | [optional] 
**progress** | **float** | The percent completion of the DocumentArchive. | [optional] 
**state** | **str** | The current state of the DocumentArchive. | [optional] 
**message** | **str** | A message to indicate why the DocumentArchive didn&#39;t complete. | [optional] 

## Example

```python
from openapi_client.models.document_archive_base import DocumentArchiveBase

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentArchiveBase from a JSON string
document_archive_base_instance = DocumentArchiveBase.from_json(json)
# print the JSON string representation of the object
print(DocumentArchiveBase.to_json())

# convert the object into a dict
document_archive_base_dict = document_archive_base_instance.to_dict()
# create an instance of DocumentArchiveBase from a dict
document_archive_base_from_dict = DocumentArchiveBase.from_dict(document_archive_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


