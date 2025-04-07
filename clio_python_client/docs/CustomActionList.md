# CustomActionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomAction]**](CustomAction.md) | CustomAction List Response | 

## Example

```python
from openapi_client.models.custom_action_list import CustomActionList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomActionList from a JSON string
custom_action_list_instance = CustomActionList.from_json(json)
# print the JSON string representation of the object
print(CustomActionList.to_json())

# convert the object into a dict
custom_action_list_dict = custom_action_list_instance.to_dict()
# create an instance of CustomActionList from a dict
custom_action_list_from_dict = CustomActionList.from_dict(custom_action_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


