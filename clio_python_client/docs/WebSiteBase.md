# WebSiteBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *WebSite* | [optional] 
**etag** | **str** | ETag for the *WebSite* | [optional] 
**address** | **str** | The address of the *WebSite* | [optional] 
**name** | **str** | The type of *WebSite* it is | [optional] 
**default_web_site** | **bool** | Whether it is the default for this contact | [optional] 
**created_at** | **datetime** | The time the *WebSite* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *WebSite* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.web_site_base import WebSiteBase

# TODO update the JSON string below
json = "{}"
# create an instance of WebSiteBase from a JSON string
web_site_base_instance = WebSiteBase.from_json(json)
# print the JSON string representation of the object
print(WebSiteBase.to_json())

# convert the object into a dict
web_site_base_dict = web_site_base_instance.to_dict()
# create an instance of WebSiteBase from a dict
web_site_base_from_dict = WebSiteBase.from_dict(web_site_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


