# DocumentCopyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentCopyRequestData**](DocumentCopyRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_copy_request import DocumentCopyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCopyRequest from a JSON string
document_copy_request_instance = DocumentCopyRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCopyRequest.to_json())

# convert the object into a dict
document_copy_request_dict = document_copy_request_instance.to_dict()
# create an instance of DocumentCopyRequest from a dict
document_copy_request_from_dict = DocumentCopyRequest.from_dict(document_copy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


