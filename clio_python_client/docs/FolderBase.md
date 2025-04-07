# FolderBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Folder* | [optional] 
**etag** | **str** | ETag for the *Folder* | [optional] 
**created_at** | **datetime** | The time the *Folder* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Folder* was last updated (as a ISO-8601 timestamp) | [optional] 
**deleted_at** | **datetime** | The time the *Folder* was deleted (as a ISO-8601 timestamp) | [optional] 
**type** | **str** | The type of the *Folder* | [optional] 
**locked** | **bool** | Whether or not the Folder is locked. Locked Folder cannot be modified | [optional] 
**name** | **str** | The name of the Folder | [optional] 
**root** | **bool** | Whether or not the Folder is the root folder. There is only one root folder per account | [optional] 

## Example

```python
from openapi_client.models.folder_base import FolderBase

# TODO update the JSON string below
json = "{}"
# create an instance of FolderBase from a JSON string
folder_base_instance = FolderBase.from_json(json)
# print the JSON string representation of the object
print(FolderBase.to_json())

# convert the object into a dict
folder_base_dict = folder_base_instance.to_dict()
# create an instance of FolderBase from a dict
folder_base_from_dict = FolderBase.from_dict(folder_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


