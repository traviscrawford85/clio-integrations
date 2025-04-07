# CustomActionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CustomAction* | [optional] 
**etag** | **str** | ETag for the *CustomAction* | [optional] 
**created_at** | **datetime** | The time the *CustomAction* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CustomAction* was last updated (as a ISO-8601 timestamp) | [optional] 
**label** | **str** | Text label to be displayed on the custom link. | [optional] 
**target_url** | **str** | Target URL which will be opened in a new tab when the user clicks the custom link. | [optional] 
**ui_reference** | **str** | UI reference location within Clio where the link will be displayed. | [optional] 

## Example

```python
from openapi_client.models.custom_action_base import CustomActionBase

# TODO update the JSON string below
json = "{}"
# create an instance of CustomActionBase from a JSON string
custom_action_base_instance = CustomActionBase.from_json(json)
# print the JSON string representation of the object
print(CustomActionBase.to_json())

# convert the object into a dict
custom_action_base_dict = custom_action_base_instance.to_dict()
# create an instance of CustomActionBase from a dict
custom_action_base_from_dict = CustomActionBase.from_dict(custom_action_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


