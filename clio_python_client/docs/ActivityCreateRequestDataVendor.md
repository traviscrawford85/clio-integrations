# ActivityCreateRequestDataVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Contact associated with a HardCostEntry. Use the keyword &#x60;null&#x60; to specify no association.  | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_vendor import ActivityCreateRequestDataVendor

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataVendor from a JSON string
activity_create_request_data_vendor_instance = ActivityCreateRequestDataVendor.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataVendor.to_json())

# convert the object into a dict
activity_create_request_data_vendor_dict = activity_create_request_data_vendor_instance.to_dict()
# create an instance of ActivityCreateRequestDataVendor from a dict
activity_create_request_data_vendor_from_dict = ActivityCreateRequestDataVendor.from_dict(activity_create_request_data_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


