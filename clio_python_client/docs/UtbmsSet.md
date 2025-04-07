# UtbmsSet


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
from openapi_client.models.utbms_set import UtbmsSet

# TODO update the JSON string below
json = "{}"
# create an instance of UtbmsSet from a JSON string
utbms_set_instance = UtbmsSet.from_json(json)
# print the JSON string representation of the object
print(UtbmsSet.to_json())

# convert the object into a dict
utbms_set_dict = utbms_set_instance.to_dict()
# create an instance of UtbmsSet from a dict
utbms_set_from_dict = UtbmsSet.from_dict(utbms_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


