# CommunicationCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the Communication. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.communication_create_request_data_matter import CommunicationCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreateRequestDataMatter from a JSON string
communication_create_request_data_matter_instance = CommunicationCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreateRequestDataMatter.to_json())

# convert the object into a dict
communication_create_request_data_matter_dict = communication_create_request_data_matter_instance.to_dict()
# create an instance of CommunicationCreateRequestDataMatter from a dict
communication_create_request_data_matter_from_dict = CommunicationCreateRequestDataMatter.from_dict(communication_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


