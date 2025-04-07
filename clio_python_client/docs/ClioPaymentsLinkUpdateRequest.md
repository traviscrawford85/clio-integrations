# ClioPaymentsLinkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClioPaymentsLinkUpdateRequestData**](ClioPaymentsLinkUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.clio_payments_link_update_request import ClioPaymentsLinkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLinkUpdateRequest from a JSON string
clio_payments_link_update_request_instance = ClioPaymentsLinkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLinkUpdateRequest.to_json())

# convert the object into a dict
clio_payments_link_update_request_dict = clio_payments_link_update_request_instance.to_dict()
# create an instance of ClioPaymentsLinkUpdateRequest from a dict
clio_payments_link_update_request_from_dict = ClioPaymentsLinkUpdateRequest.from_dict(clio_payments_link_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


