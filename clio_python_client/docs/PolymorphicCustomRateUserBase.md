# PolymorphicCustomRateUserBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the *User* is allowed to log in | [optional] 
**etag** | **str** | ETag for the *User* | [optional] 
**id** | **int** | Unique identifier for the *User* | [optional] 
**name** | **str** | The full name of the *User* | [optional] 

## Example

```python
from openapi_client.models.polymorphic_custom_rate_user_base import PolymorphicCustomRateUserBase

# TODO update the JSON string below
json = "{}"
# create an instance of PolymorphicCustomRateUserBase from a JSON string
polymorphic_custom_rate_user_base_instance = PolymorphicCustomRateUserBase.from_json(json)
# print the JSON string representation of the object
print(PolymorphicCustomRateUserBase.to_json())

# convert the object into a dict
polymorphic_custom_rate_user_base_dict = polymorphic_custom_rate_user_base_instance.to_dict()
# create an instance of PolymorphicCustomRateUserBase from a dict
polymorphic_custom_rate_user_base_from_dict = PolymorphicCustomRateUserBase.from_dict(polymorphic_custom_rate_user_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


