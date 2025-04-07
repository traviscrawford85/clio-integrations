# ContactCreateRequestDataCoCounselRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | Billing rate if the Contact is a co-counsel.  Note: this value can only be provided during PATCH requests. It cannot be provided at the time a Contact is created (i.e. POST requests).  | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_co_counsel_rate import ContactCreateRequestDataCoCounselRate

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataCoCounselRate from a JSON string
contact_create_request_data_co_counsel_rate_instance = ContactCreateRequestDataCoCounselRate.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataCoCounselRate.to_json())

# convert the object into a dict
contact_create_request_data_co_counsel_rate_dict = contact_create_request_data_co_counsel_rate_instance.to_dict()
# create an instance of ContactCreateRequestDataCoCounselRate from a dict
contact_create_request_data_co_counsel_rate_from_dict = ContactCreateRequestDataCoCounselRate.from_dict(contact_create_request_data_co_counsel_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


