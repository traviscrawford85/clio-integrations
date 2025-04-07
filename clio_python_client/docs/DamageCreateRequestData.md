# DamageCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount | 
**damage_type** | **str** | Damage type | 
**description** | **str** | Description | 
**matter_id** | **int** | The unique identifier of the Matter to which the Damage is associated. | 

## Example

```python
from openapi_client.models.damage_create_request_data import DamageCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DamageCreateRequestData from a JSON string
damage_create_request_data_instance = DamageCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(DamageCreateRequestData.to_json())

# convert the object into a dict
damage_create_request_data_dict = damage_create_request_data_instance.to_dict()
# create an instance of DamageCreateRequestData from a dict
damage_create_request_data_from_dict = DamageCreateRequestData.from_dict(damage_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


