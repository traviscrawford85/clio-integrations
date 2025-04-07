# BillRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time the *BillRecipient* was created (as a ISO-8601 timestamp) | [optional] 
**etag** | **str** | ETag for the *BillRecipient* | [optional] 
**id** | **int** | Unique identifier for the *BillRecipient* | [optional] 
**on_all_matters** | **bool** | If the associated contact is a recipient for all of the bill&#39;s matters | [optional] 
**updated_at** | **datetime** | The time the *BillRecipient* was updated (as a ISO-8601 timestamp) | [optional] 
**recipient** | [**BillRecipientContactBase**](BillRecipientContactBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.bill_recipient import BillRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of BillRecipient from a JSON string
bill_recipient_instance = BillRecipient.from_json(json)
# print the JSON string representation of the object
print(BillRecipient.to_json())

# convert the object into a dict
bill_recipient_dict = bill_recipient_instance.to_dict()
# create an instance of BillRecipient from a dict
bill_recipient_from_dict = BillRecipient.from_dict(bill_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


