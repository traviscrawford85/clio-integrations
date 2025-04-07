# CalendarEntryCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CalendarEntryCreateRequestData**](CalendarEntryCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.calendar_entry_create_request import CalendarEntryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryCreateRequest from a JSON string
calendar_entry_create_request_instance = CalendarEntryCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryCreateRequest.to_json())

# convert the object into a dict
calendar_entry_create_request_dict = calendar_entry_create_request_instance.to_dict()
# create an instance of CalendarEntryCreateRequest from a dict
calendar_entry_create_request_from_dict = CalendarEntryCreateRequest.from_dict(calendar_entry_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


