# DocumentCategoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentCategory]**](DocumentCategory.md) | DocumentCategory List Response | 

## Example

```python
from openapi_client.models.document_category_list import DocumentCategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryList from a JSON string
document_category_list_instance = DocumentCategoryList.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryList.to_json())

# convert the object into a dict
document_category_list_dict = document_category_list_instance.to_dict()
# create an instance of DocumentCategoryList from a dict
document_category_list_from_dict = DocumentCategoryList.from_dict(document_category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


