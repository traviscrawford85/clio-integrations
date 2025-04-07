# DocumentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentUpdateRequestData**](DocumentUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_update_request import DocumentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequest from a JSON string
document_update_request_instance = DocumentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequest.to_json())

# convert the object into a dict
document_update_request_dict = document_update_request_instance.to_dict()
# create an instance of DocumentUpdateRequest from a dict
document_update_request_from_dict = DocumentUpdateRequest.from_dict(document_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


