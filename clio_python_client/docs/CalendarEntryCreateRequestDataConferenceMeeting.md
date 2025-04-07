# CalendarEntryCreateRequestDataConferenceMeeting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of conference meeting. If no conference meeting is present or the user is in an ineligible pricing tier for this feature, it will be null. | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_create_request_data_conference_meeting import CalendarEntryCreateRequestDataConferenceMeeting

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryCreateRequestDataConferenceMeeting from a JSON string
calendar_entry_create_request_data_conference_meeting_instance = CalendarEntryCreateRequestDataConferenceMeeting.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryCreateRequestDataConferenceMeeting.to_json())

# convert the object into a dict
calendar_entry_create_request_data_conference_meeting_dict = calendar_entry_create_request_data_conference_meeting_instance.to_dict()
# create an instance of CalendarEntryCreateRequestDataConferenceMeeting from a dict
calendar_entry_create_request_data_conference_meeting_from_dict = CalendarEntryCreateRequestDataConferenceMeeting.from_dict(calendar_entry_create_request_data_conference_meeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


