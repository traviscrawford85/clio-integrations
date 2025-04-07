# MatterCreateRequestDataEvergreenRetainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_threshold** | **float** | The trust balance threshold for the Matter. When the balance falls below the threshold, the retainer&#39;s associated recipients (firm users) will receive a notification. | [optional] 
**recipients** | [**List[MatterCreateRequestDataEvergreenRetainerRecipientsInner]**](MatterCreateRequestDataEvergreenRetainerRecipientsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_evergreen_retainer import MatterCreateRequestDataEvergreenRetainer

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataEvergreenRetainer from a JSON string
matter_create_request_data_evergreen_retainer_instance = MatterCreateRequestDataEvergreenRetainer.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataEvergreenRetainer.to_json())

# convert the object into a dict
matter_create_request_data_evergreen_retainer_dict = matter_create_request_data_evergreen_retainer_instance.to_dict()
# create an instance of MatterCreateRequestDataEvergreenRetainer from a dict
matter_create_request_data_evergreen_retainer_from_dict = MatterCreateRequestDataEvergreenRetainer.from_dict(matter_create_request_data_evergreen_retainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


