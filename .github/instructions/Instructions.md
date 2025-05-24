---
# Copilot Custom Project Guidance

## 🎯 Purpose

This is a Clio Integration backend project using FastAPI, Clio SDK (`clio_client`), and custom Pydantic models. Copilot should assist by inferring correct types, imports, and response models.

## 📦 Structure and Expectations

- All API calls must use `clio_client.openapi_client.api` classes.
- Authentication tokens are managed via `clio.token_store.get_access_token()`.
- Use `build_full_update_request()` for constructing `MatterUpdateRequest` payloads.
- Prefer `*.InputModel` and `*.ViewModel` for request/response schemas in routes.

## ✅ Copilot Coding Style Guide

### Imports
- Prefer **absolute imports** from:
  - `clio.api.models` (custom Pydantic models)
  - `clio_client.openapi_client.models` (Clio SDK models)

### Typing
- Always annotate return types.
- Use `Optional`, `List`, `Union`, `Literal` where applicable.
- Use `.to_dict()` on Clio SDK models for JSON compatibility.

### API Integration Patterns
```python
from clio_client.openapi_client.api.matters_api import MattersApi
from clio.token_store import get_access_token
from clio_client.openapi_client.api_client import ApiClient, Configuration
```
```
def get_authenticated_api(api_cls):
    config = Configuration()
    config.api_key["Authorization"] = token  # just the token, no "Bearer"
config.api_key_prefix["Authorization"] = "Bearer"
    return api_cls(ApiClient(config))
```
Builders
Use builder patterns like:
```
from clio.builders.matter_request_builder import build_full_update_request
from clio.api.models.MatterUpdateInputModel import MatterUpdateInputModel

def update_matter(matter_id: int, payload: MatterUpdateInputModel):
    request = build_full_update_request(payload)
```
### Testing and Corrections
If import is incorrect, suggest valid one from clio_client.openapi_client.models.

If a Pydantic model is missing required fields, recommend them with Optional where applicable.

Detect when MatterUpdateRequestData(...) is expecting a Clio SDK model and suggest conversion logic.

### Examples of Preferred Code Completion

# Correct Usage:
input: MatterUpdateInputModel
return MatterUpdateRequest(data=MatterUpdateRequestData(...))

# Incorrect:
input: dict  ❌
return MatterUpdateRequest(data=input)  ❌
```

### ✅ Additional Tips for Copilot Performance

1. **Use consistent naming conventions.** Keep files like `matter_request_builder.py` and `MatterUpdateInputModel.py` clearly named.
2. **Add docstrings and type hints** everywhere – Copilot will learn from them.
3. **Install extensions** like:
   - GitHub Copilot Chat
   - Python
   - Pylance (for type checking)

