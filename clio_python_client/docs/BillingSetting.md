# BillingSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *BillingSetting* | [optional] 
**etag** | **str** | ETag for the *BillingSetting* | [optional] 
**rounded_duration** | **float** | Rounded equivalent of duration submitted | [optional] 
**rounding** | **int** | Minute increment for time rounding | [optional] 
**use_decimal_rounding** | **bool** | Round time to two decimal places | [optional] 
**currency** | **str** | Current user setting of currency | [optional] 
**currency_sign** | **str** | The sign of the current currency | [optional] 
**tax_rate** | **float** | Rate applied for primary tax on invoices using this BillingSetting | [optional] 
**tax_name** | **str** | Name shown for primary tax on invoices using this BillingSetting | [optional] 
**apply_tax_by_default** | **bool** | Used to determine if primary tax should be applied to invoices by default | [optional] 
**time_on_flat_rate_contingency_matters_is_non_billable** | **bool** | Used to determine if hourly time entries on flat rate or contingency fee matters should be non-billable by default | [optional] 
**use_secondary_tax** | **bool** | Used to determine if secondary tax applies to invoices using this BillingSetting | [optional] 
**secondary_tax_rate** | **float** | Rate applied for secondary tax on invoices using this BillingSetting | [optional] 
**secondary_tax_rule** | **str** | Used to determine if secondary tax should be applied separately or additionally to primary tax | [optional] 
**secondary_tax_name** | **str** | Name shown for secondary tax on invoices using this BillingSetting | [optional] 
**notify_after_bill_created** | **bool** | Flag to indicate if users should have the option to notify other users when generating a bill | [optional] 
**use_utbms_codes** | **bool** | Controls usage of UTBMS codes, allowing creation of coded time entries and expenses | [optional] 
**created_at** | **datetime** | The time the *BillingSetting* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *BillingSetting* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.billing_setting import BillingSetting

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSetting from a JSON string
billing_setting_instance = BillingSetting.from_json(json)
# print the JSON string representation of the object
print(BillingSetting.to_json())

# convert the object into a dict
billing_setting_dict = billing_setting_instance.to_dict()
# create an instance of BillingSetting from a dict
billing_setting_from_dict = BillingSetting.from_dict(billing_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


