# MatterCreateRequestDataOriginatingAttorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single User associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_originating_attorney import MatterCreateRequestDataOriginatingAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataOriginatingAttorney from a JSON string
matter_create_request_data_originating_attorney_instance = MatterCreateRequestDataOriginatingAttorney.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataOriginatingAttorney.to_json())

# convert the object into a dict
matter_create_request_data_originating_attorney_dict = matter_create_request_data_originating_attorney_instance.to_dict()
# create an instance of MatterCreateRequestDataOriginatingAttorney from a dict
matter_create_request_data_originating_attorney_from_dict = MatterCreateRequestDataOriginatingAttorney.from_dict(matter_create_request_data_originating_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


