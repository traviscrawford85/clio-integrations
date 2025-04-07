# CommunicationUpdateRequestDataExternalPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single ExternalProperty associated with the Communication. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**name** | **str** | The ExternalProperty name. Note: **there is a limit of 5 external_properties per Communication** | [optional] 
**value** | **str** | The ExternalProperty value. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated ExternalProperty is present, the ExternalProperty is deleted from the Communication. | [optional] 

## Example

```python
from openapi_client.models.communication_update_request_data_external_properties_inner import CommunicationUpdateRequestDataExternalPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationUpdateRequestDataExternalPropertiesInner from a JSON string
communication_update_request_data_external_properties_inner_instance = CommunicationUpdateRequestDataExternalPropertiesInner.from_json(json)
# print the JSON string representation of the object
print(CommunicationUpdateRequestDataExternalPropertiesInner.to_json())

# convert the object into a dict
communication_update_request_data_external_properties_inner_dict = communication_update_request_data_external_properties_inner_instance.to_dict()
# create an instance of CommunicationUpdateRequestDataExternalPropertiesInner from a dict
communication_update_request_data_external_properties_inner_from_dict = CommunicationUpdateRequestDataExternalPropertiesInner.from_dict(communication_update_request_data_external_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


