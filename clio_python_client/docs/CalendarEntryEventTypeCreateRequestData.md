# CalendarEntryEventTypeCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The color assigned to the CalendarEntryEventType | 
**name** | **str** | The name of the CalendarEntryEventType | 

## Example

```python
from openapi_client.models.calendar_entry_event_type_create_request_data import CalendarEntryEventTypeCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryEventTypeCreateRequestData from a JSON string
calendar_entry_event_type_create_request_data_instance = CalendarEntryEventTypeCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryEventTypeCreateRequestData.to_json())

# convert the object into a dict
calendar_entry_event_type_create_request_data_dict = calendar_entry_event_type_create_request_data_instance.to_dict()
# create an instance of CalendarEntryEventTypeCreateRequestData from a dict
calendar_entry_event_type_create_request_data_from_dict = CalendarEntryEventTypeCreateRequestData.from_dict(calendar_entry_event_type_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


