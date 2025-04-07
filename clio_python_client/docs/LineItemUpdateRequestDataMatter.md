# LineItemUpdateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the LineItem. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.line_item_update_request_data_matter import LineItemUpdateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemUpdateRequestDataMatter from a JSON string
line_item_update_request_data_matter_instance = LineItemUpdateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(LineItemUpdateRequestDataMatter.to_json())

# convert the object into a dict
line_item_update_request_data_matter_dict = line_item_update_request_data_matter_instance.to_dict()
# create an instance of LineItemUpdateRequestDataMatter from a dict
line_item_update_request_data_matter_from_dict = LineItemUpdateRequestDataMatter.from_dict(line_item_update_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


