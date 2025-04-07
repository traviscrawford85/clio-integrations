# PhoneNumberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PhoneNumber]**](PhoneNumber.md) | PhoneNumber List Response | 

## Example

```python
from openapi_client.models.phone_number_list import PhoneNumberList

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberList from a JSON string
phone_number_list_instance = PhoneNumberList.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberList.to_json())

# convert the object into a dict
phone_number_list_dict = phone_number_list_instance.to_dict()
# create an instance of PhoneNumberList from a dict
phone_number_list_from_dict = PhoneNumberList.from_dict(phone_number_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


