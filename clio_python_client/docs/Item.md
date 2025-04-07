# Item


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
**parent** | [**LinkedFolderBase**](LinkedFolderBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**document_category** | [**DocumentCategoryBase**](DocumentCategoryBase.md) |  | [optional] 
**creator** | [**ClioCreatorBase**](ClioCreatorBase.md) |  | [optional] 
**latest_document_version** | [**DocumentVersionBase**](DocumentVersionBase.md) |  | [optional] 
**group** | [**GroupBase**](GroupBase.md) |  | [optional] 
**external_properties** | [**List[ExternalPropertyBase]**](ExternalPropertyBase.md) | ExternalProperty | [optional] 

## Example

```python
from openapi_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


