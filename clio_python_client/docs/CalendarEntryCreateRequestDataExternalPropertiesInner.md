# CalendarEntryCreateRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per CalendarEntry** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_create_request_data_external_properties_inner import CalendarEntryCreateRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryCreateRequestDataExternalPropertiesInner from a JSON string
calendar_entry_create_request_data_external_properties_inner_instance = CalendarEntryCreateRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryCreateRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
calendar_entry_create_request_data_external_properties_inner_dict = calendar_entry_create_request_data_external_properties_inner_instance.to_dict()
# create an instance of CalendarEntryCreateRequestDataExternalPropertiesInner from a dict
calendar_entry_create_request_data_external_properties_inner_from_dict = CalendarEntryCreateRequestDataExternalPropertiesInner.from_dict(calendar_entry_create_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


