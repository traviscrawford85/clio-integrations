# EventMetricsBase


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
from openapi_client.models.event_metrics_base import EventMetricsBase

# TODO update the JSON string below
json = "{}"
# create an instance of EventMetricsBase from a JSON string
event_metrics_base_instance = EventMetricsBase.from_json(json)
# print the JSON string representation of the object
print(EventMetricsBase.to_json())

# convert the object into a dict
event_metrics_base_dict = event_metrics_base_instance.to_dict()
# create an instance of EventMetricsBase from a dict
event_metrics_base_from_dict = EventMetricsBase.from_dict(event_metrics_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


