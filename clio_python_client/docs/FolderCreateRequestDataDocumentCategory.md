# FolderCreateRequestDataDocumentCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single DocumentCategory associated with the Folder. Use the keyword &#x60;null&#x60; to specify no association. | [optional] 

## Example

```python
from openapi_client.models.folder_create_request_data_document_category import FolderCreateRequestDataDocumentCategory

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCreateRequestDataDocumentCategory from a JSON string
folder_create_request_data_document_category_instance = FolderCreateRequestDataDocumentCategory.from_json(json)
# print the JSON string representation of the object
print(FolderCreateRequestDataDocumentCategory.to_json())

# convert the object into a dict
folder_create_request_data_document_category_dict = folder_create_request_data_document_category_instance.to_dict()
# create an instance of FolderCreateRequestDataDocumentCategory from a dict
folder_create_request_data_document_category_from_dict = FolderCreateRequestDataDocumentCategory.from_dict(folder_create_request_data_document_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


