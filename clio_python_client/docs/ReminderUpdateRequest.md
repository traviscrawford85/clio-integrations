# ReminderUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReminderUpdateRequestData**](ReminderUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.reminder_update_request import ReminderUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderUpdateRequest from a JSON string
reminder_update_request_instance = ReminderUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReminderUpdateRequest.to_json())

# convert the object into a dict
reminder_update_request_dict = reminder_update_request_instance.to_dict()
# create an instance of ReminderUpdateRequest from a dict
reminder_update_request_from_dict = ReminderUpdateRequest.from_dict(reminder_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


