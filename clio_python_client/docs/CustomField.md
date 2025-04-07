# CustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CustomField* | [optional] 
**etag** | **str** | ETag for the *CustomField* | [optional] 
**created_at** | **datetime** | The time the *CustomField* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CustomField* was last updated (as a ISO-8601 timestamp) | [optional] 
**name** | **str** | The name of the *CustomField* | [optional] 
**parent_type** | **str** | Type of object the *CustomField* is for | [optional] 
**field_type** | **str** | Field type of the *CustomField* | [optional] 
**displayed** | **bool** | Whether the *CustomField* is displayed by default | [optional] 
**deleted** | **bool** | Whether the *CustomField* is deleted for future use | [optional] 
**required** | **bool** | Whether the *CustomField* requires a value | [optional] 
**display_order** | **int** | The display position of the *CustomField* | [optional] 
**picklist_options** | [**List[PicklistOptionBase]**](PicklistOptionBase.md) | PicklistOption | [optional] 

## Example

```python
from openapi_client.models.custom_field import CustomField

# TODO update the JSON string below
json = "{}"
# create an instance of CustomField from a JSON string
custom_field_instance = CustomField.from_json(json)
# print the JSON string representation of the object
print(CustomField.to_json())

# convert the object into a dict
custom_field_dict = custom_field_instance.to_dict()
# create an instance of CustomField from a dict
custom_field_from_dict = CustomField.from_dict(custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


