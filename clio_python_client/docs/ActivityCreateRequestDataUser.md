# ActivityCreateRequestDataUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single User associated with the Activity. Use the keyword &#x60;null&#x60; to specify no association. On creation, if no user is specified, it will default to the current user.  If a TimeEntry is created by a Clio Connect user, the field is not editable.  | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_user import ActivityCreateRequestDataUser

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataUser from a JSON string
activity_create_request_data_user_instance = ActivityCreateRequestDataUser.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataUser.to_json())

# convert the object into a dict
activity_create_request_data_user_dict = activity_create_request_data_user_instance.to_dict()
# create an instance of ActivityCreateRequestDataUser from a dict
activity_create_request_data_user_from_dict = ActivityCreateRequestDataUser.from_dict(activity_create_request_data_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


