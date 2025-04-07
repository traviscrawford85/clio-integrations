# DocumentTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentTemplate]**](DocumentTemplate.md) | DocumentTemplate List Response | 

## Example

```python
from openapi_client.models.document_template_list import DocumentTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateList from a JSON string
document_template_list_instance = DocumentTemplateList.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateList.to_json())

# convert the object into a dict
document_template_list_dict = document_template_list_instance.to_dict()
# create an instance of DocumentTemplateList from a dict
document_template_list_from_dict = DocumentTemplateList.from_dict(document_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


