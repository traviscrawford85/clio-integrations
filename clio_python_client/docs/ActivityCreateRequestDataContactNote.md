# ActivityCreateRequestDataContactNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Note associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_contact_note import ActivityCreateRequestDataContactNote

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataContactNote from a JSON string
activity_create_request_data_contact_note_instance = ActivityCreateRequestDataContactNote.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataContactNote.to_json())

# convert the object into a dict
activity_create_request_data_contact_note_dict = activity_create_request_data_contact_note_instance.to_dict()
# create an instance of ActivityCreateRequestDataContactNote from a dict
activity_create_request_data_contact_note_from_dict = ActivityCreateRequestDataContactNote.from_dict(activity_create_request_data_contact_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


