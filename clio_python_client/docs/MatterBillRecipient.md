# MatterBillRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time the *MatterBillRecipient* was created (as a ISO-8601 timestamp) | [optional] 
**etag** | **str** | ETag for the *MatterBillRecipient* | [optional] 
**id** | **int** | Unique identifier for the *MatterBillRecipient* | [optional] 
**updated_at** | **datetime** | The time the *MatterBillRecipient* was last updated (as a ISO-8601 timestamp) | [optional] 
**recipient** | [**ContactBase**](ContactBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_bill_recipient import MatterBillRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of MatterBillRecipient from a JSON string
matter_bill_recipient_instance = MatterBillRecipient.from_json(json)
# print the JSON string representation of the object
print(MatterBillRecipient.to_json())

# convert the object into a dict
matter_bill_recipient_dict = matter_bill_recipient_instance.to_dict()
# create an instance of MatterBillRecipient from a dict
matter_bill_recipient_from_dict = MatterBillRecipient.from_dict(matter_bill_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


