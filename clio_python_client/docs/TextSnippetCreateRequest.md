# TextSnippetCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TextSnippetCreateRequestData**](TextSnippetCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.text_snippet_create_request import TextSnippetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextSnippetCreateRequest from a JSON string
text_snippet_create_request_instance = TextSnippetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TextSnippetCreateRequest.to_json())

# convert the object into a dict
text_snippet_create_request_dict = text_snippet_create_request_instance.to_dict()
# create an instance of TextSnippetCreateRequest from a dict
text_snippet_create_request_from_dict = TextSnippetCreateRequest.from_dict(text_snippet_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


