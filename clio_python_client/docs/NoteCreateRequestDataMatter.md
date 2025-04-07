# NoteCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the Note. The keyword null is not valid for this field. Required only if the Note type is &#x60;\&quot;Matter\&quot;&#x60;. | 

## Example

```python
from openapi_client.models.note_create_request_data_matter import NoteCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCreateRequestDataMatter from a JSON string
note_create_request_data_matter_instance = NoteCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(NoteCreateRequestDataMatter.to_json())

# convert the object into a dict
note_create_request_data_matter_dict = note_create_request_data_matter_instance.to_dict()
# create an instance of NoteCreateRequestDataMatter from a dict
note_create_request_data_matter_from_dict = NoteCreateRequestDataMatter.from_dict(note_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


