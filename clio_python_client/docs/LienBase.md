# LienBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Lien* | [optional] 
**amount** | **float** | The amount for Lien | [optional] 
**description** | **str** | Lien description | [optional] 
**etag** | **str** | ETag for the *Lien* | [optional] 
**lien_type** | **str** | Lien type | [optional] 
**mark_as_lien** | **bool** | Mark item as Lien | [optional] 
**created_at** | **datetime** | The time the *Lien* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Lien* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.lien_base import LienBase

# TODO update the JSON string below
json = "{}"
# create an instance of LienBase from a JSON string
lien_base_instance = LienBase.from_json(json)
# print the JSON string representation of the object
print(LienBase.to_json())

# convert the object into a dict
lien_base_dict = lien_base_instance.to_dict()
# create an instance of LienBase from a dict
lien_base_from_dict = LienBase.from_dict(lien_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


