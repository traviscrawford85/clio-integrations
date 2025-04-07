# DocumentAutomationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentAutomationCreateRequestData**](DocumentAutomationCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_automation_create_request import DocumentAutomationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutomationCreateRequest from a JSON string
document_automation_create_request_instance = DocumentAutomationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentAutomationCreateRequest.to_json())

# convert the object into a dict
document_automation_create_request_dict = document_automation_create_request_instance.to_dict()
# create an instance of DocumentAutomationCreateRequest from a dict
document_automation_create_request_from_dict = DocumentAutomationCreateRequest.from_dict(document_automation_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


