# CalendarEntryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CalendarEntry]**](CalendarEntry.md) | CalendarEntry List Response | 

## Example

```python
from openapi_client.models.calendar_entry_list import CalendarEntryList

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryList from a JSON string
calendar_entry_list_instance = CalendarEntryList.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryList.to_json())

# convert the object into a dict
calendar_entry_list_dict = calendar_entry_list_instance.to_dict()
# create an instance of CalendarEntryList from a dict
calendar_entry_list_from_dict = CalendarEntryList.from_dict(calendar_entry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


