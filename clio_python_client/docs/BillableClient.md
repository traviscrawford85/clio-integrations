# BillableClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *BillableClient* | [optional] 
**unbilled_hours** | **float** | The unbilled hours of  the client | [optional] 
**unbilled_amount** | **float** | The unbilled amount of the client | [optional] 
**amount_in_trust** | **float** | The trust amount available for the client | [optional] 
**name** | **str** | The name of the Client | [optional] 
**billable_matters_count** | **int** | The total number of billable matters the client has | [optional] 
**billable_matters** | [**List[BillableMatterBase]**](BillableMatterBase.md) | BillableMatter | [optional] 

## Example

```python
from openapi_client.models.billable_client import BillableClient

# TODO update the JSON string below
json = "{}"
# create an instance of BillableClient from a JSON string
billable_client_instance = BillableClient.from_json(json)
# print the JSON string representation of the object
print(BillableClient.to_json())

# convert the object into a dict
billable_client_dict = billable_client_instance.to_dict()
# create an instance of BillableClient from a dict
billable_client_from_dict = BillableClient.from_dict(billable_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


