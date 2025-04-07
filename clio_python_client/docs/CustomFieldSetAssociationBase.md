# CustomFieldSetAssociationBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CustomFieldSetAssociation* | [optional] 
**etag** | **str** | ETag for the *CustomFieldSetAssociation* | [optional] 
**display_order** | **int** | The display position of the *CustomFieldSetAssociation* | [optional] 
**created_at** | **datetime** | The time the *CustomFieldSetAssociation* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CustomFieldSetAssociation* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.custom_field_set_association_base import CustomFieldSetAssociationBase

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSetAssociationBase from a JSON string
custom_field_set_association_base_instance = CustomFieldSetAssociationBase.from_json(json)
# print the JSON string representation of the object
print(CustomFieldSetAssociationBase.to_json())

# convert the object into a dict
custom_field_set_association_base_dict = custom_field_set_association_base_instance.to_dict()
# create an instance of CustomFieldSetAssociationBase from a dict
custom_field_set_association_base_from_dict = CustomFieldSetAssociationBase.from_dict(custom_field_set_association_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


