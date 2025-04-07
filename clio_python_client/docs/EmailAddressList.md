# EmailAddressList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EmailAddress]**](EmailAddress.md) | EmailAddress List Response | 

## Example

```python
from openapi_client.models.email_address_list import EmailAddressList

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddressList from a JSON string
email_address_list_instance = EmailAddressList.from_json(json)
# print the JSON string representation of the object
print(EmailAddressList.to_json())

# convert the object into a dict
email_address_list_dict = email_address_list_instance.to_dict()
# create an instance of EmailAddressList from a dict
email_address_list_from_dict = EmailAddressList.from_dict(email_address_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


