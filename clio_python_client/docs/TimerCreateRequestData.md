# TimerCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**TimerCreateRequestDataActivity**](TimerCreateRequestDataActivity.md) |  | 

## Example

```python
from openapi_client.models.timer_create_request_data import TimerCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TimerCreateRequestData from a JSON string
timer_create_request_data_instance = TimerCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TimerCreateRequestData.to_json())

# convert the object into a dict
timer_create_request_data_dict = timer_create_request_data_instance.to_dict()
# create an instance of TimerCreateRequestData from a dict
timer_create_request_data_from_dict = TimerCreateRequestData.from_dict(timer_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


