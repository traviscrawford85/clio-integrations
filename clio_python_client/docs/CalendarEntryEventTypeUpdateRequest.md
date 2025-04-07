# CalendarEntryEventTypeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CalendarEntryEventTypeUpdateRequestData**](CalendarEntryEventTypeUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.calendar_entry_event_type_update_request import CalendarEntryEventTypeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryEventTypeUpdateRequest from a JSON string
calendar_entry_event_type_update_request_instance = CalendarEntryEventTypeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryEventTypeUpdateRequest.to_json())

# convert the object into a dict
calendar_entry_event_type_update_request_dict = calendar_entry_event_type_update_request_instance.to_dict()
# create an instance of CalendarEntryEventTypeUpdateRequest from a dict
calendar_entry_event_type_update_request_from_dict = CalendarEntryEventTypeUpdateRequest.from_dict(calendar_entry_event_type_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


