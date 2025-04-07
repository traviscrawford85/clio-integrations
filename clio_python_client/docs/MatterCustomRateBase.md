# MatterCustomRateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the *MatterCustomRate* | [optional] 
**on_invoice** | **bool** | Specifies if the matter&#39;s associated activity is posted or on a bill. | [optional] 

## Example

```python
from openapi_client.models.matter_custom_rate_base import MatterCustomRateBase

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCustomRateBase from a JSON string
matter_custom_rate_base_instance = MatterCustomRateBase.from_json(json)
# print the JSON string representation of the object
print(MatterCustomRateBase.to_json())

# convert the object into a dict
matter_custom_rate_base_dict = matter_custom_rate_base_instance.to_dict()
# create an instance of MatterCustomRateBase from a dict
matter_custom_rate_base_from_dict = MatterCustomRateBase.from_dict(matter_custom_rate_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


