# DocumentCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_id** | **int** | Related communication record. | [optional] 
**content_type** | **str** | A standard MIME type describing the format of the object data. If the field is not specified, it is determined by the file extension. | [optional] 
**document_category** | [**DocumentCopyRequestDataDocumentCategory**](DocumentCopyRequestDataDocumentCategory.md) |  | [optional] 
**external_properties** | [**List[DocumentCreateRequestDataExternalPropertiesInner]**](DocumentCreateRequestDataExternalPropertiesInner.md) |  | [optional] 
**filename** | **str** | Name of the original file. | [optional] [default to 'name']
**multiparts** | [**List[DocumentCreateRequestDataMultipartsInner]**](DocumentCreateRequestDataMultipartsInner.md) |  | [optional] 
**name** | **str** | Document name. | 
**parent** | [**DocumentCopyRequestDataParent**](DocumentCopyRequestDataParent.md) |  | 
**received_at** | **datetime** | Date and time the document was received (Expects an ISO-8601 timestamp). | [optional] 

## Example

```python
from openapi_client.models.document_create_request_data import DocumentCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateRequestData from a JSON string
document_create_request_data_instance = DocumentCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateRequestData.to_json())

# convert the object into a dict
document_create_request_data_dict = document_create_request_data_instance.to_dict()
# create an instance of DocumentCreateRequestData from a dict
document_create_request_data_from_dict = DocumentCreateRequestData.from_dict(document_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


