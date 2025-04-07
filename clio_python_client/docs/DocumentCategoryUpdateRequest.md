# DocumentCategoryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentCategoryUpdateRequestData**](DocumentCategoryUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.document_category_update_request import DocumentCategoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryUpdateRequest from a JSON string
document_category_update_request_instance = DocumentCategoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryUpdateRequest.to_json())

# convert the object into a dict
document_category_update_request_dict = document_category_update_request_instance.to_dict()
# create an instance of DocumentCategoryUpdateRequest from a dict
document_category_update_request_from_dict = DocumentCategoryUpdateRequest.from_dict(document_category_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


