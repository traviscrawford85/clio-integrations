# TimerCreateRequestDataActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Activity associated with the Timer. The keyword &#x60;null&#x60; is not valid for this field. | 

## Example

```python
from openapi_client.models.timer_create_request_data_activity import TimerCreateRequestDataActivity

# TODO update the JSON string below
json = "{}"
# create an instance of TimerCreateRequestDataActivity from a JSON string
timer_create_request_data_activity_instance = TimerCreateRequestDataActivity.from_json(json)
# print the JSON string representation of the object
print(TimerCreateRequestDataActivity.to_json())

# convert the object into a dict
timer_create_request_data_activity_dict = timer_create_request_data_activity_instance.to_dict()
# create an instance of TimerCreateRequestDataActivity from a dict
timer_create_request_data_activity_from_dict = TimerCreateRequestDataActivity.from_dict(timer_create_request_data_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


