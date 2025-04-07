# LineItemList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LineItem]**](LineItem.md) | LineItem List Response | 

## Example

```python
from openapi_client.models.line_item_list import LineItemList

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemList from a JSON string
line_item_list_instance = LineItemList.from_json(json)
# print the JSON string representation of the object
print(LineItemList.to_json())

# convert the object into a dict
line_item_list_dict = line_item_list_instance.to_dict()
# create an instance of LineItemList from a dict
line_item_list_from_dict = LineItemList.from_dict(line_item_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


