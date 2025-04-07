# CalendarList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Calendar]**](Calendar.md) | Calendar List Response | 

## Example

```python
from openapi_client.models.calendar_list import CalendarList

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarList from a JSON string
calendar_list_instance = CalendarList.from_json(json)
# print the JSON string representation of the object
print(CalendarList.to_json())

# convert the object into a dict
calendar_list_dict = calendar_list_instance.to_dict()
# create an instance of CalendarList from a dict
calendar_list_from_dict = CalendarList.from_dict(calendar_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


