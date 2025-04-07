# FolderCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_category** | [**FolderCreateRequestDataDocumentCategory**](FolderCreateRequestDataDocumentCategory.md) |  | [optional] 
**external_properties** | [**List[FolderCreateRequestDataExternalPropertiesInner]**](FolderCreateRequestDataExternalPropertiesInner.md) |  | [optional] 
**name** | **str** | Name of the Folder | 
**parent** | [**FolderCreateRequestDataParent**](FolderCreateRequestDataParent.md) |  | 
**restore** | **bool** | Whether or not a trashed Folder should be restored. | [optional] 

## Example

```python
from openapi_client.models.folder_create_request_data import FolderCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCreateRequestData from a JSON string
folder_create_request_data_instance = FolderCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(FolderCreateRequestData.to_json())

# convert the object into a dict
folder_create_request_data_dict = folder_create_request_data_instance.to_dict()
# create an instance of FolderCreateRequestData from a dict
folder_create_request_data_from_dict = FolderCreateRequestData.from_dict(folder_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


