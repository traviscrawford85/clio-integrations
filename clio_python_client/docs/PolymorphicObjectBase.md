# PolymorphicObjectBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *PolymorphicObject* | [optional] 
**type** | **str** | The type of the *PolymorphicObject* | [optional] 
**identifier** | **str** | A string to identify the *PolymorphicObject* | [optional] 
**secondary_identifier** | **str** | A secondary string to identify the *PolymorphicObject* | [optional] 
**tertiary_identifier** | **str** | A tertiary string to identify the *PolymorphicObject* | [optional] 

## Example

```python
from openapi_client.models.polymorphic_object_base import PolymorphicObjectBase

# TODO update the JSON string below
json = "{}"
# create an instance of PolymorphicObjectBase from a JSON string
polymorphic_object_base_instance = PolymorphicObjectBase.from_json(json)
# print the JSON string representation of the object
print(PolymorphicObjectBase.to_json())

# convert the object into a dict
polymorphic_object_base_dict = polymorphic_object_base_instance.to_dict()
# create an instance of PolymorphicObjectBase from a dict
polymorphic_object_base_from_dict = PolymorphicObjectBase.from_dict(polymorphic_object_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


