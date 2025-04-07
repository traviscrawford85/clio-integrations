# CustomFieldValueBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the *CustomFieldValue* | [optional] 
**etag** | **str** | ETag for the *CustomFieldValue* | [optional] 
**field_name** | **str** | The name of the custom field | [optional] 
**created_at** | **datetime** | The time the *CustomFieldValue* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CustomFieldValue* was last updated (as a ISO-8601 timestamp) | [optional] 
**field_type** | **str** | The type of the *CustomFieldValue* | [optional] 
**field_required** | **bool** | Whether the *CustomFieldValue* requires a value | [optional] 
**field_displayed** | **bool** | Whether the *CustomFieldValue* is displayed by default | [optional] 
**field_display_order** | **int** | The display position of the *CustomFieldValue* | [optional] 
**value** | **str** | The value of the *CustomFieldValue* | [optional] 
**soft_deleted** | **bool** | Whether the value is associated with a deleted custom field | [optional] 

## Example

```python
from openapi_client.models.custom_field_value_base import CustomFieldValueBase

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValueBase from a JSON string
custom_field_value_base_instance = CustomFieldValueBase.from_json(json)
# print the JSON string representation of the object
print(CustomFieldValueBase.to_json())

# convert the object into a dict
custom_field_value_base_dict = custom_field_value_base_instance.to_dict()
# create an instance of CustomFieldValueBase from a dict
custom_field_value_base_from_dict = CustomFieldValueBase.from_dict(custom_field_value_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


