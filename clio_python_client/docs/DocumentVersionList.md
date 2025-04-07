# DocumentVersionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentVersion]**](DocumentVersion.md) | DocumentVersion List Response | 

## Example

```python
from openapi_client.models.document_version_list import DocumentVersionList

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVersionList from a JSON string
document_version_list_instance = DocumentVersionList.from_json(json)
# print the JSON string representation of the object
print(DocumentVersionList.to_json())

# convert the object into a dict
document_version_list_dict = document_version_list_instance.to_dict()
# create an instance of DocumentVersionList from a dict
document_version_list_from_dict = DocumentVersionList.from_dict(document_version_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


