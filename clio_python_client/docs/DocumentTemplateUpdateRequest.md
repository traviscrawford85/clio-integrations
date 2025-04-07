# DocumentTemplateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentTemplateUpdateRequestData**](DocumentTemplateUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_template_update_request import DocumentTemplateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateUpdateRequest from a JSON string
document_template_update_request_instance = DocumentTemplateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateUpdateRequest.to_json())

# convert the object into a dict
document_template_update_request_dict = document_template_update_request_instance.to_dict()
# create an instance of DocumentTemplateUpdateRequest from a dict
document_template_update_request_from_dict = DocumentTemplateUpdateRequest.from_dict(document_template_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


