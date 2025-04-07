# LegalAidUkContactBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *LegalAidUkContact* | [optional] 
**disability** | **int** | The disability of the LegalAidUkContact | [optional] 
**disability_code** | **str** | The disability code of the LegalAidUkContact | [optional] 
**ethnicity** | **int** | The ethnicity of the LegalAidUkContact | [optional] 
**ethnicity_title** | **str** | The ethnicity title of the LegalAidUkContact | [optional] 
**financially_eligible** | **bool** | The financial eligibility of the LegalAidUkContact | [optional] 
**gender** | **int** | The gender of the LegalAidUkContact | [optional] 
**gender_title** | **str** | The gender title of the LegalAidUkContact | [optional] 
**national_insurance_number** | **str** | National Insurance Number | [optional] 

## Example

```python
from openapi_client.models.legal_aid_uk_contact_base import LegalAidUkContactBase

# TODO update the JSON string below
json = "{}"
# create an instance of LegalAidUkContactBase from a JSON string
legal_aid_uk_contact_base_instance = LegalAidUkContactBase.from_json(json)
# print the JSON string representation of the object
print(LegalAidUkContactBase.to_json())

# convert the object into a dict
legal_aid_uk_contact_base_dict = legal_aid_uk_contact_base_instance.to_dict()
# create an instance of LegalAidUkContactBase from a dict
legal_aid_uk_contact_base_from_dict = LegalAidUkContactBase.from_dict(legal_aid_uk_contact_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


