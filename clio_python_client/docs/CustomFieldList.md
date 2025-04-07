# CustomFieldList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomField]**](CustomField.md) | CustomField List Response | 

## Example

```python
from openapi_client.models.custom_field_list import CustomFieldList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldList from a JSON string
custom_field_list_instance = CustomFieldList.from_json(json)
# print the JSON string representation of the object
print(CustomFieldList.to_json())

# convert the object into a dict
custom_field_list_dict = custom_field_list_instance.to_dict()
# create an instance of CustomFieldList from a dict
custom_field_list_from_dict = CustomFieldList.from_dict(custom_field_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


