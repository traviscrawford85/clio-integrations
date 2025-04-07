# CommunicationCreateRequestDataNotificationEventSubscribersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The unique identifier for a User to be added as a notification event subscriber to the Phone Log Communication. Note: Only applicable to Phone Log Communications, invalid for other communication types. | 

## Example

```python
from openapi_client.models.communication_create_request_data_notification_event_subscribers_inner import CommunicationCreateRequestDataNotificationEventSubscribersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreateRequestDataNotificationEventSubscribersInner from a JSON string
communication_create_request_data_notification_event_subscribers_inner_instance = CommunicationCreateRequestDataNotificationEventSubscribersInner.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreateRequestDataNotificationEventSubscribersInner.to_json())

# convert the object into a dict
communication_create_request_data_notification_event_subscribers_inner_dict = communication_create_request_data_notification_event_subscribers_inner_instance.to_dict()
# create an instance of CommunicationCreateRequestDataNotificationEventSubscribersInner from a dict
communication_create_request_data_notification_event_subscribers_inner_from_dict = CommunicationCreateRequestDataNotificationEventSubscribersInner.from_dict(communication_create_request_data_notification_event_subscribers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


