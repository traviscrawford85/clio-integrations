# CalendarEntryUpdateRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single ExternalProperty associated with the CalendarEntry. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per CalendarEntry** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated ExternalProperty is present, the ExternalProperty is deleted from the CalendarEntry. | [optional] 

## Example

```python
from openapi_client.models.calendar_entry_update_request_data_external_properties_inner import CalendarEntryUpdateRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryUpdateRequestDataExternalPropertiesInner from a JSON string
calendar_entry_update_request_data_external_properties_inner_instance = CalendarEntryUpdateRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryUpdateRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
calendar_entry_update_request_data_external_properties_inner_dict = calendar_entry_update_request_data_external_properties_inner_instance.to_dict()
# create an instance of CalendarEntryUpdateRequestDataExternalPropertiesInner from a dict
calendar_entry_update_request_data_external_properties_inner_from_dict = CalendarEntryUpdateRequestDataExternalPropertiesInner.from_dict(calendar_entry_update_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


