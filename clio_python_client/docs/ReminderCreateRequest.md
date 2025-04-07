# ReminderCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReminderCreateRequestData**](ReminderCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.reminder_create_request import ReminderCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderCreateRequest from a JSON string
reminder_create_request_instance = ReminderCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ReminderCreateRequest.to_json())

# convert the object into a dict
reminder_create_request_dict = reminder_create_request_instance.to_dict()
# create an instance of ReminderCreateRequest from a dict
reminder_create_request_from_dict = ReminderCreateRequest.from_dict(reminder_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


