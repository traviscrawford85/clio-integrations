# OutstandingClientBalanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OutstandingClientBalance]**](OutstandingClientBalance.md) | OutstandingClientBalance List Response | 

## Example

```python
from openapi_client.models.outstanding_client_balance_list import OutstandingClientBalanceList

# TODO update the JSON string below
json = "{}"
# create an instance of OutstandingClientBalanceList from a JSON string
outstanding_client_balance_list_instance = OutstandingClientBalanceList.from_json(json)
# print the JSON string representation of the object
print(OutstandingClientBalanceList.to_json())

# convert the object into a dict
outstanding_client_balance_list_dict = outstanding_client_balance_list_instance.to_dict()
# create an instance of OutstandingClientBalanceList from a dict
outstanding_client_balance_list_from_dict = OutstandingClientBalanceList.from_dict(outstanding_client_balance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


