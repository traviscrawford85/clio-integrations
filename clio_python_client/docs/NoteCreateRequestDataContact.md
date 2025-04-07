# NoteCreateRequestDataContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Contact associated with the Note. The keyword null is not valid for this field. Required only if the Note type is &#x60;\&quot;Contact\&quot;&#x60;. | 

## Example

```python
from openapi_client.models.note_create_request_data_contact import NoteCreateRequestDataContact

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCreateRequestDataContact from a JSON string
note_create_request_data_contact_instance = NoteCreateRequestDataContact.from_json(json)
# print the JSON string representation of the object
print(NoteCreateRequestDataContact.to_json())

# convert the object into a dict
note_create_request_data_contact_dict = note_create_request_data_contact_instance.to_dict()
# create an instance of NoteCreateRequestDataContact from a dict
note_create_request_data_contact_from_dict = NoteCreateRequestDataContact.from_dict(note_create_request_data_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


