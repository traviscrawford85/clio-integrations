# CustomFieldSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CustomFieldSet* | [optional] 
**etag** | **str** | ETag for the *CustomFieldSet* | [optional] 
**name** | **str** | The name of the custom field set. | [optional] 
**parent_type** | **str** | Type of object the *CustomFieldSet* is for. | [optional] 
**displayed** | **bool** | Whether or not the *CustomFieldSet* should be displayed by default. | [optional] 
**created_at** | **datetime** | The time the *CustomFieldSet* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CustomFieldSet* was last updated (as a ISO-8601 timestamp) | [optional] 
**custom_fields** | [**List[CustomFieldBase]**](CustomFieldBase.md) | CustomField | [optional] 

## Example

```python
from openapi_client.models.custom_field_set import CustomFieldSet

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSet from a JSON string
custom_field_set_instance = CustomFieldSet.from_json(json)
# print the JSON string representation of the object
print(CustomFieldSet.to_json())

# convert the object into a dict
custom_field_set_dict = custom_field_set_instance.to_dict()
# create an instance of CustomFieldSet from a dict
custom_field_set_from_dict = CustomFieldSet.from_dict(custom_field_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


