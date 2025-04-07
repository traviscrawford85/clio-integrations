# UtbmsCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *UtbmsCode* | [optional] 
**etag** | **str** | ETag for the *UtbmsCode* | [optional] 
**name** | **str** | The name of the *UtbmsCode* | [optional] 
**code** | **str** | The UTBMS code for the *UtbmsCode* | [optional] 
**description** | **str** | The UTBMS description for the *UtbmsCode* | [optional] 
**type** | **str** | The type of the *UtbmsCode* | [optional] 
**utbms_set_id** | **int** | Set id for the *UtbmsCode* | [optional] 
**created_at** | **datetime** | The time the *UtbmsCode* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *UtbmsCode* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.utbms_code import UtbmsCode

# TODO update the JSON string below
json = "{}"
# create an instance of UtbmsCode from a JSON string
utbms_code_instance = UtbmsCode.from_json(json)
# print the JSON string representation of the object
print(UtbmsCode.to_json())

# convert the object into a dict
utbms_code_dict = utbms_code_instance.to_dict()
# create an instance of UtbmsCode from a dict
utbms_code_from_dict = UtbmsCode.from_dict(utbms_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


