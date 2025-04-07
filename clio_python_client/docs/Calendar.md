# Calendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Calendar* | [optional] 
**etag** | **str** | ETag for the *Calendar* | [optional] 
**color** | **str** | Color | [optional] 
**light_color** | **str** | Accent color to complement the main calendar color. | [optional] 
**court_rules_default_calendar** | **bool** | Whether the calendar is default court rules calendar for current user | [optional] 
**name** | **str** | The name of the *Calendar* | [optional] 
**permission** | **str** | The user&#39;s permission to the *Calendar* | [optional] 
**type** | **str** | The type of the *Calendar* | [optional] 
**visible** | **bool** | Whether the *Calendar* will be shown by default in the Clio Web UI (assuming no source is provided). | [optional] 
**created_at** | **datetime** | The time the *Calendar* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Calendar* was last updated (as a ISO-8601 timestamp) | [optional] 
**source** | **str** | The source that visible applies to, by default the Clio Web UI (Expects &#39;mobile&#39; or &#39;web&#39;). | [optional] 
**creator** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.calendar import Calendar

# TODO update the JSON string below
json = "{}"
# create an instance of Calendar from a JSON string
calendar_instance = Calendar.from_json(json)
# print the JSON string representation of the object
print(Calendar.to_json())

# convert the object into a dict
calendar_dict = calendar_instance.to_dict()
# create an instance of Calendar from a dict
calendar_from_dict = Calendar.from_dict(calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


