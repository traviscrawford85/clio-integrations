# DocumentUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_id** | **int** | Related communication record. | [optional] 
**copy_version** | **bool** | Indicates whether to create a new version with the updated filename on rename. This is intended to handle cases where the document extension has been changed; if the document extension has not changed, no new version will be created. | [optional] 
**document_category** | [**DocumentCopyRequestDataDocumentCategory**](DocumentCopyRequestDataDocumentCategory.md) |  | [optional] 
**external_properties** | [**List[DocumentCopyRequestDataExternalPropertiesInner]**](DocumentCopyRequestDataExternalPropertiesInner.md) |  | [optional] 
**fully_uploaded** | **bool** | Indicates whether document is uploaded.  When marking the document fully uploaded, it arises errors when: * The file is not successfully uploaded. * Not all the file parts are uploaded. * The document is already marked as fully uploaded.  | [optional] 
**multiparts** | [**List[DocumentUpdateRequestDataMultipartsInner]**](DocumentUpdateRequestDataMultipartsInner.md) |  | [optional] 
**name** | **str** | Document name. | [optional] 
**parent** | [**DocumentUpdateRequestDataParent**](DocumentUpdateRequestDataParent.md) |  | [optional] 
**received_at** | **datetime** | Date and time the document was received (Expects an ISO-8601 timestamp). | [optional] 
**restore** | **bool** | Whether or not a trashed Document should be restored. | [optional] 
**uuid** | **str** | UUID associated with the document version. UUID is required to mark a document fully uploaded. | [optional] 

## Example

```python
from openapi_client.models.document_update_request_data import DocumentUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequestData from a JSON string
document_update_request_data_instance = DocumentUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequestData.to_json())

# convert the object into a dict
document_update_request_data_dict = document_update_request_data_instance.to_dict()
# create an instance of DocumentUpdateRequestData from a dict
document_update_request_data_from_dict = DocumentUpdateRequestData.from_dict(document_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


