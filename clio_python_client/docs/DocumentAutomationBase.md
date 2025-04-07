# DocumentAutomationBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *DocumentAutomation* | [optional] 
**etag** | **str** | ETag for the *DocumentAutomation* | [optional] 
**state** | **str** | A text description of what the automation is currently doing | [optional] 
**export_formats** | **str** | An array of what formats were requested | [optional] 
**filename** | **str** | The name of the file being generated. | [optional] 
**created_at** | **datetime** | The time the *DocumentAutomation* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *DocumentAutomation* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.document_automation_base import DocumentAutomationBase

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutomationBase from a JSON string
document_automation_base_instance = DocumentAutomationBase.from_json(json)
# print the JSON string representation of the object
print(DocumentAutomationBase.to_json())

# convert the object into a dict
document_automation_base_dict = document_automation_base_instance.to_dict()
# create an instance of DocumentAutomationBase from a dict
document_automation_base_from_dict = DocumentAutomationBase.from_dict(document_automation_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


