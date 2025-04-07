# EmailAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *EmailAddress* | [optional] 
**etag** | **str** | ETag for the *EmailAddress* | [optional] 
**address** | **str** | The address of the *EmailAddress* | [optional] 
**name** | **str** | A descriptive name for the *EmailAddress. Common values include &#x60;Home&#x60;, &#x60;Work&#x60;, and &#x60;Other&#x60;, as these are the only selectable options within Clio Manage, but other values may be returned for this field. | [optional] 
**primary** | **bool** | Whether it is the default for this contact | [optional] 
**created_at** | **datetime** | The time the *EmailAddress* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *EmailAddress* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.email_address import EmailAddress

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddress from a JSON string
email_address_instance = EmailAddress.from_json(json)
# print the JSON string representation of the object
print(EmailAddress.to_json())

# convert the object into a dict
email_address_dict = email_address_instance.to_dict()
# create an instance of EmailAddress from a dict
email_address_from_dict = EmailAddress.from_dict(email_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


