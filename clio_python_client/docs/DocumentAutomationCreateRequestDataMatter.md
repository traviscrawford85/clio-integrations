# DocumentAutomationCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the DocumentAutomation. The keyword &#x60;null&#x60; is not valid for this field. | 

## Example

```python
from openapi_client.models.document_automation_create_request_data_matter import DocumentAutomationCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutomationCreateRequestDataMatter from a JSON string
document_automation_create_request_data_matter_instance = DocumentAutomationCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(DocumentAutomationCreateRequestDataMatter.to_json())

# convert the object into a dict
document_automation_create_request_data_matter_dict = document_automation_create_request_data_matter_instance.to_dict()
# create an instance of DocumentAutomationCreateRequestDataMatter from a dict
document_automation_create_request_data_matter_from_dict = DocumentAutomationCreateRequestDataMatter.from_dict(document_automation_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


