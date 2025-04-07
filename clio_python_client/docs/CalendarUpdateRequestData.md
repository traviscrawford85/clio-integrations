# CalendarUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Calendar color as seen in the Clio Web UI. | [optional] 
**name** | **str** | Calendar name. | [optional] 
**source** | **str** | The source that visible applies to, by default the Clio Web UI (Expects &#39;mobile&#39; or &#39;web&#39;). | [optional] 
**visible** | **bool** | Whether or not the Calendar should be visible by default in the Clio Web UI (assuming no source is provided). | [optional] 

## Example

```python
from openapi_client.models.calendar_update_request_data import CalendarUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarUpdateRequestData from a JSON string
calendar_update_request_data_instance = CalendarUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CalendarUpdateRequestData.to_json())

# convert the object into a dict
calendar_update_request_data_dict = calendar_update_request_data_instance.to_dict()
# create an instance of CalendarUpdateRequestData from a dict
calendar_update_request_data_from_dict = CalendarUpdateRequestData.from_dict(calendar_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


