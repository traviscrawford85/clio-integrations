# BillableClientList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BillableClient]**](BillableClient.md) | BillableClient List Response | 

## Example

```python
from openapi_client.models.billable_client_list import BillableClientList

# TODO update the JSON string below
json = "{}"
# create an instance of BillableClientList from a JSON string
billable_client_list_instance = BillableClientList.from_json(json)
# print the JSON string representation of the object
print(BillableClientList.to_json())

# convert the object into a dict
billable_client_list_dict = billable_client_list_instance.to_dict()
# create an instance of BillableClientList from a dict
billable_client_list_from_dict = BillableClientList.from_dict(billable_client_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


