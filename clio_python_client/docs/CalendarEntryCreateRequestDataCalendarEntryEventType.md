# CalendarEntryCreateRequestDataCalendarEntryEventType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single CalendarEntryEventType associated with the CalendarEntry. Use the keyword &#x60;null&#x60; to specify no association. | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_create_request_data_calendar_entry_event_type import CalendarEntryCreateRequestDataCalendarEntryEventType

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryCreateRequestDataCalendarEntryEventType from a JSON string
calendar_entry_create_request_data_calendar_entry_event_type_instance = CalendarEntryCreateRequestDataCalendarEntryEventType.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryCreateRequestDataCalendarEntryEventType.to_json())

# convert the object into a dict
calendar_entry_create_request_data_calendar_entry_event_type_dict = calendar_entry_create_request_data_calendar_entry_event_type_instance.to_dict()
# create an instance of CalendarEntryCreateRequestDataCalendarEntryEventType from a dict
calendar_entry_create_request_data_calendar_entry_event_type_from_dict = CalendarEntryCreateRequestDataCalendarEntryEventType.from_dict(calendar_entry_create_request_data_calendar_entry_event_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


