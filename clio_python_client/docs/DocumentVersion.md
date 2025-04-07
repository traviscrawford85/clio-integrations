# DocumentVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *DocumentVersion* | [optional] 
**document_id** | **int** | The ID of the parent document. | [optional] 
**etag** | **str** | ETag for the *DocumentVersion* | [optional] 
**uuid** | **str** | UUID associated with the DocumentVersion. UUID is required to mark a document fully uploaded. | [optional] 
**created_at** | **datetime** | The time the *DocumentVersion* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *DocumentVersion* was last updated (as a ISO-8601 timestamp) | [optional] 
**filename** | **str** | The uploaded file name of the DocumentVersion. | [optional] 
**size** | **int** | The size of the DocumentVersion in bytes. | [optional] 
**version_number** | **int** | The ordered number of when this DocumentVersion was uploaded. | [optional] 
**content_type** | **str** | A standard MIME type describing the format of the object data. | [optional] 
**received_at** | **datetime** | The time the DocumentVersion was received (as an ISO-8601 timestamp) | [optional] 
**put_url** | **str** | A signed URL for uploading the file in a single operation. It expires in 10 minutes. If the document is fully uploaded, the field is empty. | [optional] 
**fully_uploaded** | **bool** | True if the DocumentVersion is uploaded. False if the DocumentVersion is being uploaded. | [optional] 
**creator** | [**ClioCreatorBase**](ClioCreatorBase.md) |  | [optional] 
**put_headers** | [**List[MultipartHeaderBase]**](MultipartHeaderBase.md) | MultipartHeader | [optional] 
**multiparts** | [**List[Multipart]**](Multipart.md) | Multipart | [optional] 

## Example

```python
from openapi_client.models.document_version import DocumentVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVersion from a JSON string
document_version_instance = DocumentVersion.from_json(json)
# print the JSON string representation of the object
print(DocumentVersion.to_json())

# convert the object into a dict
document_version_dict = document_version_instance.to_dict()
# create an instance of DocumentVersion from a dict
document_version_from_dict = DocumentVersion.from_dict(document_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


