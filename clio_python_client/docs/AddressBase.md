# AddressBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Address* | [optional] 
**etag** | **str** | ETag for the *Address* | [optional] 
**street** | **str** | Street of the *Address* | [optional] 
**city** | **str** | City of the *Address* | [optional] 
**province** | **str** | Province or state of the *Address* | [optional] 
**postal_code** | **str** | Postal code of the *Address* | [optional] 
**country** | **str** | Country of the *Address* | [optional] 
**name** | **str** | The name of the *Address* | [optional] 
**created_at** | **datetime** | The time the *Address* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Address* was last updated (as a ISO-8601 timestamp) | [optional] 
**primary** | **bool** | Whether it is the default for this contact | [optional] 

## Example

```python
from openapi_client.models.address_base import AddressBase

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBase from a JSON string
address_base_instance = AddressBase.from_json(json)
# print the JSON string representation of the object
print(AddressBase.to_json())

# convert the object into a dict
address_base_dict = address_base_instance.to_dict()
# create an instance of AddressBase from a dict
address_base_from_dict = AddressBase.from_dict(address_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


