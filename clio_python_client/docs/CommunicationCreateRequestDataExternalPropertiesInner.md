# CommunicationCreateRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per Communication** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 

## Example

```python
from openapi_client.models.communication_create_request_data_external_properties_inner import CommunicationCreateRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreateRequestDataExternalPropertiesInner from a JSON string
communication_create_request_data_external_properties_inner_instance = CommunicationCreateRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreateRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
communication_create_request_data_external_properties_inner_dict = communication_create_request_data_external_properties_inner_instance.to_dict()
# create an instance of CommunicationCreateRequestDataExternalPropertiesInner from a dict
communication_create_request_data_external_properties_inner_from_dict = CommunicationCreateRequestDataExternalPropertiesInner.from_dict(communication_create_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


