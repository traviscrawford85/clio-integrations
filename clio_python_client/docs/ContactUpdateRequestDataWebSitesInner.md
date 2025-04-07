# ContactUpdateRequestDataWebSitesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the WebSite. | [optional] [default to 'Other']
**address** | **str** | URL of the WebSite. | [optional] 
**id** | **int** | The unique identifier for a single WebSite associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**default_web_site** | **bool** | Whether or not the Contact should be the default website for the Contact. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated WebSite is present, the WebSite is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data_web_sites_inner import ContactUpdateRequestDataWebSitesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestDataWebSitesInner from a JSON string
contact_update_request_data_web_sites_inner_instance = ContactUpdateRequestDataWebSitesInner.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestDataWebSitesInner.to_json())

# convert the object into a dict
contact_update_request_data_web_sites_inner_dict = contact_update_request_data_web_sites_inner_instance.to_dict()
# create an instance of ContactUpdateRequestDataWebSitesInner from a dict
contact_update_request_data_web_sites_inner_from_dict = ContactUpdateRequestDataWebSitesInner.from_dict(contact_update_request_data_web_sites_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


