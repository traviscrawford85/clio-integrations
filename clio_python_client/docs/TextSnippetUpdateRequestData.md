# TextSnippetUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phrase** | **str** | The phrase expanded to from a TextSnippet. | [optional] 
**snippet** | **str** | The abbreviation that expands to a phrase. | [optional] 
**whole_word** | **bool** | Whether or not the TextSnippet requires a space after to trigger the expansion. | [optional] 

## Example

```python
from openapi_client.models.text_snippet_update_request_data import TextSnippetUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TextSnippetUpdateRequestData from a JSON string
text_snippet_update_request_data_instance = TextSnippetUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(TextSnippetUpdateRequestData.to_json())

# convert the object into a dict
text_snippet_update_request_data_dict = text_snippet_update_request_data_instance.to_dict()
# create an instance of TextSnippetUpdateRequestData from a dict
text_snippet_update_request_data_from_dict = TextSnippetUpdateRequestData.from_dict(text_snippet_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


