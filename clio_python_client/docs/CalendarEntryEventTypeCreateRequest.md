# CalendarEntryEventTypeCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CalendarEntryEventTypeCreateRequestData**](CalendarEntryEventTypeCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.calendar_entry_event_type_create_request import CalendarEntryEventTypeCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryEventTypeCreateRequest from a JSON string
calendar_entry_event_type_create_request_instance = CalendarEntryEventTypeCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryEventTypeCreateRequest.to_json())

# convert the object into a dict
calendar_entry_event_type_create_request_dict = calendar_entry_event_type_create_request_instance.to_dict()
# create an instance of CalendarEntryEventTypeCreateRequest from a dict
calendar_entry_event_type_create_request_from_dict = CalendarEntryEventTypeCreateRequest.from_dict(calendar_entry_event_type_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


