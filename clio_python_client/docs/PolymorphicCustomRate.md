# PolymorphicCustomRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the custom rate | [optional] 
**etag** | **str** | ETag for the *PolymorphicCustomRate* | [optional] 
**created_at** | **datetime** | The time the *PolymorphicCustomRate* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *PolymorphicCustomRate* was last updated (as a ISO-8601 timestamp) | [optional] 
**rate** | **float** | If &#x60;custom_rate.type&#x60; is &#x60;HourlyRate&#x60;, it is the dollar amount of the custom rate of the User or Group for the Matter.  If &#x60;custom_rate.type&#x60; is &#x60;FlatRate&#x60;, it is the dollar amount of the custom flat rate for the Matter.  If &#x60;custom_rate.type&#x60; is &#x60;ContingencyFee&#x60;, it is the percentage of the contingency fee awarded to the user for the Matter. The value may also be expressed as string that represents a rational number such as &#x60;1/3&#x60;.  If the user does not have sufficient rate visibility, the rates are hidden.  | [optional] 
**award** | **float** | The value of the ContingencyFee award. | [optional] 
**note** | **str** | Details about the ContingencyFee award. | [optional] 
**var_date** | **date** | The date of the ContingencyFee award. | [optional] 
**user** | [**PolymorphicCustomRateUserBase**](PolymorphicCustomRateUserBase.md) |  | [optional] 
**group** | [**PolymorphicCustomRateGroupBase**](PolymorphicCustomRateGroupBase.md) |  | [optional] 
**activity_description** | [**PolymorphicCustomRateActivityDescriptionBase**](PolymorphicCustomRateActivityDescriptionBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.polymorphic_custom_rate import PolymorphicCustomRate

# TODO update the JSON string below
json = "{}"
# create an instance of PolymorphicCustomRate from a JSON string
polymorphic_custom_rate_instance = PolymorphicCustomRate.from_json(json)
# print the JSON string representation of the object
print(PolymorphicCustomRate.to_json())

# convert the object into a dict
polymorphic_custom_rate_dict = polymorphic_custom_rate_instance.to_dict()
# create an instance of PolymorphicCustomRate from a dict
polymorphic_custom_rate_from_dict = PolymorphicCustomRate.from_dict(polymorphic_custom_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


