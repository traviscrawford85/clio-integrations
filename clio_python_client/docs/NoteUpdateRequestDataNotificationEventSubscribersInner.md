# NoteUpdateRequestDataNotificationEventSubscribersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The unique identifier for a User to be added as a notification event subscriber to the Note. | [optional] 
**id** | **int** | Unique id of this Note. | [optional] 
**destroy** | **bool** | Whether or not the notification event subscriber should be deleted. | [optional] 

## Example

```python
from openapi_client.models.note_update_request_data_notification_event_subscribers_inner import NoteUpdateRequestDataNotificationEventSubscribersInner

# TODO update the JSON string below
json = "{}"
# create an instance of NoteUpdateRequestDataNotificationEventSubscribersInner from a JSON string
note_update_request_data_notification_event_subscribers_inner_instance = NoteUpdateRequestDataNotificationEventSubscribersInner.from_json(json)
# print the JSON string representation of the object
print(NoteUpdateRequestDataNotificationEventSubscribersInner.to_json())

# convert the object into a dict
note_update_request_data_notification_event_subscribers_inner_dict = note_update_request_data_notification_event_subscribers_inner_instance.to_dict()
# create an instance of NoteUpdateRequestDataNotificationEventSubscribersInner from a dict
note_update_request_data_notification_event_subscribers_inner_from_dict = NoteUpdateRequestDataNotificationEventSubscribersInner.from_dict(note_update_request_data_notification_event_subscribers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


