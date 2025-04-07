# CalendarVisibilityList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CalendarVisibility]**](CalendarVisibility.md) | CalendarVisibility List Response | 

## Example

```python
from openapi_client.models.calendar_visibility_list import CalendarVisibilityList

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarVisibilityList from a JSON string
calendar_visibility_list_instance = CalendarVisibilityList.from_json(json)
# print the JSON string representation of the object
print(CalendarVisibilityList.to_json())

# convert the object into a dict
calendar_visibility_list_dict = calendar_visibility_list_instance.to_dict()
# create an instance of CalendarVisibilityList from a dict
calendar_visibility_list_from_dict = CalendarVisibilityList.from_dict(calendar_visibility_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


