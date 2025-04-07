# MatterBillRecipientBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time the *MatterBillRecipient* was created (as a ISO-8601 timestamp) | [optional] 
**etag** | **str** | ETag for the *MatterBillRecipient* | [optional] 
**id** | **int** | Unique identifier for the *MatterBillRecipient* | [optional] 
**updated_at** | **datetime** | The time the *MatterBillRecipient* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.matter_bill_recipient_base import MatterBillRecipientBase

# TODO update the JSON string below
json = "{}"
# create an instance of MatterBillRecipientBase from a JSON string
matter_bill_recipient_base_instance = MatterBillRecipientBase.from_json(json)
# print the JSON string representation of the object
print(MatterBillRecipientBase.to_json())

# convert the object into a dict
matter_bill_recipient_base_dict = matter_bill_recipient_base_instance.to_dict()
# create an instance of MatterBillRecipientBase from a dict
matter_bill_recipient_base_from_dict = MatterBillRecipientBase.from_dict(matter_bill_recipient_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


