# DocumentUpdateRequestDataMultipartsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **int** | The part number of multipart upload. It must be an integer between 1 to 10,000, inclusive.  Multipart upload supports upload a single file as a set of parts. Each part is a contiguous portion of the data. A &#x60;part_number&#x60; uniquely identifies a part and also defines its position within the document being uploaded. Each part must be at least 5 MB in size, except the last part. There is no minimum size limit on the last part.  The URLs of multipart upload are returned in the field, &#x60;put_url&#x60;, with the corresponding &#x60;multipart&#x60;  The API handles maximum 50 &#x60;multiparts&#x60; in one request. If the upload is split to more than 50 parts, make a PUT request with &#x60;fully_uploaded&#x60; equal to &#x60;false&#x60;, and another set of part numbers.  | [optional] 
**content_length** | **str** | The size of the part of the upload file in bytes. | [optional] 
**content_md5** | **str** | The base64-encoded 128-bit MD5 digest of the part data. This header can be used as a message integrity check to verify that the part data is the same data that was originally sent. Although it is optional, we recommend using the Content-MD5 mechanism as an end-to-end integrity check. | [optional] 

## Example

```python
from openapi_client.models.document_update_request_data_multiparts_inner import DocumentUpdateRequestDataMultipartsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequestDataMultipartsInner from a JSON string
document_update_request_data_multiparts_inner_instance = DocumentUpdateRequestDataMultipartsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequestDataMultipartsInner.to_json())

# convert the object into a dict
document_update_request_data_multiparts_inner_dict = document_update_request_data_multiparts_inner_instance.to_dict()
# create an instance of DocumentUpdateRequestDataMultipartsInner from a dict
document_update_request_data_multiparts_inner_from_dict = DocumentUpdateRequestDataMultipartsInner.from_dict(document_update_request_data_multiparts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


