# NoteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Note]**](Note.md) | Note List Response | 

## Example

```python
from openapi_client.models.note_list import NoteList

# TODO update the JSON string below
json = "{}"
# create an instance of NoteList from a JSON string
note_list_instance = NoteList.from_json(json)
# print the JSON string representation of the object
print(NoteList.to_json())

# convert the object into a dict
note_list_dict = note_list_instance.to_dict()
# create an instance of NoteList from a dict
note_list_from_dict = NoteList.from_dict(note_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


