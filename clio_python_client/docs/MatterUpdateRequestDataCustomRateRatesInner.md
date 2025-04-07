# MatterUpdateRequestDataCustomRateRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**MatterUpdateRequestDataCustomRateRatesInnerUser**](MatterUpdateRequestDataCustomRateRatesInnerUser.md) |  | [optional] 
**award** | **float** | The full amount of the award given. Only valid for ContingencyFee. If given as an empty string, it will reset the ContingencyFee into the unawarded state. | [optional] 
**note** | **str** | Detailed description of the rate. Only valid for ContingencyFee. | [optional] 
**var_date** | **date** | The date the rate is for. Only valid for ContingencyFee. (Expects an ISO-8601 date). | [optional] 
**rate** | **float** | If &#x60;type&#x60; is &#x60;HourlyRate&#x60;, it is the dollar amount of the custom rate of the User or Group for the Matter.  If &#x60;type&#x60; is &#x60;FlatRate&#x60;, it is the dollar amount of the custom flat rate for the Matter.  If &#x60;type&#x60; is &#x60;ContingencyFee&#x60;, it is the percentage of the contingency fee awarded to the user for the Matter.  | [optional] 
**id** | **int** | The unique identifier for a single Rate associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated Rate is present, the Rate is deleted from the Matter. | [optional] 
**activity_description** | [**MatterCreateRequestDataCustomRateRatesInnerActivityDescription**](MatterCreateRequestDataCustomRateRatesInnerActivityDescription.md) |  | [optional] 
**group** | [**MatterCreateRequestDataCustomRateRatesInnerGroup**](MatterCreateRequestDataCustomRateRatesInnerGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_custom_rate_rates_inner import MatterUpdateRequestDataCustomRateRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataCustomRateRatesInner from a JSON string
matter_update_request_data_custom_rate_rates_inner_instance = MatterUpdateRequestDataCustomRateRatesInner.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataCustomRateRatesInner.to_json())

# convert the object into a dict
matter_update_request_data_custom_rate_rates_inner_dict = matter_update_request_data_custom_rate_rates_inner_instance.to_dict()
# create an instance of MatterUpdateRequestDataCustomRateRatesInner from a dict
matter_update_request_data_custom_rate_rates_inner_from_dict = MatterUpdateRequestDataCustomRateRatesInner.from_dict(matter_update_request_data_custom_rate_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


