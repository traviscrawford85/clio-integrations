# CalendarUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CalendarUpdateRequestData**](CalendarUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.calendar_update_request import CalendarUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarUpdateRequest from a JSON string
calendar_update_request_instance = CalendarUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarUpdateRequest.to_json())

# convert the object into a dict
calendar_update_request_dict = calendar_update_request_instance.to_dict()
# create an instance of CalendarUpdateRequest from a dict
calendar_update_request_from_dict = CalendarUpdateRequest.from_dict(calendar_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


