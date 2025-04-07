# MatterBalanceBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *MatterBalance* | [optional] 
**amount** | **float** | The amount of balance of a matter. | [optional] 

## Example

```python
from openapi_client.models.matter_balance_base import MatterBalanceBase

# TODO update the JSON string below
json = "{}"
# create an instance of MatterBalanceBase from a JSON string
matter_balance_base_instance = MatterBalanceBase.from_json(json)
# print the JSON string representation of the object
print(MatterBalanceBase.to_json())

# convert the object into a dict
matter_balance_base_dict = matter_balance_base_instance.to_dict()
# create an instance of MatterBalanceBase from a dict
matter_balance_base_from_dict = MatterBalanceBase.from_dict(matter_balance_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


