# ClioPaymentsLinkUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired** | **bool** | Setting this will update the payment link to be immediately expired. | [optional] 

## Example

```python
from openapi_client.models.clio_payments_link_update_request_data import ClioPaymentsLinkUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLinkUpdateRequestData from a JSON string
clio_payments_link_update_request_data_instance = ClioPaymentsLinkUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLinkUpdateRequestData.to_json())

# convert the object into a dict
clio_payments_link_update_request_data_dict = clio_payments_link_update_request_data_instance.to_dict()
# create an instance of ClioPaymentsLinkUpdateRequestData from a dict
clio_payments_link_update_request_data_from_dict = ClioPaymentsLinkUpdateRequestData.from_dict(clio_payments_link_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


