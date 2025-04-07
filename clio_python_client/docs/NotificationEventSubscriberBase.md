# NotificationEventSubscriberBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *NotificationEventSubscriber* | [optional] 
**etag** | **str** | ETag for the *NotificationEventSubscriber* | [optional] 
**user_id** | **int** | The unique identifier for a User added as a notification event subscriber to the NotificationEventSubscriber | [optional] 
**name** | **str** | The User name added as a notification event subscriber to the NotificationEventSubscriber | [optional] 
**created_at** | **datetime** | The time the *NotificationEventSubscriber* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *NotificationEventSubscriber* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.notification_event_subscriber_base import NotificationEventSubscriberBase

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventSubscriberBase from a JSON string
notification_event_subscriber_base_instance = NotificationEventSubscriberBase.from_json(json)
# print the JSON string representation of the object
print(NotificationEventSubscriberBase.to_json())

# convert the object into a dict
notification_event_subscriber_base_dict = notification_event_subscriber_base_instance.to_dict()
# create an instance of NotificationEventSubscriberBase from a dict
notification_event_subscriber_base_from_dict = NotificationEventSubscriberBase.from_dict(notification_event_subscriber_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


