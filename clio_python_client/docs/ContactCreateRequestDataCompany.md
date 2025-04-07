# ContactCreateRequestDataCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Company associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_company import ContactCreateRequestDataCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataCompany from a JSON string
contact_create_request_data_company_instance = ContactCreateRequestDataCompany.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataCompany.to_json())

# convert the object into a dict
contact_create_request_data_company_dict = contact_create_request_data_company_instance.to_dict()
# create an instance of ContactCreateRequestDataCompany from a dict
contact_create_request_data_company_from_dict = ContactCreateRequestDataCompany.from_dict(contact_create_request_data_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


