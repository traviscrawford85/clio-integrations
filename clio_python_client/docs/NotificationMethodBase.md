# NotificationMethodBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *NotificationMethod* | [optional] 
**etag** | **str** | ETag for the *NotificationMethod* | [optional] 
**type** | **str** | Human readable description of the type of notification | [optional] 
**email_address** | **str** | Email address to send the notification to (only for email type) | [optional] 
**is_default_email_address** | **bool** | A boolean that is returned only on notification method objects that are relevant e.g. Email notification or Alternative Email | [optional] 
**created_at** | **datetime** | The time the *NotificationMethod* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *NotificationMethod* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.notification_method_base import NotificationMethodBase

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationMethodBase from a JSON string
notification_method_base_instance = NotificationMethodBase.from_json(json)
# print the JSON string representation of the object
print(NotificationMethodBase.to_json())

# convert the object into a dict
notification_method_base_dict = notification_method_base_instance.to_dict()
# create an instance of NotificationMethodBase from a dict
notification_method_base_from_dict = NotificationMethodBase.from_dict(notification_method_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


