# PhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *PhoneNumber* | [optional] 
**etag** | **str** | ETag for the *PhoneNumber* | [optional] 
**number** | **str** | Contact&#39;s Phone Number | [optional] 
**name** | **str** | The type of *PhoneNumber* it is | [optional] 
**primary** | **bool** | Whether it is default for this contact | [optional] 
**created_at** | **datetime** | The time the *PhoneNumber* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *PhoneNumber* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.phone_number import PhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumber from a JSON string
phone_number_instance = PhoneNumber.from_json(json)
# print the JSON string representation of the object
print(PhoneNumber.to_json())

# convert the object into a dict
phone_number_dict = phone_number_instance.to_dict()
# create an instance of PhoneNumber from a dict
phone_number_from_dict = PhoneNumber.from_dict(phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


