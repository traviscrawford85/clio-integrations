# DocumentTemplateUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_category** | [**DocumentTemplateCreateRequestDataDocumentCategory**](DocumentTemplateCreateRequestDataDocumentCategory.md) |  | [optional] 
**file** | **str** | A file that contains the DocumentTemplate. The file can be uploaded through a form as application/x-www-form-urlencoded or multipart/form-data request. Alternatively, the file can be converted to a BASE64-encoded string and serialized to JSON.  | [optional] 
**filename** | **str** | The name of the file. The field is required when the file is BASE64-encoded string. | [optional] 

## Example

```python
from openapi_client.models.document_template_update_request_data import DocumentTemplateUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateUpdateRequestData from a JSON string
document_template_update_request_data_instance = DocumentTemplateUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateUpdateRequestData.to_json())

# convert the object into a dict
document_template_update_request_data_dict = document_template_update_request_data_instance.to_dict()
# create an instance of DocumentTemplateUpdateRequestData from a dict
document_template_update_request_data_from_dict = DocumentTemplateUpdateRequestData.from_dict(document_template_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


