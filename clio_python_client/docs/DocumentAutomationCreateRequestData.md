# DocumentAutomationCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_template** | [**DocumentAutomationCreateRequestDataDocumentTemplate**](DocumentAutomationCreateRequestDataDocumentTemplate.md) |  | 
**filename** | **str** | The filename the generated document should have. | 
**formats** | **List[str]** | The formats the document should be generated as. It can either be generated as a PDF and/or in whatever type the document template is. | 
**matter** | [**DocumentAutomationCreateRequestDataMatter**](DocumentAutomationCreateRequestDataMatter.md) |  | 

## Example

```python
from openapi_client.models.document_automation_create_request_data import DocumentAutomationCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutomationCreateRequestData from a JSON string
document_automation_create_request_data_instance = DocumentAutomationCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentAutomationCreateRequestData.to_json())

# convert the object into a dict
document_automation_create_request_data_dict = document_automation_create_request_data_instance.to_dict()
# create an instance of DocumentAutomationCreateRequestData from a dict
document_automation_create_request_data_from_dict = DocumentAutomationCreateRequestData.from_dict(document_automation_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


