# PracticeAreaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PracticeArea]**](PracticeArea.md) | PracticeArea List Response | 

## Example

```python
from openapi_client.models.practice_area_list import PracticeAreaList

# TODO update the JSON string below
json = "{}"
# create an instance of PracticeAreaList from a JSON string
practice_area_list_instance = PracticeAreaList.from_json(json)
# print the JSON string representation of the object
print(PracticeAreaList.to_json())

# convert the object into a dict
practice_area_list_dict = practice_area_list_instance.to_dict()
# create an instance of PracticeAreaList from a dict
practice_area_list_from_dict = PracticeAreaList.from_dict(practice_area_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


