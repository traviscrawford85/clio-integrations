# MatterUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **bool** | Whether or not the matter is billable. | [optional] [default to True]
**client** | [**MatterUpdateRequestDataClient**](MatterUpdateRequestDataClient.md) |  | [optional] 
**client_reference** | **str** | Client Reference string for external uses. | [optional] 
**close_date** | **date** | Date the Matter was set to closed. (Expects an ISO-8601 date). | [optional] 
**currency** | **object** | Currency of the matter | [optional] 
**custom_field_set_associations** | [**List[MatterUpdateRequestDataCustomFieldSetAssociationsInner]**](MatterUpdateRequestDataCustomFieldSetAssociationsInner.md) |  | [optional] 
**custom_field_values** | [**List[MatterUpdateRequestDataCustomFieldValuesInner]**](MatterUpdateRequestDataCustomFieldValuesInner.md) |  | [optional] 
**custom_rate** | [**MatterUpdateRequestDataCustomRate**](MatterUpdateRequestDataCustomRate.md) |  | [optional] 
**description** | **str** | Detailed description of the Matter. | [optional] 
**display_number** | **str** | Matter reference and label. Depending on the account&#39;s manual_matter_numbering setting, this is either read only (generated), or customizable. | [optional] 
**evergreen_retainer** | [**MatterUpdateRequestDataEvergreenRetainer**](MatterUpdateRequestDataEvergreenRetainer.md) |  | [optional] 
**group** | [**MatterCreateRequestDataGroup**](MatterCreateRequestDataGroup.md) |  | [optional] 
**location** | **str** | Location of the Matter. | [optional] 
**matter_budget** | [**MatterCreateRequestDataMatterBudget**](MatterCreateRequestDataMatterBudget.md) |  | [optional] 
**matter_stage** | [**MatterCreateRequestDataMatterStage**](MatterCreateRequestDataMatterStage.md) |  | [optional] 
**open_date** | **date** | Date the Matter was set to open. (Expects an ISO-8601 date). | [optional] 
**originating_attorney** | [**MatterCreateRequestDataOriginatingAttorney**](MatterCreateRequestDataOriginatingAttorney.md) |  | [optional] 
**pending_date** | **date** | Date the Matter was set to pending. (Expects an ISO-8601 date). | [optional] 
**practice_area** | [**MatterCreateRequestDataPracticeArea**](MatterCreateRequestDataPracticeArea.md) |  | [optional] 
**relationships** | [**List[MatterUpdateRequestDataRelationshipsInner]**](MatterUpdateRequestDataRelationshipsInner.md) |  | [optional] 
**reset_matter_number** | **bool** | Defaults to false. Resets the matter&#39;s number based on the account&#39;s matter numbering scheme. | [optional] [default to False]
**responsible_attorney** | [**MatterCreateRequestDataOriginatingAttorney**](MatterCreateRequestDataOriginatingAttorney.md) |  | [optional] 
**split_invoice_payers** | [**List[MatterUpdateRequestDataSplitInvoicePayersInner]**](MatterUpdateRequestDataSplitInvoicePayersInner.md) |  | [optional] 
**status** | **str** | Matter status. | [optional] 
**statute_of_limitations** | [**MatterUpdateRequestDataStatuteOfLimitations**](MatterUpdateRequestDataStatuteOfLimitations.md) |  | [optional] 
**task_template_list_instances** | [**List[MatterUpdateRequestDataTaskTemplateListInstancesInner]**](MatterUpdateRequestDataTaskTemplateListInstancesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data import MatterUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestData from a JSON string
matter_update_request_data_instance = MatterUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestData.to_json())

# convert the object into a dict
matter_update_request_data_dict = matter_update_request_data_instance.to_dict()
# create an instance of MatterUpdateRequestData from a dict
matter_update_request_data_from_dict = MatterUpdateRequestData.from_dict(matter_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


