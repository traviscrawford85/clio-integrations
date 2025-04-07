# ClioCreatorBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_owner** | **bool** | Whether the *ClioCreator* is the owner of the account | [optional] 
**clio_connect** | **bool** | Whether the *ClioCreator* is a Clio Connect user | [optional] 
**court_rules_default_attendee** | **bool** | Whether the *ClioCreator* is a default attendee for court rules events | [optional] 
**default_calendar_id** | **int** | Default calendar id for *ClioCreator*. | [optional] 
**email** | **str** | The email of the *ClioCreator* | [optional] 
**enabled** | **bool** | Whether the *ClioCreator* is allowed to log in | [optional] 
**etag** | **str** | ETag for the *ClioCreator* | [optional] 
**id** | **int** | Unique identifier for the *ClioCreator* | [optional] 
**type** | **str** | The type of the *ClioCreator* | [optional] 
**initials** | **str** | The initials of the *ClioCreator* | [optional] 
**first_name** | **str** | The first name of the *ClioCreator* | [optional] 
**last_name** | **str** | The last name of the *ClioCreator* | [optional] 
**name** | **str** | The full name of the *ClioCreator* | [optional] 
**phone_number** | **str** | The primary phone number for the *ClioCreator*. | [optional] 
**rate** | **float** | Default user activity rate for *ClioCreator*. | [optional] 
**subscription_type** | **str** | The subscription type of the *ClioCreator* | [optional] 
**time_zone** | **str** | The selected time zone of the *ClioCreator* | [optional] 
**roles** | **List[str]** | An array of roles assigned to this *ClioCreator* | [optional] 
**created_at** | **datetime** | The time the *ClioCreator* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ClioCreator* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.clio_creator_base import ClioCreatorBase

# TODO update the JSON string below
json = "{}"
# create an instance of ClioCreatorBase from a JSON string
clio_creator_base_instance = ClioCreatorBase.from_json(json)
# print the JSON string representation of the object
print(ClioCreatorBase.to_json())

# convert the object into a dict
clio_creator_base_dict = clio_creator_base_instance.to_dict()
# create an instance of ClioCreatorBase from a dict
clio_creator_base_from_dict = ClioCreatorBase.from_dict(clio_creator_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


