# DocumentCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentCreateRequestData**](DocumentCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_create_request import DocumentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateRequest from a JSON string
document_create_request_instance = DocumentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateRequest.to_json())

# convert the object into a dict
document_create_request_dict = document_create_request_instance.to_dict()
# create an instance of DocumentCreateRequest from a dict
document_create_request_from_dict = DocumentCreateRequest.from_dict(document_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


