# ContactCreateRequestDataWebSitesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the WebSite. | [optional] [default to 'Other']
**address** | **str** | URL of the WebSite. | [optional] 
**default_web_site** | **bool** | Whether or not the Contact should be the default website for the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_web_sites_inner import ContactCreateRequestDataWebSitesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataWebSitesInner from a JSON string
contact_create_request_data_web_sites_inner_instance = ContactCreateRequestDataWebSitesInner.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataWebSitesInner.to_json())

# convert the object into a dict
contact_create_request_data_web_sites_inner_dict = contact_create_request_data_web_sites_inner_instance.to_dict()
# create an instance of ContactCreateRequestDataWebSitesInner from a dict
contact_create_request_data_web_sites_inner_from_dict = ContactCreateRequestDataWebSitesInner.from_dict(contact_create_request_data_web_sites_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


