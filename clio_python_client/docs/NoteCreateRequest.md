# NoteCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NoteCreateRequestData**](NoteCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.note_create_request import NoteCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCreateRequest from a JSON string
note_create_request_instance = NoteCreateRequest.from_json(json)
# print the JSON string representation of the object
print(NoteCreateRequest.to_json())

# convert the object into a dict
note_create_request_dict = note_create_request_instance.to_dict()
# create an instance of NoteCreateRequest from a dict
note_create_request_from_dict = NoteCreateRequest.from_dict(note_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


