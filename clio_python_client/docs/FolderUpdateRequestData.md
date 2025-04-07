# FolderUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_category** | [**FolderCreateRequestDataDocumentCategory**](FolderCreateRequestDataDocumentCategory.md) |  | [optional] 
**external_properties** | [**List[FolderUpdateRequestDataExternalPropertiesInner]**](FolderUpdateRequestDataExternalPropertiesInner.md) |  | [optional] 
**name** | **str** | Name of the Folder | [optional] 
**parent** | [**FolderUpdateRequestDataParent**](FolderUpdateRequestDataParent.md) |  | [optional] 
**restore** | **bool** | Whether or not a trashed Folder should be restored. | [optional] 

## Example

```python
from openapi_client.models.folder_update_request_data import FolderUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUpdateRequestData from a JSON string
folder_update_request_data_instance = FolderUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(FolderUpdateRequestData.to_json())

# convert the object into a dict
folder_update_request_data_dict = folder_update_request_data_instance.to_dict()
# create an instance of FolderUpdateRequestData from a dict
folder_update_request_data_from_dict = FolderUpdateRequestData.from_dict(folder_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


