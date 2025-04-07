# CalendarEntryUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **str** | Flag to delete a specific instance of a recurring event. | [optional] 
**all_day** | **bool** | Whether or not the CalendarEntry is for all day. | [optional] 
**attendees** | [**List[CalendarEntryCreateRequestDataAttendeesInner]**](CalendarEntryCreateRequestDataAttendeesInner.md) |  | [optional] 
**calendar_entry_event_type** | [**CalendarEntryCreateRequestDataCalendarEntryEventType**](CalendarEntryCreateRequestDataCalendarEntryEventType.md) |  | [optional] 
**calendar_owner** | [**CalendarEntryUpdateRequestDataCalendarOwner**](CalendarEntryUpdateRequestDataCalendarOwner.md) |  | [optional] 
**conference_meeting** | [**CalendarEntryCreateRequestDataConferenceMeeting**](CalendarEntryCreateRequestDataConferenceMeeting.md) |  | [optional] 
**description** | **str** | A detailed description of the CalendarEntry. | [optional] 
**end_at** | **datetime** | The time the CalendarEntry ends (Expects an ISO-8601 timestamp). | [optional] 
**external_properties** | [**List[CalendarEntryUpdateRequestDataExternalPropertiesInner]**](CalendarEntryUpdateRequestDataExternalPropertiesInner.md) |  | [optional] 
**location** | **str** | The geographic location of the CalendarEntry. | [optional] 
**matter** | [**CalendarEntryCreateRequestDataMatter**](CalendarEntryCreateRequestDataMatter.md) |  | [optional] 
**recurrence_rule** | **str** | Recurrence rule for expanding recurring CalendarEntry. To convert an existing recurring event to a non-recurring event, &#x60;&#39;&#39;&#x60; or &#x60;null&#x60; are valid values. | [optional] 
**send_email_notification** | **bool** | Whether the calendar Entry should send email notifications to attendees | [optional] 
**start_at** | **datetime** | The time the CalendarEntry starts (Expects an ISO-8601 timestamp). | [optional] 
**summary** | **str** | A short summary of the CalendarEntry. | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_update_request_data import CalendarEntryUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryUpdateRequestData from a JSON string
calendar_entry_update_request_data_instance = CalendarEntryUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryUpdateRequestData.to_json())

# convert the object into a dict
calendar_entry_update_request_data_dict = calendar_entry_update_request_data_instance.to_dict()
# create an instance of CalendarEntryUpdateRequestData from a dict
calendar_entry_update_request_data_from_dict = CalendarEntryUpdateRequestData.from_dict(calendar_entry_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


