# DocumentCopyRequestDataDocumentCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single DocumentCategory associated with the Document. Use the keyword &#x60;null&#x60; to specify no association. | [optional] 

## Example

```python
from openapi_client.models.document_copy_request_data_document_category import DocumentCopyRequestDataDocumentCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCopyRequestDataDocumentCategory from a JSON string
document_copy_request_data_document_category_instance = DocumentCopyRequestDataDocumentCategory.from_json(json)
# print the JSON string representation of the object
print(DocumentCopyRequestDataDocumentCategory.to_json())

# convert the object into a dict
document_copy_request_data_document_category_dict = document_copy_request_data_document_category_instance.to_dict()
# create an instance of DocumentCopyRequestDataDocumentCategory from a dict
document_copy_request_data_document_category_from_dict = DocumentCopyRequestDataDocumentCategory.from_dict(document_copy_request_data_document_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


