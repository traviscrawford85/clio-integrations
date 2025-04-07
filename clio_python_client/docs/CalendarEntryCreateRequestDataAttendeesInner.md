# CalendarEntryCreateRequestDataAttendeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Attendee associated with the CalendarEntry. The keyword &#x60;null&#x60; is not valid for this field. Not required for creating new Attendee, but required for updating or deleting existing ones. | [optional] 
**type** | **str** | The type of attendee (Calendar, Contact) | [optional] 
**destroy** | **bool** | Flag to delete a specific attendee. | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_create_request_data_attendees_inner import CalendarEntryCreateRequestDataAttendeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryCreateRequestDataAttendeesInner from a JSON string
calendar_entry_create_request_data_attendees_inner_instance = CalendarEntryCreateRequestDataAttendeesInner.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryCreateRequestDataAttendeesInner.to_json())

# convert the object into a dict
calendar_entry_create_request_data_attendees_inner_dict = calendar_entry_create_request_data_attendees_inner_instance.to_dict()
# create an instance of CalendarEntryCreateRequestDataAttendeesInner from a dict
calendar_entry_create_request_data_attendees_inner_from_dict = CalendarEntryCreateRequestDataAttendeesInner.from_dict(calendar_entry_create_request_data_attendees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


