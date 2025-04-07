# PolymorphicCustomRateGroupBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | ETag for the *Group* | [optional] 
**id** | **int** | Unique identifier for the *Group* | [optional] 
**name** | **str** | The name of the *Group* | [optional] 

## Example

```python
from openapi_client.models.polymorphic_custom_rate_group_base import PolymorphicCustomRateGroupBase

# TODO update the JSON string below
json = "{}"
# create an instance of PolymorphicCustomRateGroupBase from a JSON string
polymorphic_custom_rate_group_base_instance = PolymorphicCustomRateGroupBase.from_json(json)
# print the JSON string representation of the object
print(PolymorphicCustomRateGroupBase.to_json())

# convert the object into a dict
polymorphic_custom_rate_group_base_dict = polymorphic_custom_rate_group_base_instance.to_dict()
# create an instance of PolymorphicCustomRateGroupBase from a dict
polymorphic_custom_rate_group_base_from_dict = PolymorphicCustomRateGroupBase.from_dict(polymorphic_custom_rate_group_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


