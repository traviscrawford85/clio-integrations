# CalendarVisibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CalendarVisibility* | [optional] 
**etag** | **str** | ETag for the *CalendarVisibility* | [optional] 
**color** | **str** | Calendar color | [optional] 
**light_color** | **str** | Accent color to complement the main calendar color. | [optional] 
**visible** | **bool** | Whether the *CalendarVisibility* will be shown by default in the Clio Web UI. | [optional] 
**name** | **str** | Calendar name | [optional] 
**created_at** | **datetime** | The time the *CalendarVisibility* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CalendarVisibility* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.calendar_visibility import CalendarVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarVisibility from a JSON string
calendar_visibility_instance = CalendarVisibility.from_json(json)
# print the JSON string representation of the object
print(CalendarVisibility.to_json())

# convert the object into a dict
calendar_visibility_dict = calendar_visibility_instance.to_dict()
# create an instance of CalendarVisibility from a dict
calendar_visibility_from_dict = CalendarVisibility.from_dict(calendar_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


