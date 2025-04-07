# ContactUpdateRequestDataInstantMessengersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the InstantMessenger. | [optional] [default to 'Other']
**address** | **str** | Address of the InstantMessenger. | [optional] 
**id** | **int** | The unique identifier for a single InstantMessenger associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated InstantMessenger is present, the InstantMessenger is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data_instant_messengers_inner import ContactUpdateRequestDataInstantMessengersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestDataInstantMessengersInner from a JSON string
contact_update_request_data_instant_messengers_inner_instance = ContactUpdateRequestDataInstantMessengersInner.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestDataInstantMessengersInner.to_json())

# convert the object into a dict
contact_update_request_data_instant_messengers_inner_dict = contact_update_request_data_instant_messengers_inner_instance.to_dict()
# create an instance of ContactUpdateRequestDataInstantMessengersInner from a dict
contact_update_request_data_instant_messengers_inner_from_dict = ContactUpdateRequestDataInstantMessengersInner.from_dict(contact_update_request_data_instant_messengers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


