# UtbmsSetBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *UtbmsSet* | [optional] 
**etag** | **str** | ETag for the *UtbmsSet* | [optional] 
**name** | **str** | The name of the *UtbmsSet* | [optional] 
**enabled** | **bool** | Whether the *UtbmsSet* is enabled for the current account. | [optional] 
**created_at** | **datetime** | The time the *UtbmsSet* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *UtbmsSet* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.utbms_set_base import UtbmsSetBase

# TODO update the JSON string below
json = "{}"
# create an instance of UtbmsSetBase from a JSON string
utbms_set_base_instance = UtbmsSetBase.from_json(json)
# print the JSON string representation of the object
print(UtbmsSetBase.to_json())

# convert the object into a dict
utbms_set_base_dict = utbms_set_base_instance.to_dict()
# create an instance of UtbmsSetBase from a dict
utbms_set_base_from_dict = UtbmsSetBase.from_dict(utbms_set_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


