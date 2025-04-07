# BillingSettingShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BillingSetting**](BillingSetting.md) |  | 

## Example

```python
from openapi_client.models.billing_setting_show import BillingSettingShow

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSettingShow from a JSON string
billing_setting_show_instance = BillingSettingShow.from_json(json)
# print the JSON string representation of the object
print(BillingSettingShow.to_json())

# convert the object into a dict
billing_setting_show_dict = billing_setting_show_instance.to_dict()
# create an instance of BillingSettingShow from a dict
billing_setting_show_from_dict = BillingSettingShow.from_dict(billing_setting_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


