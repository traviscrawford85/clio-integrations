# CalendarEntryCreateRequestDataCalendarOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Calendar associated with the CalendarEntry. The keyword &#x60;null&#x60; is not valid for this field. | 

## Example

```python
from openapi_client.models.calendar_entry_create_request_data_calendar_owner import CalendarEntryCreateRequestDataCalendarOwner

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryCreateRequestDataCalendarOwner from a JSON string
calendar_entry_create_request_data_calendar_owner_instance = CalendarEntryCreateRequestDataCalendarOwner.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryCreateRequestDataCalendarOwner.to_json())

# convert the object into a dict
calendar_entry_create_request_data_calendar_owner_dict = calendar_entry_create_request_data_calendar_owner_instance.to_dict()
# create an instance of CalendarEntryCreateRequestDataCalendarOwner from a dict
calendar_entry_create_request_data_calendar_owner_from_dict = CalendarEntryCreateRequestDataCalendarOwner.from_dict(calendar_entry_create_request_data_calendar_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


