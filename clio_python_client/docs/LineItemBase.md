# LineItemBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *LineItem* | [optional] 
**etag** | **str** | ETag for the *LineItem* | [optional] 
**type** | **str** | The type of the *LineItem* | [optional] 
**description** | **str** | The description for the *LineItem* | [optional] 
**var_date** | **date** | The *LineItem* date (as a ISO-8601 date) | [optional] 
**price** | **float** | The price of the *LineItem* | [optional] 
**taxable** | **bool** | Whether the *LineItem* is taxable | [optional] 
**kind** | **str** | The kind of *LineItem* | [optional] 
**note** | **str** | The note attached to the *LineItem* | [optional] 
**secondary_taxable** | **bool** | Whether the *LineItem* is secondary taxable | [optional] 
**total** | **float** | The total amount for the *LineItem* | [optional] 
**tax** | **float** | The tax amount for the *LineItem* | [optional] 
**secondary_tax** | **float** | The secondary tax amount for the *LineItem* | [optional] 
**sub_total** | **float** | The subtotal amount for the *LineItem* | [optional] 
**quantity** | **float** | The amount of hours for the *LineItem* | [optional] 
**group_ordering** | **int** | The value to specify the ordering of the *LineItem* on a bill | [optional] 
**created_at** | **datetime** | The time the *LineItem* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *LineItem* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.line_item_base import LineItemBase

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemBase from a JSON string
line_item_base_instance = LineItemBase.from_json(json)
# print the JSON string representation of the object
print(LineItemBase.to_json())

# convert the object into a dict
line_item_base_dict = line_item_base_instance.to_dict()
# create an instance of LineItemBase from a dict
line_item_base_from_dict = LineItemBase.from_dict(line_item_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


