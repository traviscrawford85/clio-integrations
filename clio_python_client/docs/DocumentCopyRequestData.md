# DocumentCopyRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_id** | **int** | Related communication record. | [optional] 
**document_category** | [**DocumentCopyRequestDataDocumentCategory**](DocumentCopyRequestDataDocumentCategory.md) |  | [optional] 
**external_properties** | [**List[DocumentCopyRequestDataExternalPropertiesInner]**](DocumentCopyRequestDataExternalPropertiesInner.md) |  | [optional] 
**filename** | **str** | Name of the original file. | [optional] [default to 'name']
**name** | **str** | Document name. | [optional] 
**parent** | [**DocumentCopyRequestDataParent**](DocumentCopyRequestDataParent.md) |  | 
**received_at** | **datetime** | Date and time the document was received (Expects an ISO-8601 timestamp). | [optional] 

## Example

```python
from openapi_client.models.document_copy_request_data import DocumentCopyRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCopyRequestData from a JSON string
document_copy_request_data_instance = DocumentCopyRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentCopyRequestData.to_json())

# convert the object into a dict
document_copy_request_data_dict = document_copy_request_data_instance.to_dict()
# create an instance of DocumentCopyRequestData from a dict
document_copy_request_data_from_dict = DocumentCopyRequestData.from_dict(document_copy_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


