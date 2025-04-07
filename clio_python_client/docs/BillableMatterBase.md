# BillableMatterBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The currency code | [optional] 
**currency_id** | **int** | The currency ID | [optional] 
**id** | **int** | Unique identifier for the *BillableMatter* | [optional] 
**unbilled_hours** | **float** | The unbilled number of hours for the matter | [optional] 
**unbilled_amount** | **float** | The unbilled amount for the matter | [optional] 
**amount_in_trust** | **float** | The trust amount available for the matter | [optional] 
**display_number** | **str** | The reference to the matter | [optional] 

## Example

```python
from openapi_client.models.billable_matter_base import BillableMatterBase

# TODO update the JSON string below
json = "{}"
# create an instance of BillableMatterBase from a JSON string
billable_matter_base_instance = BillableMatterBase.from_json(json)
# print the JSON string representation of the object
print(BillableMatterBase.to_json())

# convert the object into a dict
billable_matter_base_dict = billable_matter_base_instance.to_dict()
# create an instance of BillableMatterBase from a dict
billable_matter_base_from_dict = BillableMatterBase.from_dict(billable_matter_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


