# ContactCreateRequestDataAvatar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | The avatar image for the *Contact*, base64-encoded. Must be a valid GIF, JPG, or PNG image of less than 2 megabytes in size. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated Avatar is present, the Avatar is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_avatar import ContactCreateRequestDataAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataAvatar from a JSON string
contact_create_request_data_avatar_instance = ContactCreateRequestDataAvatar.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataAvatar.to_json())

# convert the object into a dict
contact_create_request_data_avatar_dict = contact_create_request_data_avatar_instance.to_dict()
# create an instance of ContactCreateRequestDataAvatar from a dict
contact_create_request_data_avatar_from_dict = ContactCreateRequestDataAvatar.from_dict(contact_create_request_data_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


