# TimerBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Timer* | [optional] 
**etag** | **str** | ETag for the *Timer* | [optional] 
**start_time** | **datetime** | The time the *Timer* was started (as ISO-8601 timestamp) | [optional] 
**elapsed_time** | **float** | How much time has elapsed, in hours, since the timer was started | [optional] 
**created_at** | **datetime** | The time the *Timer* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Timer* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.timer_base import TimerBase

# TODO update the JSON string below
json = "{}"
# create an instance of TimerBase from a JSON string
timer_base_instance = TimerBase.from_json(json)
# print the JSON string representation of the object
print(TimerBase.to_json())

# convert the object into a dict
timer_base_dict = timer_base_instance.to_dict()
# create an instance of TimerBase from a dict
timer_base_from_dict = TimerBase.from_dict(timer_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


