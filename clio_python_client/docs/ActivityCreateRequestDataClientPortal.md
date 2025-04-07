# ActivityCreateRequestDataClientPortal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single ClientPortal associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_client_portal import ActivityCreateRequestDataClientPortal

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataClientPortal from a JSON string
activity_create_request_data_client_portal_instance = ActivityCreateRequestDataClientPortal.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataClientPortal.to_json())

# convert the object into a dict
activity_create_request_data_client_portal_dict = activity_create_request_data_client_portal_instance.to_dict()
# create an instance of ActivityCreateRequestDataClientPortal from a dict
activity_create_request_data_client_portal_from_dict = ActivityCreateRequestDataClientPortal.from_dict(activity_create_request_data_client_portal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


