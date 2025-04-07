# ActivityCreateRequestDataCalendarEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single CalendarEntry associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_calendar_entry import ActivityCreateRequestDataCalendarEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataCalendarEntry from a JSON string
activity_create_request_data_calendar_entry_instance = ActivityCreateRequestDataCalendarEntry.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataCalendarEntry.to_json())

# convert the object into a dict
activity_create_request_data_calendar_entry_dict = activity_create_request_data_calendar_entry_instance.to_dict()
# create an instance of ActivityCreateRequestDataCalendarEntry from a dict
activity_create_request_data_calendar_entry_from_dict = ActivityCreateRequestDataCalendarEntry.from_dict(activity_create_request_data_calendar_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


