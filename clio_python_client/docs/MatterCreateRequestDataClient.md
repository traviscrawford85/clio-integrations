# MatterCreateRequestDataClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Contact associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | 

## Example

```python
from openapi_client.models.matter_create_request_data_client import MatterCreateRequestDataClient

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataClient from a JSON string
matter_create_request_data_client_instance = MatterCreateRequestDataClient.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataClient.to_json())

# convert the object into a dict
matter_create_request_data_client_dict = matter_create_request_data_client_instance.to_dict()
# create an instance of MatterCreateRequestDataClient from a dict
matter_create_request_data_client_from_dict = MatterCreateRequestDataClient.from_dict(matter_create_request_data_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


