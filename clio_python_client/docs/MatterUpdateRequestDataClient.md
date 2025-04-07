# MatterUpdateRequestDataClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Contact associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_client import MatterUpdateRequestDataClient

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataClient from a JSON string
matter_update_request_data_client_instance = MatterUpdateRequestDataClient.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataClient.to_json())

# convert the object into a dict
matter_update_request_data_client_dict = matter_update_request_data_client_instance.to_dict()
# create an instance of MatterUpdateRequestDataClient from a dict
matter_update_request_data_client_from_dict = MatterUpdateRequestDataClient.from_dict(matter_update_request_data_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


