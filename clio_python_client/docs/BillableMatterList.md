# BillableMatterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BillableMatter]**](BillableMatter.md) | BillableMatter List Response | 

## Example

```python
from openapi_client.models.billable_matter_list import BillableMatterList

# TODO update the JSON string below
json = "{}"
# create an instance of BillableMatterList from a JSON string
billable_matter_list_instance = BillableMatterList.from_json(json)
# print the JSON string representation of the object
print(BillableMatterList.to_json())

# convert the object into a dict
billable_matter_list_dict = billable_matter_list_instance.to_dict()
# create an instance of BillableMatterList from a dict
billable_matter_list_from_dict = BillableMatterList.from_dict(billable_matter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


