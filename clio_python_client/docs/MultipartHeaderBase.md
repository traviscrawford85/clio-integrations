# MultipartHeaderBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required HTTP header field name for uploading. | [optional] 
**value** | **str** | Required HTTP header field value for uploading. | [optional] 

## Example

```python
from openapi_client.models.multipart_header_base import MultipartHeaderBase

# TODO update the JSON string below
json = "{}"
# create an instance of MultipartHeaderBase from a JSON string
multipart_header_base_instance = MultipartHeaderBase.from_json(json)
# print the JSON string representation of the object
print(MultipartHeaderBase.to_json())

# convert the object into a dict
multipart_header_base_dict = multipart_header_base_instance.to_dict()
# create an instance of MultipartHeaderBase from a dict
multipart_header_base_from_dict = MultipartHeaderBase.from_dict(multipart_header_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


