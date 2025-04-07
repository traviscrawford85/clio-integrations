# ActivityUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_description** | [**ActivityCreateRequestDataActivityDescription**](ActivityCreateRequestDataActivityDescription.md) |  | [optional] 
**calendar_entry** | [**ActivityCreateRequestDataCalendarEntry**](ActivityCreateRequestDataCalendarEntry.md) |  | [optional] 
**client_portal** | [**ActivityCreateRequestDataClientPortal**](ActivityCreateRequestDataClientPortal.md) |  | [optional] 
**communication** | [**ActivityCreateRequestDataCommunication**](ActivityCreateRequestDataCommunication.md) |  | [optional] 
**contact_note** | [**ActivityCreateRequestDataContactNote**](ActivityCreateRequestDataContactNote.md) |  | [optional] 
**var_date** | **date** | The date the Activity was performed. (Expects an ISO-8601 date). | [optional] 
**expense_category** | [**ActivityCreateRequestDataExpenseCategory**](ActivityCreateRequestDataExpenseCategory.md) |  | [optional] 
**matter** | [**ActivityCreateRequestDataMatter**](ActivityCreateRequestDataMatter.md) |  | [optional] 
**matter_note** | [**ActivityCreateRequestDataContactNote**](ActivityCreateRequestDataContactNote.md) |  | [optional] 
**no_charge** | **bool** | Whether the non-billable *Activity* will be shown on the bill. | [optional] 
**non_billable** | **bool** | Whether or not this Activity is prevented from appearing as a line item in a bill. Only valid for non-billed TimeEntries, and with the exception of the Activity having no_charge set to true.  | [optional] 
**note** | **str** | A custom note to describe what the Activity is for. | [optional] 
**price** | **float** | For an ExpenseEntry, HardCostEntry, and SoftCostEntry, it is the expense amount.  [Support Link for ExpenseEntry](https://help.clio.com/hc/en-us/articles/9289745356571-Expenses)  [Support Link for HardCostEntry and SoftCostEntry](https://help.clio.com/hc/en-us/articles/9289745356571-Expenses#enable-hard-and-soft-cost-expenses-0-0)  For a TimeEntry, it is the hourly or flat amount. When updating a TimeEntry, if the price is not given or the user does not have the permission to view the rate, and its activity description, matter and/or user is changed, the price is reset according to the rate defined for the activity description, matter, client or user.  [Support Link for Rates Hierarchy](https://help.clio.com/hc/en-us/articles/9289801180187-Rates-and-Rate-Hierarchies-)  [Support Link for Billing Rate Visibility](https://help.clio.com/hc/en-us/articles/9285360193819-Permissions-and-Billing-Rates#billing-rate-visibility-0-3)  | [optional] 
**quantity** | **float** | The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.  **Version &lt;&#x3D; 4.0.3:** The number of hours the TimeEntry took.  **Latest version:** The number of seconds the TimeEntry took.  | [optional] 
**reference** | **str** | A check reference for a HardCostEntry. | [optional] 
**start_timer** | **bool** | Whether or not a timer should be started for this Activity. Only valid for non-FlatRate, non-billed TimeEntries. | [optional] 
**task** | [**ActivityCreateRequestDataTask**](ActivityCreateRequestDataTask.md) |  | [optional] 
**tax_setting** | **str** | The option denoting whether primary tax, secondary tax, or both is applied to an expense entry. | [optional] 
**text_message_conversation** | [**ActivityCreateRequestDataTextMessageConversation**](ActivityCreateRequestDataTextMessageConversation.md) |  | [optional] 
**type** | **str** | The type of the Activity. | [optional] 
**user** | [**ActivityCreateRequestDataUser**](ActivityCreateRequestDataUser.md) |  | [optional] 
**utbms_expense** | [**ActivityCreateRequestDataUtbmsExpense**](ActivityCreateRequestDataUtbmsExpense.md) |  | [optional] 
**vendor** | [**ActivityCreateRequestDataVendor**](ActivityCreateRequestDataVendor.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_update_request_data import ActivityUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityUpdateRequestData from a JSON string
activity_update_request_data_instance = ActivityUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ActivityUpdateRequestData.to_json())

# convert the object into a dict
activity_update_request_data_dict = activity_update_request_data_instance.to_dict()
# create an instance of ActivityUpdateRequestData from a dict
activity_update_request_data_from_dict = ActivityUpdateRequestData.from_dict(activity_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


