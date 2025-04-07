# FolderUpdateRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single ExternalProperty associated with the Folder. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per Folder** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated ExternalProperty is present, the ExternalProperty is deleted from the Folder. | [optional] 

## Example

```python
from openapi_client.models.folder_update_request_data_external_properties_inner import FolderUpdateRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUpdateRequestDataExternalPropertiesInner from a JSON string
folder_update_request_data_external_properties_inner_instance = FolderUpdateRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(FolderUpdateRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
folder_update_request_data_external_properties_inner_dict = folder_update_request_data_external_properties_inner_instance.to_dict()
# create an instance of FolderUpdateRequestDataExternalPropertiesInner from a dict
folder_update_request_data_external_properties_inner_from_dict = FolderUpdateRequestDataExternalPropertiesInner.from_dict(folder_update_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


