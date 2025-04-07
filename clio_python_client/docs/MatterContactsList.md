# MatterContactsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MatterContacts]**](MatterContacts.md) | MatterContacts List Response | 

## Example

```python
from openapi_client.models.matter_contacts_list import MatterContactsList

# TODO update the JSON string below
json = "{}"
# create an instance of MatterContactsList from a JSON string
matter_contacts_list_instance = MatterContactsList.from_json(json)
# print the JSON string representation of the object
print(MatterContactsList.to_json())

# convert the object into a dict
matter_contacts_list_dict = matter_contacts_list_instance.to_dict()
# create an instance of MatterContactsList from a dict
matter_contacts_list_from_dict = MatterContactsList.from_dict(matter_contacts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


