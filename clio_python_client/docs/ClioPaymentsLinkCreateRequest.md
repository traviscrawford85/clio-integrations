# ClioPaymentsLinkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClioPaymentsLinkCreateRequestData**](ClioPaymentsLinkCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.clio_payments_link_create_request import ClioPaymentsLinkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLinkCreateRequest from a JSON string
clio_payments_link_create_request_instance = ClioPaymentsLinkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLinkCreateRequest.to_json())

# convert the object into a dict
clio_payments_link_create_request_dict = clio_payments_link_create_request_instance.to_dict()
# create an instance of ClioPaymentsLinkCreateRequest from a dict
clio_payments_link_create_request_from_dict = ClioPaymentsLinkCreateRequest.from_dict(clio_payments_link_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


