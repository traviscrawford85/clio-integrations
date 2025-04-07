# TextSnippetCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phrase** | **str** | The phrase expanded to from a TextSnippet. | 
**snippet** | **str** | The abbreviation that expands to a phrase. | 
**whole_word** | **bool** | Whether or not the TextSnippet requires a space after to trigger the expansion. | [optional] 

## Example

```python
from openapi_client.models.text_snippet_create_request_data import TextSnippetCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TextSnippetCreateRequestData from a JSON string
text_snippet_create_request_data_instance = TextSnippetCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TextSnippetCreateRequestData.to_json())

# convert the object into a dict
text_snippet_create_request_data_dict = text_snippet_create_request_data_instance.to_dict()
# create an instance of TextSnippetCreateRequestData from a dict
text_snippet_create_request_data_from_dict = TextSnippetCreateRequestData.from_dict(text_snippet_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


