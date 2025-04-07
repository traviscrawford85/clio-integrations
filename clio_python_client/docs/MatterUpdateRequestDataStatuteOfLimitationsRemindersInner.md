# MatterUpdateRequestDataStatuteOfLimitationsRemindersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_value** | **int** | Time measured in &#x60;duration_unit&#x60; to remind user before the subject. | [optional] 
**duration_unit** | **str** | Unit to measure the duration value in. | [optional] 
**notification_method** | [**MatterUpdateRequestDataStatuteOfLimitationsRemindersInnerNotificationMethod**](MatterUpdateRequestDataStatuteOfLimitationsRemindersInnerNotificationMethod.md) |  | [optional] 
**id** | **int** | The unique identifier for a single Reminder associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated Reminder is present, the Reminder is deleted from the Matter. | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_statute_of_limitations_reminders_inner import MatterUpdateRequestDataStatuteOfLimitationsRemindersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataStatuteOfLimitationsRemindersInner from a JSON string
matter_update_request_data_statute_of_limitations_reminders_inner_instance = MatterUpdateRequestDataStatuteOfLimitationsRemindersInner.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataStatuteOfLimitationsRemindersInner.to_json())

# convert the object into a dict
matter_update_request_data_statute_of_limitations_reminders_inner_dict = matter_update_request_data_statute_of_limitations_reminders_inner_instance.to_dict()
# create an instance of MatterUpdateRequestDataStatuteOfLimitationsRemindersInner from a dict
matter_update_request_data_statute_of_limitations_reminders_inner_from_dict = MatterUpdateRequestDataStatuteOfLimitationsRemindersInner.from_dict(matter_update_request_data_statute_of_limitations_reminders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


