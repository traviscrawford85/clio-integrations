# TrustLineItemUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date for the TrustLineItem. (Expects an ISO-8601 date). | [optional] 
**note** | **str** | Note for the TrustLineItem. | [optional] 
**total** | **float** | Total amount the TrustLineItem is for. | [optional] 

## Example

```python
from openapi_client.models.trust_line_item_update_request_data import TrustLineItemUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TrustLineItemUpdateRequestData from a JSON string
trust_line_item_update_request_data_instance = TrustLineItemUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(TrustLineItemUpdateRequestData.to_json())

# convert the object into a dict
trust_line_item_update_request_data_dict = trust_line_item_update_request_data_instance.to_dict()
# create an instance of TrustLineItemUpdateRequestData from a dict
trust_line_item_update_request_data_from_dict = TrustLineItemUpdateRequestData.from_dict(trust_line_item_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


