# ActivityCalendarEntryBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the *CalendarEntry* | [optional] 
**etag** | **str** | ETag for the *CalendarEntry* | [optional] 
**calendar_owner_id** | **int** | The id of the calendar owner. | [optional] 

## Example

```python
from openapi_client.models.activity_calendar_entry_base import ActivityCalendarEntryBase

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCalendarEntryBase from a JSON string
activity_calendar_entry_base_instance = ActivityCalendarEntryBase.from_json(json)
# print the JSON string representation of the object
print(ActivityCalendarEntryBase.to_json())

# convert the object into a dict
activity_calendar_entry_base_dict = activity_calendar_entry_base_instance.to_dict()
# create an instance of ActivityCalendarEntryBase from a dict
activity_calendar_entry_base_from_dict = ActivityCalendarEntryBase.from_dict(activity_calendar_entry_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


