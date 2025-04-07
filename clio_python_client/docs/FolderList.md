# FolderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Folder]**](Folder.md) | Folder List Response | 

## Example

```python
from openapi_client.models.folder_list import FolderList

# TODO update the JSON string below
json = "{}"
# create an instance of FolderList from a JSON string
folder_list_instance = FolderList.from_json(json)
# print the JSON string representation of the object
print(FolderList.to_json())

# convert the object into a dict
folder_list_dict = folder_list_instance.to_dict()
# create an instance of FolderList from a dict
folder_list_from_dict = FolderList.from_dict(folder_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


