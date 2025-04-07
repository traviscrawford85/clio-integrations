# TextSnippetUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TextSnippetUpdateRequestData**](TextSnippetUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.text_snippet_update_request import TextSnippetUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextSnippetUpdateRequest from a JSON string
text_snippet_update_request_instance = TextSnippetUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TextSnippetUpdateRequest.to_json())

# convert the object into a dict
text_snippet_update_request_dict = text_snippet_update_request_instance.to_dict()
# create an instance of TextSnippetUpdateRequest from a dict
text_snippet_update_request_from_dict = TextSnippetUpdateRequest.from_dict(text_snippet_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


