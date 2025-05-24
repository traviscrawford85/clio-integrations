from clio_client.openapi_client.models.custom_action_base import CustomActionBase

model_cls = CustomActionBase
for name, field in model_cls.model_fields.items():
    print(f"{name}: {field.annotation}")

# print(inspect.signature(CustomAction))

# print(model_cls.model_fields)


