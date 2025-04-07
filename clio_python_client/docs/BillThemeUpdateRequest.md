# BillThemeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BillThemeUpdateRequestData**](BillThemeUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.bill_theme_update_request import BillThemeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillThemeUpdateRequest from a JSON string
bill_theme_update_request_instance = BillThemeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BillThemeUpdateRequest.to_json())

# convert the object into a dict
bill_theme_update_request_dict = bill_theme_update_request_instance.to_dict()
# create an instance of BillThemeUpdateRequest from a dict
bill_theme_update_request_from_dict = BillThemeUpdateRequest.from_dict(bill_theme_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


