# ServiceTypeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ServiceType* | [optional] 
**etag** | **str** | ETag for the *ServiceType* | [optional] 
**created_at** | **datetime** | The time the *ServiceType* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ServiceType* was last updated (as a ISO-8601 timestamp) | [optional] 
**system_id** | **int** | Server ID | [optional] 
**description** | **str** | A detailed description of the *ServiceType* | [optional] 
**default** | **bool** | Whether *ServiceType* is default for the current user | [optional] 

## Example

```python
from openapi_client.models.service_type_base import ServiceTypeBase

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTypeBase from a JSON string
service_type_base_instance = ServiceTypeBase.from_json(json)
# print the JSON string representation of the object
print(ServiceTypeBase.to_json())

# convert the object into a dict
service_type_base_dict = service_type_base_instance.to_dict()
# create an instance of ServiceTypeBase from a dict
service_type_base_from_dict = ServiceTypeBase.from_dict(service_type_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


