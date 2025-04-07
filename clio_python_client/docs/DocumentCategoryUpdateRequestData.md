# DocumentCategoryUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | What the DocumentCategory should be called. | [optional] 

## Example

```python
from openapi_client.models.document_category_update_request_data import DocumentCategoryUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryUpdateRequestData from a JSON string
document_category_update_request_data_instance = DocumentCategoryUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryUpdateRequestData.to_json())

# convert the object into a dict
document_category_update_request_data_dict = document_category_update_request_data_instance.to_dict()
# create an instance of DocumentCategoryUpdateRequestData from a dict
document_category_update_request_data_from_dict = DocumentCategoryUpdateRequestData.from_dict(document_category_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


