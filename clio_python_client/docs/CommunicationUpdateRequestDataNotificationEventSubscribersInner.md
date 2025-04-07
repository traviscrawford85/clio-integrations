# CommunicationUpdateRequestDataNotificationEventSubscribersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The unique identifier for a User to be added as a notification event subscriber to the Phone Log Communication. Note: Only applicable to Phone Log Communications, invalid for other communication types. | [optional] 
**id** | **int** | Unique id of this Communication. Note: Only applicable to Phone Log Communications, invalid for other communication types. | [optional] 
**destroy** | **bool** | Whether or not the notification event subscriber should be deleted. Note: Only applicable to Phone Log Communications, invalid for other communication types. | [optional] 

## Example

```python
from openapi_client.models.communication_update_request_data_notification_event_subscribers_inner import CommunicationUpdateRequestDataNotificationEventSubscribersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationUpdateRequestDataNotificationEventSubscribersInner from a JSON string
communication_update_request_data_notification_event_subscribers_inner_instance = CommunicationUpdateRequestDataNotificationEventSubscribersInner.from_json(json)
# print the JSON string representation of the object
print(CommunicationUpdateRequestDataNotificationEventSubscribersInner.to_json())

# convert the object into a dict
communication_update_request_data_notification_event_subscribers_inner_dict = communication_update_request_data_notification_event_subscribers_inner_instance.to_dict()
# create an instance of CommunicationUpdateRequestDataNotificationEventSubscribersInner from a dict
communication_update_request_data_notification_event_subscribers_inner_from_dict = CommunicationUpdateRequestDataNotificationEventSubscribersInner.from_dict(communication_update_request_data_notification_event_subscribers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


