# EventMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unread_mobile_events** | **int** | The number of unread mobile event notifications for the current user | [optional] 
**unread_web_events** | **int** | The number of unread web event notifications for the current user | [optional] 
**unread_secure_messages** | **int** | The number of unread secure messages for the current user | [optional] 
**unread_client_portal_messages** | **int** | The number of unread client portal messages for the current user | [optional] 
**unread_text_messages** | **int** | The number of unread text messages for the current user | [optional] 

## Example

```python
from openapi_client.models.event_metrics import EventMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of EventMetrics from a JSON string
event_metrics_instance = EventMetrics.from_json(json)
# print the JSON string representation of the object
print(EventMetrics.to_json())

# convert the object into a dict
event_metrics_dict = event_metrics_instance.to_dict()
# create an instance of EventMetrics from a dict
event_metrics_from_dict = EventMetrics.from_dict(event_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


