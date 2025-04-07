# BillList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Bill]**](Bill.md) | Bill List Response | 

## Example

```python
from openapi_client.models.bill_list import BillList

# TODO update the JSON string below
json = "{}"
# create an instance of BillList from a JSON string
bill_list_instance = BillList.from_json(json)
# print the JSON string representation of the object
print(BillList.to_json())

# convert the object into a dict
bill_list_dict = bill_list_instance.to_dict()
# create an instance of BillList from a dict
bill_list_from_dict = BillList.from_dict(bill_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


