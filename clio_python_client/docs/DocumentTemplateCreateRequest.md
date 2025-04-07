# DocumentTemplateCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentTemplateCreateRequestData**](DocumentTemplateCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_template_create_request import DocumentTemplateCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateCreateRequest from a JSON string
document_template_create_request_instance = DocumentTemplateCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateCreateRequest.to_json())

# convert the object into a dict
document_template_create_request_dict = document_template_create_request_instance.to_dict()
# create an instance of DocumentTemplateCreateRequest from a dict
document_template_create_request_from_dict = DocumentTemplateCreateRequest.from_dict(document_template_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


