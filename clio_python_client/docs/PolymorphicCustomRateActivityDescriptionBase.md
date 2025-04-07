# PolymorphicCustomRateActivityDescriptionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ActivityDescription* | [optional] 
**etag** | **str** | ETag for the *ActivityDescription* | [optional] 
**name** | **str** | The name of the *ActivityDescription* | [optional] 

## Example

```python
from openapi_client.models.polymorphic_custom_rate_activity_description_base import PolymorphicCustomRateActivityDescriptionBase

# TODO update the JSON string below
json = "{}"
# create an instance of PolymorphicCustomRateActivityDescriptionBase from a JSON string
polymorphic_custom_rate_activity_description_base_instance = PolymorphicCustomRateActivityDescriptionBase.from_json(json)
# print the JSON string representation of the object
print(PolymorphicCustomRateActivityDescriptionBase.to_json())

# convert the object into a dict
polymorphic_custom_rate_activity_description_base_dict = polymorphic_custom_rate_activity_description_base_instance.to_dict()
# create an instance of PolymorphicCustomRateActivityDescriptionBase from a dict
polymorphic_custom_rate_activity_description_base_from_dict = PolymorphicCustomRateActivityDescriptionBase.from_dict(polymorphic_custom_rate_activity_description_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


