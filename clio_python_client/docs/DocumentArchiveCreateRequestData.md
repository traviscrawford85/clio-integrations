# DocumentArchiveCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DocumentArchiveCreateRequestDataItemsInner]**](DocumentArchiveCreateRequestDataItemsInner.md) |  | 

## Example

```python
from openapi_client.models.document_archive_create_request_data import DocumentArchiveCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentArchiveCreateRequestData from a JSON string
document_archive_create_request_data_instance = DocumentArchiveCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentArchiveCreateRequestData.to_json())

# convert the object into a dict
document_archive_create_request_data_dict = document_archive_create_request_data_instance.to_dict()
# create an instance of DocumentArchiveCreateRequestData from a dict
document_archive_create_request_data_from_dict = DocumentArchiveCreateRequestData.from_dict(document_archive_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


