# Multipart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **int** | Unique identifier of a part which defines its position within the document being uploaded. | [optional] 
**put_url** | **str** | A signed URL for uploading the file part. It expires in 10 minutes. | [optional] 
**put_headers** | [**List[MultipartHeaderBase]**](MultipartHeaderBase.md) | MultipartHeader | [optional] 

## Example

```python
from openapi_client.models.multipart import Multipart

# TODO update the JSON string below
json = "{}"
# create an instance of Multipart from a JSON string
multipart_instance = Multipart.from_json(json)
# print the JSON string representation of the object
print(Multipart.to_json())

# convert the object into a dict
multipart_dict = multipart_instance.to_dict()
# create an instance of Multipart from a dict
multipart_from_dict = Multipart.from_dict(multipart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


