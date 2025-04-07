# Timer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Timer* | [optional] 
**etag** | **str** | ETag for the *Timer* | [optional] 
**start_time** | **datetime** | The time the *Timer* was started (as ISO-8601 timestamp) | [optional] 
**elapsed_time** | **float** | How much time has elapsed, in hours, since the timer was started | [optional] 
**created_at** | **datetime** | The time the *Timer* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Timer* was last updated (as a ISO-8601 timestamp) | [optional] 
**activity** | [**ActivityBase**](ActivityBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.timer import Timer

# TODO update the JSON string below
json = "{}"
# create an instance of Timer from a JSON string
timer_instance = Timer.from_json(json)
# print the JSON string representation of the object
print(Timer.to_json())

# convert the object into a dict
timer_dict = timer_instance.to_dict()
# create an instance of Timer from a dict
timer_from_dict = Timer.from_dict(timer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


