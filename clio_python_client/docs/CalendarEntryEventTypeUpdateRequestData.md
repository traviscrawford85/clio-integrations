# CalendarEntryEventTypeUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The color assigned to the CalendarEntryEventType | [optional] 
**name** | **str** | The name of the CalendarEntryEventType | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_event_type_update_request_data import CalendarEntryEventTypeUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryEventTypeUpdateRequestData from a JSON string
calendar_entry_event_type_update_request_data_instance = CalendarEntryEventTypeUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryEventTypeUpdateRequestData.to_json())

# convert the object into a dict
calendar_entry_event_type_update_request_data_dict = calendar_entry_event_type_update_request_data_instance.to_dict()
# create an instance of CalendarEntryEventTypeUpdateRequestData from a dict
calendar_entry_event_type_update_request_data_from_dict = CalendarEntryEventTypeUpdateRequestData.from_dict(calendar_entry_event_type_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


