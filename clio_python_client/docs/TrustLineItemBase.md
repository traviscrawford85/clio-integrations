# TrustLineItemBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TrustLineItem* | [optional] 
**etag** | **str** | ETag for the *TrustLineItem* | [optional] 
**var_date** | **date** | The date of the *TrustLineItem* (as a ISO-8601 date) | [optional] 
**total** | **float** | The total amount for the *TrustLineItem* | [optional] 
**note** | **str** | Note for the *TrustLineItem* | [optional] 
**created_at** | **datetime** | The time the *TrustLineItem* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TrustLineItem* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.trust_line_item_base import TrustLineItemBase

# TODO update the JSON string below
json = "{}"
# create an instance of TrustLineItemBase from a JSON string
trust_line_item_base_instance = TrustLineItemBase.from_json(json)
# print the JSON string representation of the object
print(TrustLineItemBase.to_json())

# convert the object into a dict
trust_line_item_base_dict = trust_line_item_base_instance.to_dict()
# create an instance of TrustLineItemBase from a dict
trust_line_item_base_from_dict = TrustLineItemBase.from_dict(trust_line_item_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


