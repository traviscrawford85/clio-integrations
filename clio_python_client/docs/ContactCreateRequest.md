# ContactCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ContactCreateRequestData**](ContactCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.contact_create_request import ContactCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequest from a JSON string
contact_create_request_instance = ContactCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequest.to_json())

# convert the object into a dict
contact_create_request_dict = contact_create_request_instance.to_dict()
# create an instance of ContactCreateRequest from a dict
contact_create_request_from_dict = ContactCreateRequest.from_dict(contact_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


