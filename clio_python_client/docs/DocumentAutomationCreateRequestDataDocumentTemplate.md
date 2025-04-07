# DocumentAutomationCreateRequestDataDocumentTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single DocumentTemplate associated with the DocumentAutomation. The keyword &#x60;null&#x60; is not valid for this field. | 

## Example

```python
from openapi_client.models.document_automation_create_request_data_document_template import DocumentAutomationCreateRequestDataDocumentTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutomationCreateRequestDataDocumentTemplate from a JSON string
document_automation_create_request_data_document_template_instance = DocumentAutomationCreateRequestDataDocumentTemplate.from_json(json)
# print the JSON string representation of the object
print(DocumentAutomationCreateRequestDataDocumentTemplate.to_json())

# convert the object into a dict
document_automation_create_request_data_document_template_dict = document_automation_create_request_data_document_template_instance.to_dict()
# create an instance of DocumentAutomationCreateRequestDataDocumentTemplate from a dict
document_automation_create_request_data_document_template_from_dict = DocumentAutomationCreateRequestDataDocumentTemplate.from_dict(document_automation_create_request_data_document_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


