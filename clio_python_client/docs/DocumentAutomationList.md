# DocumentAutomationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentAutomation]**](DocumentAutomation.md) | DocumentAutomation List Response | 

## Example

```python
from openapi_client.models.document_automation_list import DocumentAutomationList

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutomationList from a JSON string
document_automation_list_instance = DocumentAutomationList.from_json(json)
# print the JSON string representation of the object
print(DocumentAutomationList.to_json())

# convert the object into a dict
document_automation_list_dict = document_automation_list_instance.to_dict()
# create an instance of DocumentAutomationList from a dict
document_automation_list_from_dict = DocumentAutomationList.from_dict(document_automation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


