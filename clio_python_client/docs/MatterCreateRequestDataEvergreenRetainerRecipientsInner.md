# MatterCreateRequestDataEvergreenRetainerRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the &#x60;id&#x60; of a User who will receive the trust balance notification. | [optional] 
**destroy** | **bool** | Used to remove an existing User as a recipient of the trust balance notification. | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_evergreen_retainer_recipients_inner import MatterCreateRequestDataEvergreenRetainerRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataEvergreenRetainerRecipientsInner from a JSON string
matter_create_request_data_evergreen_retainer_recipients_inner_instance = MatterCreateRequestDataEvergreenRetainerRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataEvergreenRetainerRecipientsInner.to_json())

# convert the object into a dict
matter_create_request_data_evergreen_retainer_recipients_inner_dict = matter_create_request_data_evergreen_retainer_recipients_inner_instance.to_dict()
# create an instance of MatterCreateRequestDataEvergreenRetainerRecipientsInner from a dict
matter_create_request_data_evergreen_retainer_recipients_inner_from_dict = MatterCreateRequestDataEvergreenRetainerRecipientsInner.from_dict(matter_create_request_data_evergreen_retainer_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


