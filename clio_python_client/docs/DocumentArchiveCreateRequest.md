# DocumentArchiveCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentArchiveCreateRequestData**](DocumentArchiveCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_archive_create_request import DocumentArchiveCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentArchiveCreateRequest from a JSON string
document_archive_create_request_instance = DocumentArchiveCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentArchiveCreateRequest.to_json())

# convert the object into a dict
document_archive_create_request_dict = document_archive_create_request_instance.to_dict()
# create an instance of DocumentArchiveCreateRequest from a dict
document_archive_create_request_from_dict = DocumentArchiveCreateRequest.from_dict(document_archive_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


