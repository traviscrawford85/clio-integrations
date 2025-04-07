# MatterCreateRequestDataPracticeArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single PracticeArea associated with the Matter. Use the keyword &#x60;null&#x60; to specify no association. | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_practice_area import MatterCreateRequestDataPracticeArea

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataPracticeArea from a JSON string
matter_create_request_data_practice_area_instance = MatterCreateRequestDataPracticeArea.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataPracticeArea.to_json())

# convert the object into a dict
matter_create_request_data_practice_area_dict = matter_create_request_data_practice_area_instance.to_dict()
# create an instance of MatterCreateRequestDataPracticeArea from a dict
matter_create_request_data_practice_area_from_dict = MatterCreateRequestDataPracticeArea.from_dict(matter_create_request_data_practice_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


