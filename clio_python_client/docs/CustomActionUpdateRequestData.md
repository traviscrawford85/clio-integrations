# CustomActionUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Text label to be displayed on the custom link. | [optional] 
**target_url** | **str** | Target URL which will be opened in a new tab when the user clicks the custom link. | [optional] 
**ui_reference** | **str** | UI reference location within Clio where the link will be displayed. | [optional] 

## Example

```python
from openapi_client.models.custom_action_update_request_data import CustomActionUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomActionUpdateRequestData from a JSON string
custom_action_update_request_data_instance = CustomActionUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CustomActionUpdateRequestData.to_json())

# convert the object into a dict
custom_action_update_request_data_dict = custom_action_update_request_data_instance.to_dict()
# create an instance of CustomActionUpdateRequestData from a dict
custom_action_update_request_data_from_dict = CustomActionUpdateRequestData.from_dict(custom_action_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


