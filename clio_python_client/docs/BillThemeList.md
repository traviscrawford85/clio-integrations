# BillThemeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BillTheme]**](BillTheme.md) | BillTheme List Response | 

## Example

```python
from openapi_client.models.bill_theme_list import BillThemeList

# TODO update the JSON string below
json = "{}"
# create an instance of BillThemeList from a JSON string
bill_theme_list_instance = BillThemeList.from_json(json)
# print the JSON string representation of the object
print(BillThemeList.to_json())

# convert the object into a dict
bill_theme_list_dict = bill_theme_list_instance.to_dict()
# create an instance of BillThemeList from a dict
bill_theme_list_from_dict = BillThemeList.from_dict(bill_theme_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


