# CalendarEntryUpdateRequestDataCalendarOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Calendar associated with the CalendarEntry. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_update_request_data_calendar_owner import CalendarEntryUpdateRequestDataCalendarOwner

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryUpdateRequestDataCalendarOwner from a JSON string
calendar_entry_update_request_data_calendar_owner_instance = CalendarEntryUpdateRequestDataCalendarOwner.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryUpdateRequestDataCalendarOwner.to_json())

# convert the object into a dict
calendar_entry_update_request_data_calendar_owner_dict = calendar_entry_update_request_data_calendar_owner_instance.to_dict()
# create an instance of CalendarEntryUpdateRequestDataCalendarOwner from a dict
calendar_entry_update_request_data_calendar_owner_from_dict = CalendarEntryUpdateRequestDataCalendarOwner.from_dict(calendar_entry_update_request_data_calendar_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


