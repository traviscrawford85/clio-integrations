# ClioPaymentsLinkCreateRequestDataSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the record associated with the payment link. | 
**type** | **str** | The type of the record associated with the payment link. The type of record determines the behavior of the payment link.  Type of subject object: * &#39;BankAccount&#39; results in a payment link for a direct payment. * &#39;Bill&#39; results in a payment link for paying an existing invoice or trust request. * &#39;Contact&#39; results in a payment link for paying the outstanding invoices of a contact.  | 

## Example

```python
from openapi_client.models.clio_payments_link_create_request_data_subject import ClioPaymentsLinkCreateRequestDataSubject

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLinkCreateRequestDataSubject from a JSON string
clio_payments_link_create_request_data_subject_instance = ClioPaymentsLinkCreateRequestDataSubject.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLinkCreateRequestDataSubject.to_json())

# convert the object into a dict
clio_payments_link_create_request_data_subject_dict = clio_payments_link_create_request_data_subject_instance.to_dict()
# create an instance of ClioPaymentsLinkCreateRequestDataSubject from a dict
clio_payments_link_create_request_data_subject_from_dict = ClioPaymentsLinkCreateRequestDataSubject.from_dict(clio_payments_link_create_request_data_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


