# Clio Client SDK

A reusable, auto-authenticated Python client for Clio's API.

## Install

```bash
pip install git+https://github.com/your-username/clio-client-sdk.git
```

## Usage

```python
from clio_client.session import ClioSession

session = ClioSession()
matters = session.matters_api.list_matters().data
for matter in matters:
    print(matter.display_number)
```

## Setup

- Create a `.env` file based on `.env.example`
- Ensure you have a valid `clio_token_store.json`
