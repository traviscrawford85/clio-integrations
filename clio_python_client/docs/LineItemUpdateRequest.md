# LineItemUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LineItemUpdateRequestData**](LineItemUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.line_item_update_request import LineItemUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemUpdateRequest from a JSON string
line_item_update_request_instance = LineItemUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(LineItemUpdateRequest.to_json())

# convert the object into a dict
line_item_update_request_dict = line_item_update_request_instance.to_dict()
# create an instance of LineItemUpdateRequest from a dict
line_item_update_request_from_dict = LineItemUpdateRequest.from_dict(line_item_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


