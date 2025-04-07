# NoteUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date for the Note. (Expects an ISO-8601 date). | [optional] 
**detail** | **str** | Note body. | [optional] 
**notification_event_subscribers** | [**List[NoteUpdateRequestDataNotificationEventSubscribersInner]**](NoteUpdateRequestDataNotificationEventSubscribersInner.md) |  | [optional] 
**subject** | **str** | Note subject. | [optional] 

## Example

```python
from openapi_client.models.note_update_request_data import NoteUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of NoteUpdateRequestData from a JSON string
note_update_request_data_instance = NoteUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(NoteUpdateRequestData.to_json())

# convert the object into a dict
note_update_request_data_dict = note_update_request_data_instance.to_dict()
# create an instance of NoteUpdateRequestData from a dict
note_update_request_data_from_dict = NoteUpdateRequestData.from_dict(note_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


