# MatterDocketCreateRequestDataTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Trigger associated with the MatterDocket. The keyword &#x60;null&#x60; is not valid for this field. | 

## Example

```python
from openapi_client.models.matter_docket_create_request_data_trigger import MatterDocketCreateRequestDataTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of MatterDocketCreateRequestDataTrigger from a JSON string
matter_docket_create_request_data_trigger_instance = MatterDocketCreateRequestDataTrigger.from_json(json)
# print the JSON string representation of the object
print(MatterDocketCreateRequestDataTrigger.to_json())

# convert the object into a dict
matter_docket_create_request_data_trigger_dict = matter_docket_create_request_data_trigger_instance.to_dict()
# create an instance of MatterDocketCreateRequestDataTrigger from a dict
matter_docket_create_request_data_trigger_from_dict = MatterDocketCreateRequestDataTrigger.from_dict(matter_docket_create_request_data_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


