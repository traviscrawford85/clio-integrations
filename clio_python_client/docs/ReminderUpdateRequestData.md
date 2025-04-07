# ReminderUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_unit** | **str** | Unit to measure the duration value in. | [optional] 
**duration_value** | **int** | Time measured in &#x60;duration_unit&#x60; to remind user before the subject. | [optional] 
**notification_method** | [**MatterUpdateRequestDataStatuteOfLimitationsRemindersInnerNotificationMethod**](MatterUpdateRequestDataStatuteOfLimitationsRemindersInnerNotificationMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.reminder_update_request_data import ReminderUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderUpdateRequestData from a JSON string
reminder_update_request_data_instance = ReminderUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ReminderUpdateRequestData.to_json())

# convert the object into a dict
reminder_update_request_data_dict = reminder_update_request_data_instance.to_dict()
# create an instance of ReminderUpdateRequestData from a dict
reminder_update_request_data_from_dict = ReminderUpdateRequestData.from_dict(reminder_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


