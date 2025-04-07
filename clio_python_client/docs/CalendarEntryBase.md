# CalendarEntryBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the *CalendarEntry* | [optional] 
**etag** | **str** | ETag for the *CalendarEntry* | [optional] 
**summary** | **str** | A short summary of the *CalendarEntry* | [optional] 
**description** | **str** | A detailed description of the *CalendarEntry* | [optional] 
**location** | **str** | The geographic location of the *CalendarEntry* | [optional] 
**start_at** | **datetime** | The time the *CalendarEntry* starts (as an ISO-8601 timestamp) | [optional] 
**end_at** | **datetime** | The time the *CalendarEntry* ends (as an ISO-8601 timestamp) | [optional] 
**all_day** | **bool** | Whether the event is all day | [optional] 
**recurrence_rule** | **str** | Recurrence rule for expanding | [optional] 
**parent_calendar_entry_id** | **int** | Identifier for the parent *CalendarEntry* | [optional] 
**court_rule** | **bool** | Whether this event is associated with a Court Rule | [optional] 
**created_at** | **datetime** | The time the *CalendarEntry* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CalendarEntry* was last updated (as a ISO-8601 timestamp) | [optional] 
**permission** | **str** | The view permission for the current user, will return &#39;viewer&#39; when permission is &#39;limited_viewer&#39; and the user is an attendee. | [optional] 
**calendar_owner_id** | **int** | The id of the calendar owner. | [optional] 
**start_at_time_zone** | **str** | Original start at time zone of the event. | [optional] 
**time_entries_count** | **int** | The number of &#x60;TimeEntry&#x60; activities associated with the *CalendarEntry* | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_base import CalendarEntryBase

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryBase from a JSON string
calendar_entry_base_instance = CalendarEntryBase.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryBase.to_json())

# convert the object into a dict
calendar_entry_base_dict = calendar_entry_base_instance.to_dict()
# create an instance of CalendarEntryBase from a dict
calendar_entry_base_from_dict = CalendarEntryBase.from_dict(calendar_entry_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


