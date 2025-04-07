# NoteUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NoteUpdateRequestData**](NoteUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.note_update_request import NoteUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NoteUpdateRequest from a JSON string
note_update_request_instance = NoteUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NoteUpdateRequest.to_json())

# convert the object into a dict
note_update_request_dict = note_update_request_instance.to_dict()
# create an instance of NoteUpdateRequest from a dict
note_update_request_from_dict = NoteUpdateRequest.from_dict(note_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


