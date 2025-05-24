# Project Goals for Copilot Agent

## Primary Objective
Audit the Clio integration project to ensure it:
- Uses a single, consistent method for authenticating with the Clio API
- Stores and retrieves tokens only from the database, not from files
- Configures the OpenAPI client correctly using the Clio `access_token` (no double "Bearer")
- Uses the correct base URL: `https://app.clio.com/api/v4`

## Specific Audit Tasks

### 1. Token Usage
- Verify `get_access_token()` is used uniformly across the codebase.
- Ensure `access_token` is retrieved from the SQLite database.
- Detect and flag any leftover references to `clio_token_store.json`.

### 2. OpenAPI Client Configuration
- Confirm that OpenAPI clients are configured as:
  ```python
  config = Configuration(host="https://app.clio.com/api/v4")
  config.api_key["Authorization"] = token
  config.api_key_prefix["Authorization"] = "Bearer"

## General Instructions

- We are auditing and cleaning up the Clio integration codebase.
- Use `get_access_token()` for all token usage.
- Use OpenAPI client with:
  ```python
  config.api_key["Authorization"] = token
  config.api_key_prefix["Authorization"] = "Bearer"
