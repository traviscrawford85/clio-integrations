# DocumentCopyRequestDataParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the parent object. | 
**type** | **str** | Type of parent object: * \&quot;Document\&quot; represents an existing Clio document. It is specified when you provide a new revision (or document version) to an existing document. * \&quot;Folder\&quot; represents a specified folder on Clio by folder id. It if specified when you add / move an item to a folder. * \&quot;Contact\&quot; represents a contact folder on Clio identified by contact id. It is specified when you add / move an item to a contact folder. A contact folder will be created for the specified contact if none exists already. * \&quot;Matter\&quot; represents a matter folder on Clio identified by matter id. It is specified when you add / move an item to a matter folder.  | 

## Example

```python
from openapi_client.models.document_copy_request_data_parent import DocumentCopyRequestDataParent

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCopyRequestDataParent from a JSON string
document_copy_request_data_parent_instance = DocumentCopyRequestDataParent.from_json(json)
# print the JSON string representation of the object
print(DocumentCopyRequestDataParent.to_json())

# convert the object into a dict
document_copy_request_data_parent_dict = document_copy_request_data_parent_instance.to_dict()
# create an instance of DocumentCopyRequestDataParent from a dict
document_copy_request_data_parent_from_dict = DocumentCopyRequestDataParent.from_dict(document_copy_request_data_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


