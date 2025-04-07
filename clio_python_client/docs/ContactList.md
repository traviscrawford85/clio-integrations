# ContactList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Contact]**](Contact.md) | Contact List Response | 

## Example

```python
from openapi_client.models.contact_list import ContactList

# TODO update the JSON string below
json = "{}"
# create an instance of ContactList from a JSON string
contact_list_instance = ContactList.from_json(json)
# print the JSON string representation of the object
print(ContactList.to_json())

# convert the object into a dict
contact_list_dict = contact_list_instance.to_dict()
# create an instance of ContactList from a dict
contact_list_from_dict = ContactList.from_dict(contact_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


