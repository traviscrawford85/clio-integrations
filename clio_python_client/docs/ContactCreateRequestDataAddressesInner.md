# ContactCreateRequestDataAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Address. | [optional] [default to 'Other']
**street** | **str** | Street. | [optional] 
**city** | **str** | City. | [optional] 
**province** | **str** | Province or state. | [optional] 
**postal_code** | **str** | Postal code or zip code. | [optional] 
**country** | **str** | Country | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_addresses_inner import ContactCreateRequestDataAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataAddressesInner from a JSON string
contact_create_request_data_addresses_inner_instance = ContactCreateRequestDataAddressesInner.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataAddressesInner.to_json())

# convert the object into a dict
contact_create_request_data_addresses_inner_dict = contact_create_request_data_addresses_inner_instance.to_dict()
# create an instance of ContactCreateRequestDataAddressesInner from a dict
contact_create_request_data_addresses_inner_from_dict = ContactCreateRequestDataAddressesInner.from_dict(contact_create_request_data_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


