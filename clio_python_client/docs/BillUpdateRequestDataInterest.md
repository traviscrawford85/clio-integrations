# BillUpdateRequestDataInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | Interest amount for the Bill as percentage. | [optional] 
**type** | **str** | The type of interest you are applying to your Bill with the &#x60;interest[rate]&#x60;. | [optional] 
**period** | **int** | The interest period for how frequently your Bill will charge interest. | [optional] 

## Example

```python
from openapi_client.models.bill_update_request_data_interest import BillUpdateRequestDataInterest

# TODO update the JSON string below
json = "{}"
# create an instance of BillUpdateRequestDataInterest from a JSON string
bill_update_request_data_interest_instance = BillUpdateRequestDataInterest.from_json(json)
# print the JSON string representation of the object
print(BillUpdateRequestDataInterest.to_json())

# convert the object into a dict
bill_update_request_data_interest_dict = bill_update_request_data_interest_instance.to_dict()
# create an instance of BillUpdateRequestDataInterest from a dict
bill_update_request_data_interest_from_dict = BillUpdateRequestDataInterest.from_dict(bill_update_request_data_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


