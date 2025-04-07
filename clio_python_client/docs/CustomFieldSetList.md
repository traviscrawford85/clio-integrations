# CustomFieldSetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomFieldSet]**](CustomFieldSet.md) | CustomFieldSet List Response | 

## Example

```python
from openapi_client.models.custom_field_set_list import CustomFieldSetList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSetList from a JSON string
custom_field_set_list_instance = CustomFieldSetList.from_json(json)
# print the JSON string representation of the object
print(CustomFieldSetList.to_json())

# convert the object into a dict
custom_field_set_list_dict = custom_field_set_list_instance.to_dict()
# create an instance of CustomFieldSetList from a dict
custom_field_set_list_from_dict = CustomFieldSetList.from_dict(custom_field_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


