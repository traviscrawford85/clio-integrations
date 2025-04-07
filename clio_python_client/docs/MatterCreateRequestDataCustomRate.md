# MatterCreateRequestDataCustomRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of custom rate for the Matter. | 
**rates** | [**List[MatterCreateRequestDataCustomRateRatesInner]**](MatterCreateRequestDataCustomRateRatesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_custom_rate import MatterCreateRequestDataCustomRate

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataCustomRate from a JSON string
matter_create_request_data_custom_rate_instance = MatterCreateRequestDataCustomRate.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataCustomRate.to_json())

# convert the object into a dict
matter_create_request_data_custom_rate_dict = matter_create_request_data_custom_rate_instance.to_dict()
# create an instance of MatterCreateRequestDataCustomRate from a dict
matter_create_request_data_custom_rate_from_dict = MatterCreateRequestDataCustomRate.from_dict(matter_create_request_data_custom_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


