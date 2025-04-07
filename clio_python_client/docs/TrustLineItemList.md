# TrustLineItemList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TrustLineItem]**](TrustLineItem.md) | TrustLineItem List Response | 

## Example

```python
from openapi_client.models.trust_line_item_list import TrustLineItemList

# TODO update the JSON string below
json = "{}"
# create an instance of TrustLineItemList from a JSON string
trust_line_item_list_instance = TrustLineItemList.from_json(json)
# print the JSON string representation of the object
print(TrustLineItemList.to_json())

# convert the object into a dict
trust_line_item_list_dict = trust_line_item_list_instance.to_dict()
# create an instance of TrustLineItemList from a dict
trust_line_item_list_from_dict = TrustLineItemList.from_dict(trust_line_item_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


