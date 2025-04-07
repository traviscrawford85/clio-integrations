# TrustLineItem


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
**bill** | [**BillBase**](BillBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**client** | [**ContactBase**](ContactBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.trust_line_item import TrustLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrustLineItem from a JSON string
trust_line_item_instance = TrustLineItem.from_json(json)
# print the JSON string representation of the object
print(TrustLineItem.to_json())

# convert the object into a dict
trust_line_item_dict = trust_line_item_instance.to_dict()
# create an instance of TrustLineItem from a dict
trust_line_item_from_dict = TrustLineItem.from_dict(trust_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


