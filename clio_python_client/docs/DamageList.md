# DamageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Damage]**](Damage.md) | Damage List Response | 

## Example

```python
from openapi_client.models.damage_list import DamageList

# TODO update the JSON string below
json = "{}"
# create an instance of DamageList from a JSON string
damage_list_instance = DamageList.from_json(json)
# print the JSON string representation of the object
print(DamageList.to_json())

# convert the object into a dict
damage_list_dict = damage_list_instance.to_dict()
# create an instance of DamageList from a dict
damage_list_from_dict = DamageList.from_dict(damage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


