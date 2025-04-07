# LaukCivilCertificatedRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *LaukCivilCertificatedRate* | [optional] 
**activity** | **str** | Activity of the *LaukCivilCertificatedRate* | [optional] 
**activity_sub_category** | **str** | Activity sub-category | [optional] 
**activity_type** | **str** | Activity type | [optional] 
**attended_several_hearings_for_multiple_clients** | **bool** | Multiple hearings for multiple clients indicator | [optional] 
**category_of_law** | **str** | Category of law | [optional] 
**created_at** | **datetime** | The time the *LaukCivilCertificatedRate* was created (as a ISO-8601 timestamp) | [optional] 
**change_of_solicitor** | **bool** | Change of solicitor indicator | [optional] 
**court** | **str** | Court associated | [optional] 
**eligible_for_sqm** | **bool** | SQM eligibility (Legal Aid England and Wales) | [optional] 
**exceptional** | **float** | Fee applied for high activity count | [optional] 
**exceptional_warning** | **str** | Warning for exceptional status | [optional] 
**etag** | **str** | ETag for the *LaukCivilCertificatedRate* | [optional] 
**fee** | **float** | Fee amount | [optional] 
**fee_scheme** | **str** | Fee scheme | [optional] 
**first_conducting_solicitor** | **bool** | First conducting solicitor indicator | [optional] 
**key** | **str** | Unique key | [optional] 
**number_of_clients** | **str** | Number of clients | [optional] 
**party** | **str** | Associated party | [optional] 
**post_transfer_clients_represented** | **str** | Post-transfer clients represented | [optional] 
**rate_type** | **str** | Rate type | [optional] 
**region** | **str** | Region | [optional] 
**session_type** | **str** | Session type | [optional] 
**user_type** | **str** | User type | [optional] 
**updated_at** | **datetime** | The time the *LaukCivilCertificatedRate* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.lauk_civil_certificated_rate import LaukCivilCertificatedRate

# TODO update the JSON string below
json = "{}"
# create an instance of LaukCivilCertificatedRate from a JSON string
lauk_civil_certificated_rate_instance = LaukCivilCertificatedRate.from_json(json)
# print the JSON string representation of the object
print(LaukCivilCertificatedRate.to_json())

# convert the object into a dict
lauk_civil_certificated_rate_dict = lauk_civil_certificated_rate_instance.to_dict()
# create an instance of LaukCivilCertificatedRate from a dict
lauk_civil_certificated_rate_from_dict = LaukCivilCertificatedRate.from_dict(lauk_civil_certificated_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


