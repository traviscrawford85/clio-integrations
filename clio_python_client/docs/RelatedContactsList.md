# RelatedContactsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RelatedContacts]**](RelatedContacts.md) | RelatedContacts List Response | 

## Example

```python
from openapi_client.models.related_contacts_list import RelatedContactsList

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedContactsList from a JSON string
related_contacts_list_instance = RelatedContactsList.from_json(json)
# print the JSON string representation of the object
print(RelatedContactsList.to_json())

# convert the object into a dict
related_contacts_list_dict = related_contacts_list_instance.to_dict()
# create an instance of RelatedContactsList from a dict
related_contacts_list_from_dict = RelatedContactsList.from_dict(related_contacts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


