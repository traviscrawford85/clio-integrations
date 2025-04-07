# TrustLineItemUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrustLineItemUpdateRequestData**](TrustLineItemUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.trust_line_item_update_request import TrustLineItemUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrustLineItemUpdateRequest from a JSON string
trust_line_item_update_request_instance = TrustLineItemUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TrustLineItemUpdateRequest.to_json())

# convert the object into a dict
trust_line_item_update_request_dict = trust_line_item_update_request_instance.to_dict()
# create an instance of TrustLineItemUpdateRequest from a dict
trust_line_item_update_request_from_dict = TrustLineItemUpdateRequest.from_dict(trust_line_item_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


