# CalendarEntryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CalendarEntryUpdateRequestData**](CalendarEntryUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.calendar_entry_update_request import CalendarEntryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryUpdateRequest from a JSON string
calendar_entry_update_request_instance = CalendarEntryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryUpdateRequest.to_json())

# convert the object into a dict
calendar_entry_update_request_dict = calendar_entry_update_request_instance.to_dict()
# create an instance of CalendarEntryUpdateRequest from a dict
calendar_entry_update_request_from_dict = CalendarEntryUpdateRequest.from_dict(calendar_entry_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


