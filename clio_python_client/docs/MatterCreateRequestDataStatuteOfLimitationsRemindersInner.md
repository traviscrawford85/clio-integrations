# MatterCreateRequestDataStatuteOfLimitationsRemindersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_value** | **int** | Time measured in &#x60;duration_unit&#x60; to remind user before the subject. | 
**duration_unit** | **str** | Unit to measure the duration value in. | 
**notification_method** | [**MatterCreateRequestDataStatuteOfLimitationsRemindersInnerNotificationMethod**](MatterCreateRequestDataStatuteOfLimitationsRemindersInnerNotificationMethod.md) |  | 

## Example

```python
from openapi_client.models.matter_create_request_data_statute_of_limitations_reminders_inner import MatterCreateRequestDataStatuteOfLimitationsRemindersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataStatuteOfLimitationsRemindersInner from a JSON string
matter_create_request_data_statute_of_limitations_reminders_inner_instance = MatterCreateRequestDataStatuteOfLimitationsRemindersInner.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataStatuteOfLimitationsRemindersInner.to_json())

# convert the object into a dict
matter_create_request_data_statute_of_limitations_reminders_inner_dict = matter_create_request_data_statute_of_limitations_reminders_inner_instance.to_dict()
# create an instance of MatterCreateRequestDataStatuteOfLimitationsRemindersInner from a dict
matter_create_request_data_statute_of_limitations_reminders_inner_from_dict = MatterCreateRequestDataStatuteOfLimitationsRemindersInner.from_dict(matter_create_request_data_statute_of_limitations_reminders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


