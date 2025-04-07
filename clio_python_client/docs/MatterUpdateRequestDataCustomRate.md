# MatterUpdateRequestDataCustomRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of custom rate for the Matter. | [optional] 
**rates** | [**List[MatterUpdateRequestDataCustomRateRatesInner]**](MatterUpdateRequestDataCustomRateRatesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_custom_rate import MatterUpdateRequestDataCustomRate

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataCustomRate from a JSON string
matter_update_request_data_custom_rate_instance = MatterUpdateRequestDataCustomRate.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataCustomRate.to_json())

# convert the object into a dict
matter_update_request_data_custom_rate_dict = matter_update_request_data_custom_rate_instance.to_dict()
# create an instance of MatterUpdateRequestDataCustomRate from a dict
matter_update_request_data_custom_rate_from_dict = MatterUpdateRequestDataCustomRate.from_dict(matter_update_request_data_custom_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


