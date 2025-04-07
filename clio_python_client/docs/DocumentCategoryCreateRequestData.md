# DocumentCategoryCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | What the DocumentCategory should be called. | 

## Example

```python
from openapi_client.models.document_category_create_request_data import DocumentCategoryCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryCreateRequestData from a JSON string
document_category_create_request_data_instance = DocumentCategoryCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryCreateRequestData.to_json())

# convert the object into a dict
document_category_create_request_data_dict = document_category_create_request_data_instance.to_dict()
# create an instance of DocumentCategoryCreateRequestData from a dict
document_category_create_request_data_from_dict = DocumentCategoryCreateRequestData.from_dict(document_category_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


