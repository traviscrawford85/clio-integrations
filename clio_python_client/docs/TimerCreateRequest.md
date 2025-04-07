# TimerCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TimerCreateRequestData**](TimerCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.timer_create_request import TimerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TimerCreateRequest from a JSON string
timer_create_request_instance = TimerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TimerCreateRequest.to_json())

# convert the object into a dict
timer_create_request_dict = timer_create_request_instance.to_dict()
# create an instance of TimerCreateRequest from a dict
timer_create_request_from_dict = TimerCreateRequest.from_dict(timer_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


