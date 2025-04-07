# CalendarVisibilityUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CalendarVisibilityUpdateRequestData**](CalendarVisibilityUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.calendar_visibility_update_request import CalendarVisibilityUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarVisibilityUpdateRequest from a JSON string
calendar_visibility_update_request_instance = CalendarVisibilityUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarVisibilityUpdateRequest.to_json())

# convert the object into a dict
calendar_visibility_update_request_dict = calendar_visibility_update_request_instance.to_dict()
# create an instance of CalendarVisibilityUpdateRequest from a dict
calendar_visibility_update_request_from_dict = CalendarVisibilityUpdateRequest.from_dict(calendar_visibility_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


