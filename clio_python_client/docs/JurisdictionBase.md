# JurisdictionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Jurisdiction* | [optional] 
**etag** | **str** | ETag for the *Jurisdiction* | [optional] 
**created_at** | **datetime** | The time the *Jurisdiction* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Jurisdiction* was last updated (as a ISO-8601 timestamp) | [optional] 
**system_id** | **int** | Server ID | [optional] 
**description** | **str** | Description | [optional] 
**default** | **bool** | Whether the *Jurisdiction* is default for the current user | [optional] 
**display_timezone** | **str** | Formatted IANA timezone with UTC offset | [optional] 
**valid_subscription** | **bool** | Boolean value for whether the user has the jurisdictions | [optional] 
**is_local_timezone** | **bool** | Boolean value for when the timezone is in the local users timezone | [optional] 

## Example

```python
from openapi_client.models.jurisdiction_base import JurisdictionBase

# TODO update the JSON string below
json = "{}"
# create an instance of JurisdictionBase from a JSON string
jurisdiction_base_instance = JurisdictionBase.from_json(json)
# print the JSON string representation of the object
print(JurisdictionBase.to_json())

# convert the object into a dict
jurisdiction_base_dict = jurisdiction_base_instance.to_dict()
# create an instance of JurisdictionBase from a dict
jurisdiction_base_from_dict = JurisdictionBase.from_dict(jurisdiction_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


