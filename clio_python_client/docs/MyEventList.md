# MyEventList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MyEvent]**](MyEvent.md) | MyEvent List Response | 

## Example

```python
from openapi_client.models.my_event_list import MyEventList

# TODO update the JSON string below
json = "{}"
# create an instance of MyEventList from a JSON string
my_event_list_instance = MyEventList.from_json(json)
# print the JSON string representation of the object
print(MyEventList.to_json())

# convert the object into a dict
my_event_list_dict = my_event_list_instance.to_dict()
# create an instance of MyEventList from a dict
my_event_list_from_dict = MyEventList.from_dict(my_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


