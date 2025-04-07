# DocumentTemplateCreateRequestDataDocumentCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single DocumentCategory associated with the DocumentTemplate. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.document_template_create_request_data_document_category import DocumentTemplateCreateRequestDataDocumentCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateCreateRequestDataDocumentCategory from a JSON string
document_template_create_request_data_document_category_instance = DocumentTemplateCreateRequestDataDocumentCategory.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateCreateRequestDataDocumentCategory.to_json())

# convert the object into a dict
document_template_create_request_data_document_category_dict = document_template_create_request_data_document_category_instance.to_dict()
# create an instance of DocumentTemplateCreateRequestDataDocumentCategory from a dict
document_template_create_request_data_document_category_from_dict = DocumentTemplateCreateRequestDataDocumentCategory.from_dict(document_template_create_request_data_document_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


