# LineItemUpdateRequestDataActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Activity associated with the LineItem. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.line_item_update_request_data_activity import LineItemUpdateRequestDataActivity

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemUpdateRequestDataActivity from a JSON string
line_item_update_request_data_activity_instance = LineItemUpdateRequestDataActivity.from_json(json)
# print the JSON string representation of the object
print(LineItemUpdateRequestDataActivity.to_json())

# convert the object into a dict
line_item_update_request_data_activity_dict = line_item_update_request_data_activity_instance.to_dict()
# create an instance of LineItemUpdateRequestDataActivity from a dict
line_item_update_request_data_activity_from_dict = LineItemUpdateRequestDataActivity.from_dict(line_item_update_request_data_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


