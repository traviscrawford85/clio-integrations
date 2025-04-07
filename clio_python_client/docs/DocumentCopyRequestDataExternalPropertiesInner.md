# DocumentCopyRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single ExternalProperty associated with the Document. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per Document** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated ExternalProperty is present, the ExternalProperty is deleted from the Document. | [optional] 

## Example

```python
from openapi_client.models.document_copy_request_data_external_properties_inner import DocumentCopyRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCopyRequestDataExternalPropertiesInner from a JSON string
document_copy_request_data_external_properties_inner_instance = DocumentCopyRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCopyRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
document_copy_request_data_external_properties_inner_dict = document_copy_request_data_external_properties_inner_instance.to_dict()
# create an instance of DocumentCopyRequestDataExternalPropertiesInner from a dict
document_copy_request_data_external_properties_inner_from_dict = DocumentCopyRequestDataExternalPropertiesInner.from_dict(document_copy_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


