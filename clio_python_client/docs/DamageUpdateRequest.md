# DamageUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DamageUpdateRequestData**](DamageUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.damage_update_request import DamageUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DamageUpdateRequest from a JSON string
damage_update_request_instance = DamageUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DamageUpdateRequest.to_json())

# convert the object into a dict
damage_update_request_dict = damage_update_request_instance.to_dict()
# create an instance of DamageUpdateRequest from a dict
damage_update_request_from_dict = DamageUpdateRequest.from_dict(damage_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


