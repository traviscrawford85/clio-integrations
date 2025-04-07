# MyEventUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marked_as_read** | **bool** | Indicates whether the event notification should be marked as read by the current user. If &#x60;false&#x60; the event status is reset to unread. | [optional] 

## Example

```python
from openapi_client.models.my_event_update_request_data import MyEventUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MyEventUpdateRequestData from a JSON string
my_event_update_request_data_instance = MyEventUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(MyEventUpdateRequestData.to_json())

# convert the object into a dict
my_event_update_request_data_dict = my_event_update_request_data_instance.to_dict()
# create an instance of MyEventUpdateRequestData from a dict
my_event_update_request_data_from_dict = MyEventUpdateRequestData.from_dict(my_event_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


