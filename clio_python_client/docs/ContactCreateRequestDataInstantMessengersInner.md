# ContactCreateRequestDataInstantMessengersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the InstantMessenger. | [optional] [default to 'Other']
**address** | **str** | Address of the InstantMessenger. | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_instant_messengers_inner import ContactCreateRequestDataInstantMessengersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataInstantMessengersInner from a JSON string
contact_create_request_data_instant_messengers_inner_instance = ContactCreateRequestDataInstantMessengersInner.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataInstantMessengersInner.to_json())

# convert the object into a dict
contact_create_request_data_instant_messengers_inner_dict = contact_create_request_data_instant_messengers_inner_instance.to_dict()
# create an instance of ContactCreateRequestDataInstantMessengersInner from a dict
contact_create_request_data_instant_messengers_inner_from_dict = ContactCreateRequestDataInstantMessengersInner.from_dict(contact_create_request_data_instant_messengers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


