# BillUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BillUpdateRequestData**](BillUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.bill_update_request import BillUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillUpdateRequest from a JSON string
bill_update_request_instance = BillUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BillUpdateRequest.to_json())

# convert the object into a dict
bill_update_request_dict = bill_update_request_instance.to_dict()
# create an instance of BillUpdateRequest from a dict
bill_update_request_from_dict = BillUpdateRequest.from_dict(bill_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


