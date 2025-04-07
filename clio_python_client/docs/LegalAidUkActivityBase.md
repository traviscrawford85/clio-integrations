# LegalAidUkActivityBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_sub_category** | **str** | Activity sub-category | [optional] 
**advocacy** | **int** | Advocacy | [optional] 
**base_rate** | **float** | Base rate | [optional] 
**bolt_ons** | **str** | Bolt ons | [optional] 
**bolt_ons_summary** | **str** | Bolt ons summary | [optional] 
**court** | **int** | Court | [optional] 
**eligible_for_sqm** | **bool** | Eligible for SQM | [optional] 
**expert** | **int** | Expert | [optional] 
**form_of_civil_legal_service** | **int** | Form of civil legal service | [optional] 
**id** | **int** | Unique identifier for the *LegalAidUkActivity* | [optional] 
**is_custom_rate** | **bool** | Flag to indicate if rate was manually entered by user | [optional] 
**json_key** | **str** | Lookup key that references JSON data | [optional] 
**region** | **int** | Region | [optional] 
**tax_exclusive** | **bool** | Flag to indicate if tax is exclusive | [optional] 
**uplift** | **float** | Uplift percentage applied to activity rate | [optional] 
**user_type** | **int** | User type | [optional] 

## Example

```python
from openapi_client.models.legal_aid_uk_activity_base import LegalAidUkActivityBase

# TODO update the JSON string below
json = "{}"
# create an instance of LegalAidUkActivityBase from a JSON string
legal_aid_uk_activity_base_instance = LegalAidUkActivityBase.from_json(json)
# print the JSON string representation of the object
print(LegalAidUkActivityBase.to_json())

# convert the object into a dict
legal_aid_uk_activity_base_dict = legal_aid_uk_activity_base_instance.to_dict()
# create an instance of LegalAidUkActivityBase from a dict
legal_aid_uk_activity_base_from_dict = LegalAidUkActivityBase.from_dict(legal_aid_uk_activity_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


