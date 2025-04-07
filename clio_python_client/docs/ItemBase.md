# ItemBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Item* | [optional] 
**etag** | **str** | ETag for the *Item* | [optional] 
**created_at** | **datetime** | The time the *Item* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Item* was last updated (as a ISO-8601 timestamp) | [optional] 
**deleted_at** | **datetime** | The time the *Item* was deleted (as a ISO-8601 timestamp) | [optional] 
**type** | **str** | The type of the *Item* | [optional] 
**locked** | **bool** | Whether or not the Item is locked. Locked Item cannot be modified | [optional] 
**name** | **str** | The name of the Item | [optional] 

## Example

```python
from openapi_client.models.item_base import ItemBase

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBase from a JSON string
item_base_instance = ItemBase.from_json(json)
# print the JSON string representation of the object
print(ItemBase.to_json())

# convert the object into a dict
item_base_dict = item_base_instance.to_dict()
# create an instance of ItemBase from a dict
item_base_from_dict = ItemBase.from_dict(item_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


