# DocumentCategoryCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentCategoryCreateRequestData**](DocumentCategoryCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_category_create_request import DocumentCategoryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryCreateRequest from a JSON string
document_category_create_request_instance = DocumentCategoryCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryCreateRequest.to_json())

# convert the object into a dict
document_category_create_request_dict = document_category_create_request_instance.to_dict()
# create an instance of DocumentCategoryCreateRequest from a dict
document_category_create_request_from_dict = DocumentCategoryCreateRequest.from_dict(document_category_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


