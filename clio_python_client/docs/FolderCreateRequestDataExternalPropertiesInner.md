# FolderCreateRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per Folder** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 

## Example

```python
from openapi_client.models.folder_create_request_data_external_properties_inner import FolderCreateRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCreateRequestDataExternalPropertiesInner from a JSON string
folder_create_request_data_external_properties_inner_instance = FolderCreateRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(FolderCreateRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
folder_create_request_data_external_properties_inner_dict = folder_create_request_data_external_properties_inner_instance.to_dict()
# create an instance of FolderCreateRequestDataExternalPropertiesInner from a dict
folder_create_request_data_external_properties_inner_from_dict = FolderCreateRequestDataExternalPropertiesInner.from_dict(folder_create_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


