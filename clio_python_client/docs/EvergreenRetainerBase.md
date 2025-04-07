# EvergreenRetainerBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *EvergreenRetainer* | [optional] 
**created_at** | **datetime** | The time the *EvergreenRetainer* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *EvergreenRetainer* was last updated (as a ISO-8601 timestamp) | [optional] 
**etag** | **str** | ETag for the *EvergreenRetainer* | [optional] 
**minimum_threshold** | **float** | The trust balance threshold for the associated Matter. When the balance falls below the threshold, the retainer&#39;s associated recipients (firm users) will receive a notification. | [optional] 

## Example

```python
from openapi_client.models.evergreen_retainer_base import EvergreenRetainerBase

# TODO update the JSON string below
json = "{}"
# create an instance of EvergreenRetainerBase from a JSON string
evergreen_retainer_base_instance = EvergreenRetainerBase.from_json(json)
# print the JSON string representation of the object
print(EvergreenRetainerBase.to_json())

# convert the object into a dict
evergreen_retainer_base_dict = evergreen_retainer_base_instance.to_dict()
# create an instance of EvergreenRetainerBase from a dict
evergreen_retainer_base_from_dict = EvergreenRetainerBase.from_dict(evergreen_retainer_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


