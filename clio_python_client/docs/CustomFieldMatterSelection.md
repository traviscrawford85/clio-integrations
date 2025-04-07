# CustomFieldMatterSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CustomFieldMatterSelection* | [optional] 
**display_number** | **str** | The reference and label of the *CustomFieldMatterSelection*. Depending on the account&#39;s manual_matter_numbering setting, this is either read only (generated) or customizable. | [optional] 

## Example

```python
from openapi_client.models.custom_field_matter_selection import CustomFieldMatterSelection

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldMatterSelection from a JSON string
custom_field_matter_selection_instance = CustomFieldMatterSelection.from_json(json)
# print the JSON string representation of the object
print(CustomFieldMatterSelection.to_json())

# convert the object into a dict
custom_field_matter_selection_dict = custom_field_matter_selection_instance.to_dict()
# create an instance of CustomFieldMatterSelection from a dict
custom_field_matter_selection_from_dict = CustomFieldMatterSelection.from_dict(custom_field_matter_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


