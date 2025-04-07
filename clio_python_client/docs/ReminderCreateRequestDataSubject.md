# ReminderCreateRequestDataSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single CalendarEntry and Task associated with the Reminder. The keyword &#x60;null&#x60; is not valid for this field. | 
**type** | **str** | Model type of the Subject. | 

## Example

```python
from openapi_client.models.reminder_create_request_data_subject import ReminderCreateRequestDataSubject

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderCreateRequestDataSubject from a JSON string
reminder_create_request_data_subject_instance = ReminderCreateRequestDataSubject.from_json(json)
# print the JSON string representation of the object
print(ReminderCreateRequestDataSubject.to_json())

# convert the object into a dict
reminder_create_request_data_subject_dict = reminder_create_request_data_subject_instance.to_dict()
# create an instance of ReminderCreateRequestDataSubject from a dict
reminder_create_request_data_subject_from_dict = ReminderCreateRequestDataSubject.from_dict(reminder_create_request_data_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


