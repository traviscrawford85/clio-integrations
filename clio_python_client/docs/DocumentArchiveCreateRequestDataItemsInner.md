# DocumentArchiveCreateRequestDataItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Document or Folder associated with the DocumentArchive. Use the keyword &#x60;null&#x60; to specify no association. | 
**type** | **int** | The type of the item to download | 

## Example

```python
from openapi_client.models.document_archive_create_request_data_items_inner import DocumentArchiveCreateRequestDataItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentArchiveCreateRequestDataItemsInner from a JSON string
document_archive_create_request_data_items_inner_instance = DocumentArchiveCreateRequestDataItemsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentArchiveCreateRequestDataItemsInner.to_json())

# convert the object into a dict
document_archive_create_request_data_items_inner_dict = document_archive_create_request_data_items_inner_instance.to_dict()
# create an instance of DocumentArchiveCreateRequestDataItemsInner from a dict
document_archive_create_request_data_items_inner_from_dict = DocumentArchiveCreateRequestDataItemsInner.from_dict(document_archive_create_request_data_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


