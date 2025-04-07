# TextSnippetBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TextSnippet* | [optional] 
**etag** | **str** | ETag for the *TextSnippet* | [optional] 
**created_at** | **datetime** | The time the *TextSnippet* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TextSnippet* was last updated (as a ISO-8601 timestamp) | [optional] 
**snippet** | **str** | The abbreviation that should be expanded | [optional] 
**phrase** | **str** | The phrase the abbreviation should be expanded to | [optional] 
**whole_word** | **bool** | Whether the *TextSnippet* abbreviation requires a space after it has been entered to expand to a phrase | [optional] 

## Example

```python
from openapi_client.models.text_snippet_base import TextSnippetBase

# TODO update the JSON string below
json = "{}"
# create an instance of TextSnippetBase from a JSON string
text_snippet_base_instance = TextSnippetBase.from_json(json)
# print the JSON string representation of the object
print(TextSnippetBase.to_json())

# convert the object into a dict
text_snippet_base_dict = text_snippet_base_instance.to_dict()
# create an instance of TextSnippetBase from a dict
text_snippet_base_from_dict = TextSnippetBase.from_dict(text_snippet_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


