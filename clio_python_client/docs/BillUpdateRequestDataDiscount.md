# BillUpdateRequestDataDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | Discount amount for the Bill. This can either be a percentage or monetary value, this is determined by the &#x60;discount[type]&#x60;. | [optional] 
**type** | **str** | The type of discount you are applying to your Bill with the &#x60;discount[rate]&#x60;. | [optional] 
**note** | **str** | A note for your Bill&#39;s discount. | [optional] 

## Example

```python
from openapi_client.models.bill_update_request_data_discount import BillUpdateRequestDataDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of BillUpdateRequestDataDiscount from a JSON string
bill_update_request_data_discount_instance = BillUpdateRequestDataDiscount.from_json(json)
# print the JSON string representation of the object
print(BillUpdateRequestDataDiscount.to_json())

# convert the object into a dict
bill_update_request_data_discount_dict = bill_update_request_data_discount_instance.to_dict()
# create an instance of BillUpdateRequestDataDiscount from a dict
bill_update_request_data_discount_from_dict = BillUpdateRequestDataDiscount.from_dict(bill_update_request_data_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


