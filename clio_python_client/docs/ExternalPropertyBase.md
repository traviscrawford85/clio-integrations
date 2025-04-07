# ExternalPropertyBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ExternalProperty* | [optional] 
**etag** | **str** | ETag for the *ExternalProperty* | [optional] 
**name** | **str** | The name of the *ExternalProperty* | [optional] 
**value** | **str** | The value of the *ExternalProperty* | [optional] 
**created_at** | **datetime** | The time the *ExternalProperty* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ExternalProperty* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.external_property_base import ExternalPropertyBase

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalPropertyBase from a JSON string
external_property_base_instance = ExternalPropertyBase.from_json(json)
# print the JSON string representation of the object
print(ExternalPropertyBase.to_json())

# convert the object into a dict
external_property_base_dict = external_property_base_instance.to_dict()
# create an instance of ExternalPropertyBase from a dict
external_property_base_from_dict = ExternalPropertyBase.from_dict(external_property_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


