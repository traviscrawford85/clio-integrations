# DamageCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DamageCreateRequestData**](DamageCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.damage_create_request import DamageCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DamageCreateRequest from a JSON string
damage_create_request_instance = DamageCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DamageCreateRequest.to_json())

# convert the object into a dict
damage_create_request_dict = damage_create_request_instance.to_dict()
# create an instance of DamageCreateRequest from a dict
damage_create_request_from_dict = DamageCreateRequest.from_dict(damage_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


