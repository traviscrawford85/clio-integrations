# PicklistOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *PicklistOption* | [optional] 
**etag** | **str** | ETag for the *PicklistOption* | [optional] 
**created_at** | **datetime** | The time the *PicklistOption* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *PicklistOption* was last updated (as a ISO-8601 timestamp) | [optional] 
**option** | **str** | The value of the *PicklistOption* | [optional] 
**deleted_at** | **datetime** | The time the *PicklistOption* was deleted (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.picklist_option import PicklistOption

# TODO update the JSON string below
json = "{}"
# create an instance of PicklistOption from a JSON string
picklist_option_instance = PicklistOption.from_json(json)
# print the JSON string representation of the object
print(PicklistOption.to_json())

# convert the object into a dict
picklist_option_dict = picklist_option_instance.to_dict()
# create an instance of PicklistOption from a dict
picklist_option_from_dict = PicklistOption.from_dict(picklist_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


