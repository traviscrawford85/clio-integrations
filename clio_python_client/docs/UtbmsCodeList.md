# UtbmsCodeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UtbmsCode]**](UtbmsCode.md) | UtbmsCode List Response | 

## Example

```python
from openapi_client.models.utbms_code_list import UtbmsCodeList

# TODO update the JSON string below
json = "{}"
# create an instance of UtbmsCodeList from a JSON string
utbms_code_list_instance = UtbmsCodeList.from_json(json)
# print the JSON string representation of the object
print(UtbmsCodeList.to_json())

# convert the object into a dict
utbms_code_list_dict = utbms_code_list_instance.to_dict()
# create an instance of UtbmsCodeList from a dict
utbms_code_list_from_dict = UtbmsCodeList.from_dict(utbms_code_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


