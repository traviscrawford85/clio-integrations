# TextSnippetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TextSnippet]**](TextSnippet.md) | TextSnippet List Response | 

## Example

```python
from openapi_client.models.text_snippet_list import TextSnippetList

# TODO update the JSON string below
json = "{}"
# create an instance of TextSnippetList from a JSON string
text_snippet_list_instance = TextSnippetList.from_json(json)
# print the JSON string representation of the object
print(TextSnippetList.to_json())

# convert the object into a dict
text_snippet_list_dict = text_snippet_list_instance.to_dict()
# create an instance of TextSnippetList from a dict
text_snippet_list_from_dict = TextSnippetList.from_dict(text_snippet_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


