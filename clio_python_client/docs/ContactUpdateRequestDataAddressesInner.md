# ContactUpdateRequestDataAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Address. | [optional] [default to 'Other']
**street** | **str** | Street. | [optional] 
**city** | **str** | City. | [optional] 
**province** | **str** | Province or state. | [optional] 
**postal_code** | **str** | Postal code or zip code. | [optional] 
**country** | **str** | Country | [optional] 
**id** | **int** | The unique identifier for a single Address associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated Address is present, the Address is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data_addresses_inner import ContactUpdateRequestDataAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestDataAddressesInner from a JSON string
contact_update_request_data_addresses_inner_instance = ContactUpdateRequestDataAddressesInner.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestDataAddressesInner.to_json())

# convert the object into a dict
contact_update_request_data_addresses_inner_dict = contact_update_request_data_addresses_inner_instance.to_dict()
# create an instance of ContactUpdateRequestDataAddressesInner from a dict
contact_update_request_data_addresses_inner_from_dict = ContactUpdateRequestDataAddressesInner.from_dict(contact_update_request_data_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


