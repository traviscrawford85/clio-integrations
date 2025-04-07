# MyEventUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MyEventUpdateRequestData**](MyEventUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.my_event_update_request import MyEventUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MyEventUpdateRequest from a JSON string
my_event_update_request_instance = MyEventUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MyEventUpdateRequest.to_json())

# convert the object into a dict
my_event_update_request_dict = my_event_update_request_instance.to_dict()
# create an instance of MyEventUpdateRequest from a dict
my_event_update_request_from_dict = MyEventUpdateRequest.from_dict(my_event_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


