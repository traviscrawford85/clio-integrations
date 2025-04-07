# MultipartBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **int** | Unique identifier of a part which defines its position within the document being uploaded. | [optional] 
**put_url** | **str** | A signed URL for uploading the file part. It expires in 10 minutes. | [optional] 

## Example

```python
from openapi_client.models.multipart_base import MultipartBase

# TODO update the JSON string below
json = "{}"
# create an instance of MultipartBase from a JSON string
multipart_base_instance = MultipartBase.from_json(json)
# print the JSON string representation of the object
print(MultipartBase.to_json())

# convert the object into a dict
multipart_base_dict = multipart_base_instance.to_dict()
# create an instance of MultipartBase from a dict
multipart_base_from_dict = MultipartBase.from_dict(multipart_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


