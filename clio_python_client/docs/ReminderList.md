# ReminderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Reminder]**](Reminder.md) | Reminder List Response | 

## Example

```python
from openapi_client.models.reminder_list import ReminderList

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderList from a JSON string
reminder_list_instance = ReminderList.from_json(json)
# print the JSON string representation of the object
print(ReminderList.to_json())

# convert the object into a dict
reminder_list_dict = reminder_list_instance.to_dict()
# create an instance of ReminderList from a dict
reminder_list_from_dict = ReminderList.from_dict(reminder_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


