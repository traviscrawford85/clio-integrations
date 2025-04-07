# CalendarVisibilityUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Calendar color as seen in the Clio Web UI. | [optional] 
**visible** | **str** | Whether or not the CalendarVisibility should be visible by default in the Clio Web UI. | [optional] 

## Example

```python
from openapi_client.models.calendar_visibility_update_request_data import CalendarVisibilityUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarVisibilityUpdateRequestData from a JSON string
calendar_visibility_update_request_data_instance = CalendarVisibilityUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CalendarVisibilityUpdateRequestData.to_json())

# convert the object into a dict
calendar_visibility_update_request_data_dict = calendar_visibility_update_request_data_instance.to_dict()
# create an instance of CalendarVisibilityUpdateRequestData from a dict
calendar_visibility_update_request_data_from_dict = CalendarVisibilityUpdateRequestData.from_dict(calendar_visibility_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


