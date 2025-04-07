# ActivityCreateRequestDataActivityDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single ActivityDescription associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**utbms_task_id** | **int** | The unique identifier for a single UtbmsTask associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**utbms_activity_id** | **int** | The unique identifier for a single UtbmsActivity associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_activity_description import ActivityCreateRequestDataActivityDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataActivityDescription from a JSON string
activity_create_request_data_activity_description_instance = ActivityCreateRequestDataActivityDescription.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataActivityDescription.to_json())

# convert the object into a dict
activity_create_request_data_activity_description_dict = activity_create_request_data_activity_description_instance.to_dict()
# create an instance of ActivityCreateRequestDataActivityDescription from a dict
activity_create_request_data_activity_description_from_dict = ActivityCreateRequestDataActivityDescription.from_dict(activity_create_request_data_activity_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


