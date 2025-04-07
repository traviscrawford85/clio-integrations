# DocumentCreateRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per Document** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 

## Example

```python
from openapi_client.models.document_create_request_data_external_properties_inner import DocumentCreateRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateRequestDataExternalPropertiesInner from a JSON string
document_create_request_data_external_properties_inner_instance = DocumentCreateRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
document_create_request_data_external_properties_inner_dict = document_create_request_data_external_properties_inner_instance.to_dict()
# create an instance of DocumentCreateRequestDataExternalPropertiesInner from a dict
document_create_request_data_external_properties_inner_from_dict = DocumentCreateRequestDataExternalPropertiesInner.from_dict(document_create_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


