# CalendarEntryEventType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CalendarEntryEventType* | [optional] 
**etag** | **str** | ETag for the *CalendarEntryEventType* | [optional] 
**created_at** | **datetime** | The time the *CalendarEntryEventType* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CalendarEntryEventType* was last updated (as a ISO-8601 timestamp) | [optional] 
**color** | **str** | The color describing the *CalendarEntryEventType* | [optional] 
**name** | **str** | The name for the *CalendarEntryEventType* | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_event_type import CalendarEntryEventType

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryEventType from a JSON string
calendar_entry_event_type_instance = CalendarEntryEventType.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryEventType.to_json())

# convert the object into a dict
calendar_entry_event_type_dict = calendar_entry_event_type_instance.to_dict()
# create an instance of CalendarEntryEventType from a dict
calendar_entry_event_type_from_dict = CalendarEntryEventType.from_dict(calendar_entry_event_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


