# DamageBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Damage* | [optional] 
**amount** | **float** | Amount for Damage | [optional] 
**damage_type** | **str** | Damage type of the record | [optional] 
**description** | **str** | Description for Damage | [optional] 
**etag** | **str** | ETag for the *Damage* | [optional] 
**created_at** | **datetime** | The time the *Damage* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Damage* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.damage_base import DamageBase

# TODO update the JSON string below
json = "{}"
# create an instance of DamageBase from a JSON string
damage_base_instance = DamageBase.from_json(json)
# print the JSON string representation of the object
print(DamageBase.to_json())

# convert the object into a dict
damage_base_dict = damage_base_instance.to_dict()
# create an instance of DamageBase from a dict
damage_base_from_dict = DamageBase.from_dict(damage_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


