# BillThemeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *BillTheme* | [optional] 
**etag** | **str** | ETag for the *BillTheme* | [optional] 
**created_at** | **datetime** | The time the *BillTheme* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *BillTheme* was last updated (as a ISO-8601 timestamp) | [optional] 
**account_id** | **int** | The account number the *BillTheme* belongs to | [optional] 
**default** | **bool** | Whether the *BillTheme* is the default for its account | [optional] 
**name** | **str** | The name of the *BillTheme* | [optional] 
**config** | **str** | The configuration of the *BillTheme* | [optional] 

## Example

```python
from openapi_client.models.bill_theme_base import BillThemeBase

# TODO update the JSON string below
json = "{}"
# create an instance of BillThemeBase from a JSON string
bill_theme_base_instance = BillThemeBase.from_json(json)
# print the JSON string representation of the object
print(BillThemeBase.to_json())

# convert the object into a dict
bill_theme_base_dict = bill_theme_base_instance.to_dict()
# create an instance of BillThemeBase from a dict
bill_theme_base_from_dict = BillThemeBase.from_dict(bill_theme_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


