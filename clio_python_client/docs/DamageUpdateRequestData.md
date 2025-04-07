# DamageUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount | [optional] 
**damage_type** | **str** | Damage type | [optional] 
**description** | **str** | Description | [optional] 

## Example

```python
from openapi_client.models.damage_update_request_data import DamageUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DamageUpdateRequestData from a JSON string
damage_update_request_data_instance = DamageUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(DamageUpdateRequestData.to_json())

# convert the object into a dict
damage_update_request_data_dict = damage_update_request_data_instance.to_dict()
# create an instance of DamageUpdateRequestData from a dict
damage_update_request_data_from_dict = DamageUpdateRequestData.from_dict(damage_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


