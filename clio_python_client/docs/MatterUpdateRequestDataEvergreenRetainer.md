# MatterUpdateRequestDataEvergreenRetainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_threshold** | **float** | The trust balance threshold for the Matter. When the balance falls below the threshold, the retainer&#39;s associated recipients (firm users) will receive a notification. | [optional] 
**destroy** | **bool** | If this flag is set to &#x60;true&#x60;, the trust balance notification will be deleted from the Matter. | [optional] 
**recipients** | [**List[MatterCreateRequestDataEvergreenRetainerRecipientsInner]**](MatterCreateRequestDataEvergreenRetainerRecipientsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_evergreen_retainer import MatterUpdateRequestDataEvergreenRetainer

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataEvergreenRetainer from a JSON string
matter_update_request_data_evergreen_retainer_instance = MatterUpdateRequestDataEvergreenRetainer.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataEvergreenRetainer.to_json())

# convert the object into a dict
matter_update_request_data_evergreen_retainer_dict = matter_update_request_data_evergreen_retainer_instance.to_dict()
# create an instance of MatterUpdateRequestDataEvergreenRetainer from a dict
matter_update_request_data_evergreen_retainer_from_dict = MatterUpdateRequestDataEvergreenRetainer.from_dict(matter_update_request_data_evergreen_retainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


